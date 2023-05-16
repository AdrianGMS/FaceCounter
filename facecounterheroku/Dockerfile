From python:3.11

# Establecer el directorio de trabajo
WORKDIR /facecounterheroku

# Copiar los archivos necesarios
COPY main.py .
COPY Procfile .
COPY requirements.txt .
COPY runtime.txt .


# Instalar las dependencias
RUN apt-get update
RUN pip install cmake
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install -y libgl1-mesa-glx


# Exponer el puerto 5000
# EXPOSE 5000

# Definir el comando de inicio
ENTRYPOINT [ "python" ]
CMD ["main.py"]