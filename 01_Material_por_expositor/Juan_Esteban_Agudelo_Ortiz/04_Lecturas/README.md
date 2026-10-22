# Lecturas recomendadas

Los artículos no se incluyen en el repositorio por derechos de autor; aquí van los enlaces. Están ordenados para leer de lo general a lo específico.

## Surya y los datos de SDO

- Roy, S. et al. (2025). *Surya: Foundation Model for Heliophysics.* [arXiv:2508.14112](https://arxiv.org/abs/2508.14112). El modelo fundacional que usamos como codificador visual (366 millones de parámetros, 13 canales de SDO, 2 instantes).

## Modelos de visión y lenguaje: los fundamentos

- Dosovitskiy, A. et al. (2020). *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale.* [arXiv:2010.11929](https://arxiv.org/abs/2010.11929). De dónde viene la idea de "un token por parche".
- Radford, A. et al. (2021). *Learning Transferable Visual Models From Natural Language Supervision (CLIP).* [arXiv:2103.00020](https://arxiv.org/abs/2103.00020).
- Liu, H. et al. (2023). *Visual Instruction Tuning (LLaVA).* [arXiv:2304.08485](https://arxiv.org/abs/2304.08485). La receta de proyector entre un codificador visual y un modelo de lenguaje que seguimos.
- Liu, H. et al. (2024). *Improved Baselines with Visual Instruction Tuning (LLaVA-1.5).* [arXiv:2310.03744](https://arxiv.org/abs/2310.03744). Proyector de dos capas con GELU.
- Zhang, J. et al. (2024). *Vision-Language Models for Vision Tasks: A Survey.* IEEE TPAMI 46(8). Una visión de conjunto del campo.

## Modelos de visión y lenguaje para teledetección (ciencias de la Tierra)

- Kuckreja, K. et al. (2024). *GeoChat: Grounded Large Vision-Language Model for Remote Sensing.*
- Hu, Y. et al. (2023). *RSGPT: A Remote Sensing Vision Language Model and Benchmark.* [arXiv:2307.15266](https://arxiv.org/abs/2307.15266).
- Irvin, J. A. et al. (2025). *TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data.* ICLR 2025, [arXiv:2410.06234](https://arxiv.org/abs/2410.06234). Un asistente para secuencias de imágenes en el tiempo.
- Mall, U. et al. (2024). *Remote Sensing Vision-Language Foundation Models without Annotations via Ground Remote Alignment.* ICLR 2024, [arXiv:2312.06960](https://arxiv.org/abs/2312.06960). Cómo entrenar sin textos escritos a mano.
- Li, X. et al. (2024). *Vision-Language Models in Remote Sensing: Current Progress and Future Trends.* IEEE GRSM 12(2), 32–66.

## Física solar y astronomía

- Shao, M. et al. (2026). *JW-VL: A Vision-Language Model for Solar Physics.* [arXiv:2603.28504](https://arxiv.org/abs/2603.28504). Hasta donde sabemos, el trabajo más directo sobre un modelo de visión y lenguaje para física solar; trabaja con imágenes renderizadas, no con los datos físicos.
- Zaman, S. et al. (2025). *AstroLLaVA: towards the unification of astronomical data and natural language.* [arXiv:2504.08583](https://arxiv.org/abs/2504.08583).
- Baek, J.-H. et al. (2024). *Deep learning-based solar image captioning.* Advances in Space Research 73(6), 3270–3281, [doi:10.1016/j.asr.2023.12.066](https://doi.org/10.1016/j.asr.2023.12.066). Conjunto de descripciones de imágenes de SDO (DeepSDO).

## Datos

- Conjunto público de Surya (sin credenciales): `s3://nasa-surya-bench`, archivos `AAAA/MM/AAAAMMDD_HHMM.nc`.
