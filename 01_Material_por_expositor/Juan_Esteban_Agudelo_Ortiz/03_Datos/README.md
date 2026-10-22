# Datos de la sesión de Juan Esteban Agudelo Ortiz

Archivos livianos (unos 36 MB en total) que usa el cuaderno `../02_Notebooks/01_Del_dato_solar_al_caption.ipynb`. Se leen con NumPy y `json`; **no hace falta GPU ni PyTorch**.

| Archivo | Qué contiene | Forma / formato |
|---|---|---|
| `recorte_AR11944_20140107_1824.npz` | Recorte de 704 × 704 píxeles alrededor de la región activa NOAA 11944, los 13 canales de Surya **sin normalizar** (`raw`), los nombres de los canales (`channels`) y la caja en píxeles de la imagen de 4096 × 4096 (`bbox_px`) | `raw`: (13, 704, 704), `float32` |
| `disco_completo_512.npz` | Disco completo reducido 8 veces (promedio de bloques) en `aia131`, `aia304` y `hmi_m`, para dibujar la caja de la región | 3 arreglos de (512, 512) |
| `normalizacion_constantes.json` | Media, desviación, `epsilon` y factor de escala de cada canal (de `scalers.yaml`, el archivo que acompaña a Surya), más el mínimo, máximo, media y desviación de la imagen completa, antes y después de normalizar | JSON |
| `tokens_recorte_AR11944_20140107_1824.npy` | Tokens de Surya de esa región, **antes del pooling**: una celda de 16 × 16 píxeles por token | (45, 45, 1280), `float16` |
| `embeddings_ejemplo.npz` | Diez regiones con sus 256 tokens ya reducidos (`embeddings`) y sus identificadores (`ids`) | (10, 256, 1280), `float16` |
| `captions_ejemplo.json` | Esas diez regiones con su caption de referencia y, para las apartadas del entrenamiento, el caption que generó el modelo | JSON |
| `resultados_heldout.json` | Las 55 regiones apartadas del entrenamiento: referencia y caption generado | JSON |
| `secuencia_ejemplo.json` | Descripción de la secuencia que recibe el modelo de lenguaje para dos captions de prueba (posiciones de la imagen, de la pérdida, etc.) | JSON |

## De dónde salen

- **Observaciones:** archivos de nivel 1.5 en el formato de Surya (SDO/AIA y SDO/HMI), del conjunto de datos público `s3://nasa-surya-bench` (sin credenciales). Instante: 7 de enero de 2014, 18:24 UT.
- **Posición de la región y captions de referencia:** reportes de regiones activas de NOAA SWPC, consultados a través de HEK. Los textos se arman con una plantilla fija a partir de la ubicación, el número de manchas y las clases de McIntosh y de Mount Wilson (sin intervención de un modelo de lenguaje).
- **Tokens y captions generados:** salida de Surya (congelado) y del proyector entrenado con el modelo de lenguaje Qwen3-8B (congelado). Se calcularon antes de la sesión en una GPU.

## Cómo se generaron

El script `scripts/export_school_data.py` del repositorio `vision-language-model-surya` (github.com/juagudeloo) produce estos archivos. Requiere los archivos de Surya (600 MB cada uno), una GPU y PyTorch; los estudiantes **no** necesitan ejecutarlo.

## Límites a tener en cuenta

Son datos de muestra para la clase. Las 55 regiones apartadas corresponden a pocos días y, en el caso del 7 de enero de 2014, a solo dos regiones observadas 18 veces. No son un conjunto de evaluación general.
