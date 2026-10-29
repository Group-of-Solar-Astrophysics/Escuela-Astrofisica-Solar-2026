"""Cut the 704 x 704 px region of each class example (aia131 and hmi_m) from the Surya .nc files and
save them, 2x block-averaged, as one light npz for the class notebook.

Usage: python exportar_imagenes_regiones.py OUT.npz DATA_DIR
DATA_DIR holds the events*.csv catalogues, Surya-1.0_validation_data/ and surya_events/ (the .nc files of
each instant). The students do not need to run it.
"""
import glob
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import hdf5plugin  # noqa: F401
import xarray as xr

OUT = Path(sys.argv[1])
DATA = Path(sys.argv[2])
IDS = ["20140107_1800_AR11944", "20140107_1824_AR11944", "20140107_1824_AR11943", "20140107_1824_AR11945",
       "20120307_0024_AR11430", "20121109_1200_AR11609", "20131109_1200_AR11892", "20141024_2136_AR12193",
       "20140107_1600_AR11942", "20140107_1600_AR11946"]
events = pd.concat([pd.read_csv(f) for f in glob.glob(str(DATA / "events*.csv"))], ignore_index=True).drop_duplicates("sample_id")
CH = ["aia131", "hmi_m"]


def find(stamp: str) -> Path:
    for root in (DATA / "Surya-1.0_validation_data", DATA / "surya_events"):
        hits = list(root.rglob(f"{stamp}.nc"))
        if hits:
            return hits[0]
    raise FileNotFoundError(stamp)


def block2(a):
    n = a.shape[0] // 2
    return a[: 2 * n, : 2 * n].reshape(n, 2, n, 2).mean(axis=(1, 3))


out = {"ids": np.array(IDS), "channels": np.array(CH)}
imgs = []
for sid in IDS:
    row = events[events.sample_id == sid].iloc[0]
    x0, y0, x1, y1 = (int(row.x_min), int(row.y_min), int(row.x_max), int(row.y_max))
    stamp = "_".join(sid.split("_")[:2])
    with xr.open_dataset(find(stamp), engine="h5netcdf", chunks=None, cache=False) as ds:
        arr = ds[CH].to_array().load().to_numpy().astype(np.float32)
    arr = arr.squeeze()
    assert arr.shape[-2:] == (4096, 4096), arr.shape
    imgs.append(np.stack([block2(arr[k, y0:y1, x0:x1]) for k in range(len(CH))]))
    print(sid, (x0, y0, x1, y1), imgs[-1].shape, flush=True)
out["images"] = np.stack(imgs).astype(np.float16)
np.savez_compressed(OUT, **out)
print("saved", OUT, OUT.stat().st_size / 1e6, "MB")
