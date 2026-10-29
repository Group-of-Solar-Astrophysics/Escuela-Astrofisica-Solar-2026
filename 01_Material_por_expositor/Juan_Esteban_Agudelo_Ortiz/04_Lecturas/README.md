# Lecturas recomendadas

Los artículos no se incluyen en el repositorio por derechos de autor; aquí van los enlaces. Están ordenados para leer de lo general a lo específico.

## Aprendizaje automático en física solar

- Asensio Ramos, A., Cheung, M. C. M., Chifu, I. y Gafeira, R. (2023). *Machine learning in solar physics.* Living Reviews in Solar Physics 20, 4, [doi:10.1007/s41116-023-00038-x](https://doi.org/10.1007/s41116-023-00038-x), [arXiv:2306.15308](https://arxiv.org/abs/2306.15308). La revisión de la que salen los ejemplos de la sesión: segmentación, superresolución, inversión de Stokes, predicción de erupciones y lado lejano.
- Bobra, M. G. y Mason, J. P. (2018). *Machine Learning, Statistics, and Data Mining for Heliophysics* (HelioML), [doi:10.5281/zenodo.1412824](https://doi.org/10.5281/zenodo.1412824); versión web v0.4.0 en [helioml.org](https://helioml.org/Introduction/title.html). Nueve capítulos, cada uno con un cuaderno de Jupyter que reproduce un resultado publicado: predicción de CME con SVM, superresolución de HMI (Enhance), DEM con redes (DeepEM), regiones activas del lado lejano (FarNet), regiones fuente del viento solar sin etiquetas y más.
- Díaz Baso, C. J. y Asensio Ramos, A. (2018). *Enhancing SDO/HMI images using deep learning.* Astronomy & Astrophysics 614, A5, [doi:10.1051/0004-6361/201731344](https://doi.org/10.1051/0004-6361/201731344), [arXiv:1706.02933](https://arxiv.org/abs/1706.02933).
- Bobra, M. G. e Ilonidis, S. (2016). *Predicting Coronal Mass Ejections Using Machine Learning Methods.* The Astrophysical Journal 821, 127, [doi:10.3847/0004-637X/821/2/127](https://doi.org/10.3847/0004-637X/821/2/127), [arXiv:1603.03775](https://arxiv.org/abs/1603.03775).
- Reiss, M. A. et al. (2021). *The Observational Uncertainty of Coronal Hole Boundaries in Automated Detection Schemes.* The Astrophysical Journal 913, 28, [doi:10.3847/1538-4357/abf2c8](https://doi.org/10.3847/1538-4357/abf2c8), [arXiv:2103.14403](https://arxiv.org/abs/2103.14403). De aquí sale la figura de agujeros coronales de la sesión (fig. 8 de la revisión).

## Surya y los datos de SDO

- Roy, S. et al. (2025). *Surya: Foundation Model for Heliophysics.* [arXiv:2508.14112](https://arxiv.org/abs/2508.14112). El modelo fundacional que usamos como codificador visual (366 millones de parámetros, 13 canales de SDO, 2 instantes).

## Modelos de visión y lenguaje: los fundamentos

- Dosovitskiy, A. et al. (2020). *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale.* [arXiv:2010.11929](https://arxiv.org/abs/2010.11929). De dónde viene la idea de "un token por parche".
- Radford, A. et al. (2021). *Learning Transferable Visual Models From Natural Language Supervision (CLIP).* [arXiv:2103.00020](https://arxiv.org/abs/2103.00020).
- Liu, H. et al. (2023). *Visual Instruction Tuning (LLaVA).* [arXiv:2304.08485](https://arxiv.org/abs/2304.08485). La receta de proyector entre un codificador visual y un modelo de lenguaje que seguimos.
- Liu, H. et al. (2024). *Improved Baselines with Visual Instruction Tuning (LLaVA-1.5).* [arXiv:2310.03744](https://arxiv.org/abs/2310.03744). Proyector de dos capas con GELU.
- Zhang, J. et al. (2024). *Vision-Language Models for Vision Tasks: A Survey.* IEEE Transactions on Pattern Analysis and Machine Intelligence 46, 5625, [doi:10.1109/TPAMI.2024.3369699](https://doi.org/10.1109/TPAMI.2024.3369699). Una visión de conjunto del campo.

## Modelos de visión y lenguaje para teledetección (ciencias de la Tierra)

- Kuckreja, K. et al. (2024). *GeoChat: Grounded Large Vision-Language Model for Remote Sensing.* CVPR 2024, [doi:10.1109/CVPR52733.2024.02629](https://doi.org/10.1109/CVPR52733.2024.02629), [arXiv:2311.15826](https://arxiv.org/abs/2311.15826).
- Hu, Y. et al. (2025). *RSGPT: A remote sensing vision language model and benchmark.* ISPRS Journal of Photogrammetry and Remote Sensing 224, 272, [doi:10.1016/j.isprsjprs.2025.03.028](https://doi.org/10.1016/j.isprsjprs.2025.03.028), [arXiv:2307.15266](https://arxiv.org/abs/2307.15266).
- Irvin, J. A. et al. (2024). *TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data.* [arXiv:2410.06234](https://arxiv.org/abs/2410.06234). Un asistente para secuencias de imágenes en el tiempo.
- Mall, U. et al. (2023). *Remote Sensing Vision-Language Foundation Models without Annotations via Ground Remote Alignment.* [arXiv:2312.06960](https://arxiv.org/abs/2312.06960). Cómo entrenar sin textos escritos a mano.
- Li, X. et al. (2024). *Vision-Language Models in Remote Sensing: Current Progress and Future Trends.* IEEE Geoscience and Remote Sensing Magazine 12, 32, [doi:10.1109/MGRS.2024.3383473](https://doi.org/10.1109/MGRS.2024.3383473), [arXiv:2305.05726](https://arxiv.org/abs/2305.05726).

## Física solar y astronomía

- Shao, M. et al. (2026). *JW-VL: A Vision-language Model for Solar Physics.* Research in Astronomy and Astrophysics 26, 095007, [doi:10.1088/1674-4527/ae5a5d](https://doi.org/10.1088/1674-4527/ae5a5d), [arXiv:2603.28504](https://arxiv.org/abs/2603.28504). Hasta donde sabemos, el trabajo más directo sobre un modelo de visión y lenguaje para física solar; trabaja con imágenes renderizadas, no con los datos físicos.
- Zaman, S. et al. (2025). *AstroLLaVA: towards the unification of astronomical data and natural language.* [arXiv:2504.08583](https://arxiv.org/abs/2504.08583).
- Baek, J.-H. et al. (2024). *Deep learning-based solar image captioning.* Advances in Space Research 73, 3270, [doi:10.1016/j.asr.2023.12.066](https://doi.org/10.1016/j.asr.2023.12.066). Conjunto de descripciones de imágenes de SDO (DeepSDO).

## Datos

- Conjunto público de Surya (sin credenciales): `s3://nasa-surya-bench`, archivos `AAAA/MM/AAAAMMDD_HHMM.nc`.

