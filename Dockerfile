# Usar la imagen base de Python 3.9
FROM python:3.9

# Crear y establecer el directorio de trabajo
RUN mkdir /work
WORKDIR /work

# Copiar solo los archivos necesarios primero para aprovechar la caché
COPY requirements.txt requirements.txt

# Actualizar pip e instalar dependencias en una sola capa
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install apache-beam[interactive]==2.47.0 && \
    pip install jupyter==1.0.0 -U && \
    pip install jupyterlab==3.6.1

# Ahora copiamos el resto del código
COPY . .

# Exponer el puerto de Jupyter
EXPOSE 8888

# Iniciar JupyterLab
ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]