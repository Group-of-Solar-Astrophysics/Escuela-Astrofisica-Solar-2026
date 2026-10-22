# Recursos adicionales

- `soluciones_ejercicios.ipynb`: soluciones de los cuatro ejercicios del cuaderno de la sesión. Corre con el mismo entorno `escuela-solar` y lee los datos de `../03_Datos`.
- `exportar_datos_de_la_clase.py`: copia de referencia del script que generó los archivos de `../03_Datos`. **No hace falta ejecutarlo**: necesita los archivos de Surya (600 MB cada uno), una GPU, PyTorch y módulos del repositorio de origen (`vision-language-model-surya`), que no están en este repositorio. Se incluye para que se vea exactamente cómo se obtuvo cada archivo.

## Para ir más allá (opcional, requiere GPU)

Todo lo que el cuaderno carga ya viene calculado. Para repetir el proceso desde los datos de Surya hace falta:

1. Una GPU con 8 a 10 GB libres para correr Surya sobre un instante (el modelo tiene 366 millones de parámetros).
2. Los archivos de Surya del instante deseado, del conjunto público `s3://nasa-surya-bench` (`AAAA/MM/AAAAMMDD_HHMM.nc`, sin credenciales; hacen falta el instante y el de 60 minutos antes).
3. PyTorch. Recuerden que la guía de instalación pide **no** instalar paquetes de aprendizaje profundo hasta recibir indicaciones del expositor: esta parte no forma parte de la sesión.
