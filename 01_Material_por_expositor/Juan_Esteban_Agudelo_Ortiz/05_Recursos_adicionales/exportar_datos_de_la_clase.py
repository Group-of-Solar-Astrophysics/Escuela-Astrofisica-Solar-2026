#!/usr/bin/env python3
"""exportar_datos_de_la_clase.py (copia de referencia; depende de los módulos del repositorio de origen) — Export the light data files for the Escuela de Astrofisica Solar 2026 class.

Everything the students need to run the class notebook on a laptop without a GPU or PyTorch:
a raw 13-channel cutout (for the normalization), a downsampled full disk (to draw the region box),
Surya's normalization constants, the unpooled token crop of that region (to show crop and pooling),
a few pooled embeddings with their captions, and the held-out results. Surya is run once, on the
2014-01-07 18:24 UT instant, to produce the unpooled crop.

Usage:
  python scripts/export_school_data.py --out /path/to/03_Datos
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "notebook"))

from notebook_utils._paths import DATA_DIR  # noqa: E402
from notebook_utils.model import SuryaModel  # noqa: E402
from notebook_utils.surya_input import SuryaInput, find_file  # noqa: E402
from notebook_utils.tokens import crop_tokens  # noqa: E402

INSTANT = datetime(2014, 1, 7, 18, 24)
REGION = "20140107_1824_AR11944"
TRAIN_IDS = ["20140107_1800_AR11944", "20140107_1824_AR11944", "20140107_1824_AR11943", "20140107_1824_AR11945"]
HELDOUT_DAYS = ["20120307", "20121109", "20131109", "20141024"]
HELDOUT_JAN7 = 2  # how many 7 January held-out regions to include
DOWNSAMPLE = 8


def read_jsonl(path: Path) -> list[dict]:
    """Read a JSONL file into a list of dicts."""
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def block_mean(image: np.ndarray, factor: int) -> np.ndarray:
    """Downsample a square image by averaging non-overlapping factor x factor blocks."""
    n = image.shape[0] // factor
    return image[: n * factor, : n * factor].reshape(n, factor, n, factor).mean(axis=(1, 3))


def main() -> None:
    """Write all the files of the class dataset."""
    parser = argparse.ArgumentParser(description="Export light data for the school class.")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    config = yaml.safe_load((DATA_DIR / "Surya-1.0" / "config.yaml").read_text())
    reader = SuryaInput(config, DATA_DIR / "Surya-1.0" / "scalers.yaml")
    roots = [DATA_DIR / "Surya-1.0_validation_data"]
    events = __import__("pandas").read_csv(DATA_DIR / "events_20140107.csv")
    row = events[(events.instant == "2014-01-07 18:24:00") & (events.noaa == 11944)].iloc[0]
    x0, y0, x1, y1 = (int(row.x_min), int(row.y_min), int(row.x_max), int(row.y_max))

    # 1. Raw cutout (all 13 channels), full-disk downsample and per-channel statistics of the full image.
    import hdf5plugin  # noqa: F401
    import xarray as xr
    with xr.open_dataset(find_file(INSTANT, roots), engine="h5netcdf", chunks=None, cache=False) as ds:
        raw = ds[reader.channels].to_array().load().to_numpy().astype(np.float32)  # (13, 4096, 4096)
    normalized = reader.load_normalized(find_file(INSTANT, roots))
    np.savez_compressed(
        args.out / "recorte_AR11944_20140107_1824.npz",
        raw=raw[:, y0:y1, x0:x1], channels=np.array(reader.channels), bbox_px=np.array([x0, y0, x1, y1]),
    )
    ch = reader.channels
    np.savez_compressed(
        args.out / "disco_completo_512.npz",
        aia131=block_mean(raw[ch.index("aia131")], DOWNSAMPLE), aia304=block_mean(raw[ch.index("aia304")], DOWNSAMPLE),
        hmi_m=block_mean(raw[ch.index("hmi_m")], DOWNSAMPLE), downsample=DOWNSAMPLE, bbox_px=np.array([x0, y0, x1, y1]),
    )
    constants = {
        c: {
            "mean": float(reader.means[i]), "std": float(reader.stds[i]), "epsilon": float(reader.epsilons[i]),
            "sl_scale_factor": float(reader.scale_factors[i]),
            "full_disk_raw": {"min": float(raw[i].min()), "max": float(raw[i].max())},
            "full_disk_normalized": {"min": float(normalized[i].min()), "max": float(normalized[i].max()),
                                     "mean": float(normalized[i].mean()), "std": float(normalized[i].std())},
        }
        for i, c in enumerate(ch)
    }
    (args.out / "normalizacion_constantes.json").write_text(json.dumps(
        {"instant": INSTANT.isoformat(), "channels": ch, "constants": constants}, indent=1))
    del raw, normalized

    # 2. Unpooled token crop of the region, from one Surya forward pass.
    surya = SuryaModel.load(config=config)
    tokens = surya.embed_batch(reader.load_pair(INSTANT, roots))  # (1, 65536, 1280)
    crop = crop_tokens(tokens, (x0, y0, x1, y1))[0].to(torch.float16).cpu().numpy()  # (h, w, 1280)
    np.save(args.out / "tokens_recorte_AR11944_20140107_1824.npy", crop)
    print("crop tokens:", crop.shape, flush=True)

    # 3. Pooled embeddings of a few samples, with their captions.
    train = {r["id"]: r for r in read_jsonl(REPO / "data/cache/manifest.jsonl")}
    held = read_jsonl(REPO / "data/cache/manifest_heldout.jsonl")
    generated = {r["id"]: r for r in read_jsonl(REPO / "runs/prototype/captions_heldout.jsonl")}
    chosen_held = [next(r["id"] for r in held if r["id"].startswith(d)) for d in HELDOUT_DAYS]
    chosen_held += [r["id"] for r in held if r["id"].startswith("20140107")][:HELDOUT_JAN7]
    ids = TRAIN_IDS + chosen_held
    records = [train.get(i) or next(r for r in held if r["id"] == i) for i in ids]
    embeddings = np.stack([torch.load(REPO / "data/cache" / r["embedding_path"]).numpy() for r in records])
    np.savez_compressed(args.out / "embeddings_ejemplo.npz", ids=np.array(ids), embeddings=embeddings.astype(np.float16))
    (args.out / "captions_ejemplo.json").write_text(json.dumps([
        {"id": r["id"], "split": "train" if r["id"] in train else "held_out", "reference": r["caption"],
         "generated": generated.get(r["id"], {}).get("generated")} for r in records
    ], indent=1, ensure_ascii=False))

    # 4. Held-out results (all 55) and the sequence layout fixture.
    (args.out / "resultados_heldout.json").write_text(json.dumps(
        [{"id": g["id"], "reference": g["reference"], "generated": g["generated"]} for g in generated.values()],
        indent=1, ensure_ascii=False))
    shutil.copy(REPO / "docs/fixtures/section10_sequence_fixture.json", args.out / "secuencia_ejemplo.json")
    print("done ->", args.out, flush=True)


if __name__ == "__main__":
    main()
