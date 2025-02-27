# Proyecto MLOps: Ambiente de Desarrollo con Docker y JupyterLab

Este repositorio contiene un entorno de desarrollo para un proyecto de Machine Learning en el que se demuestran capacidades de ingesta, validación y transformación de datos, así como el versionado del código y del ambiente de desarrollo. El objetivo es proveer un entorno aislado (mediante Docker) que permita ejecutar notebooks de Jupyter, facilitando la reproducibilidad y la colaboración.

---

## Tabla de Contenido

1. [Contexto General del Proyecto](#contexto-general-del-proyecto)
2. [Arquitectura y Archivos Principales](#arquitectura-y-archivos-principales)
3. [Requisitos Previos](#requisitos-previos)
4. [Pasos para Levantar el Contenedor](#pasos-para-levantar-el-contenedor)
5. [Acceso a JupyterLab](#acceso-a-jupyterlab)
6. [Importancia del Volumen `./work:/work`](#importancia-del-volumen-workwork)
7. [Sugerencias y Notas Adicionales](#sugerencias-y-notas-adicionales)

---

## Contexto General del Proyecto

Este proyecto está enfocado en la **creación de un pipeline de datos** que incluye:

- **Selección de características** (feature selection).
- **Ingesta** y lectura de un conjunto de datos.
- **Validación** y **estadísticas** (StatisticsGen, ExampleValidator).
- **Transformación** de los datos (Transform).
- **Gestión de metadatos** de ML (ML Metadata).
- **Seguimiento de la procedencia** de los datos.
- **Versión de código y ambiente** de desarrollo (usando Git y contenedores Docker).

El dataset principal propuesto es una variante del **conjunto de datos de tipo de cubierta forestal** (Cover Type). Aun así, la estructura y componentes TFX (TensorFlow Extended) son fácilmente adaptables a otros conjuntos de datos y flujos de trabajo de ML.

---

## Arquitectura y Archivos Principales

Este proyecto forma parte del curso de MLOps y tiene como objetivo construir un entorno de desarrollo para Machine Learning utilizando Docker, Jupyter Notebook y TensorFlow Extended (TFX). Se implementan procesos de transformación y validación de datos como parte de una canalización de datos.

```bash
Proyecto/
|-- work/
|   |-- Transformacion_Datos/
|   |   |-- data/
|   |   |-- tfx_pipeline/
|   |   |   |-- census_constants.py
|   |   |   |-- census_transform.py
|   |   |-- TFT.ipynb
|   |-- Validacion_de_Datos/
|   |   |-- cubierta_forestal.csv
|   |   |-- TFDV.ipynb
|-- Docker-compose.yml
|-- Dockerfile
|-- Readme.md
|-- requirements.txt
```

En el repositorio encontrará:

- **`Dockerfile`**: Define la imagen base (Python 3.9) y las dependencias necesarias (paquetes de Python, Jupyter, TFX, etc.).
- **`docker-compose.yml`**: Archivo de configuración para orquestar y levantar el contenedor.  
  - **Servicio `jupyter`**:
    - Construye la imagen a partir del `Dockerfile`.
    - Expone el puerto `8888`.
    - Monta un volumen local `./work:/work`.
- **`requirements.txt`**: Listado de las dependencias de Python que serán instaladas en el contenedor.
- **Carpeta `work/`**: Directorio de trabajo mapeado al contenedor, donde se ubican los notebooks (`.ipynb`) y el código fuente (`.py`).

---

## Requisitos Previos

- **Docker** instalado y funcionando en tu sistema.
- **Docker Compose** instalado.  
  > Verifica con `docker -v` y `docker-compose -v` que ambas herramientas estén disponibles.

---

## Pasos para Levantar el Contenedor

1. **Clonar el repositorio** o descargarlo en tu máquina local.
   ```bash
   git clone https://github.com/JohnSanchez27/Proyecto_1_MLOps.git #HTTPS
   git clone git@github.com:JohnSanchez27/Proyecto_1_MLOps.git #SSH
   cd Proyecto_1_MLOps


2. **Construir la imagen** definida en el Dockerfile usando Docker Compose:
   ```bash
    docker-compose build

3. **Iniciar el contenedor** den segundo plano:
   ```bash
    docker-compose up -d

4. **Verificar que el contenedor esté corriendo:**
   ```bash
    docker ps

    Deberías ver un contenedor llamado desarrollo_container (o el que hayas definido en docker-compose.yml) en ejecución.

## Acceso a JupyterLab

- Una vez que el contenedor está arriba, abre tu navegador y navega a:

    http://localhost:8888

- JupyterLab solicitará un token de acceso que se mostrará en la consola de tu terminal (donde corriste docker-compose up) o en los logs del contenedor. Copia ese token y pégalo en el navegador para iniciar sesión. (Alternativamente, puedes usar la URL completa con el token que se imprime en la consola.)


## Importancia del Volumen ./work:/work

El volumen definido en docker-compose.yml:

   ```yaml
    volumes:
    - ./work:/work
```
mapea la carpeta local work/ a la carpeta /work dentro del contenedor. Esto implica:

- Persistencia: Todos los archivos creados o modificados dentro de la carpeta /work del contenedor se verán reflejados en tu carpeta local ./work.

- Colaboración: Puedes editar tu código o notebooks con tu editor local y ver los cambios reflejados de inmediato en el contenedor (y viceversa).

- Facilidad de Uso: No necesitas reconstruir la imagen para cada cambio en los notebooks o scripts.

## Sugerencias y Notas Adicionales

- **Uso de TFX y Beam**: Se incluyeron paquetes como `apache-beam[interactive]`, `tfx`, `tensorflow-data-validation`, etc. Esto permite la **ingesta, validación y transformación** de datos de forma escalable y reproducible.

- **ML Metadata**: Para rastrear artefactos y ejecuciones, TFX utiliza un backend de metadatos (por defecto `sqlite`), lo que te permite ver qué datos se han procesado y cómo se han transformado.

- **Extensión de la Funcionalidad**: Si necesitas librerías adicionales, puedes agregarlas a `requirements.txt` y reconstruir la imagen con:
  ```bash
  docker-compose build

- **Limpieza de Contenedores:**: Para detener y eliminar el contenedor y la red asociada, ejecuta:
  ```bash
  docker-compose down

Si deseas eliminar también las imágenes construidas:
  ```bash
  docker-compose down --rmi all
  ```
