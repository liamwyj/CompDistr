# Imagen base con Python
FROM python:latest

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todos los archivos del directorio actual al contenedor
COPY . /app/

# Instala las dependencias del sistema necesarias para SQLite
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Actualiza pip antes de instalar dependencias
RUN python -m pip install --upgrade pip

# Instala las dependencias de Python especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el script de configuración de la base de datos
RUN python /app/database/setup_db.py  # Configura la base de datos

# Expone el puerto en el que el servidor WSGI (Gunicorn) escuchará
EXPOSE 9000

# Gunicorn para ejecutar la aplicación Flask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:9000", "app:app"]
