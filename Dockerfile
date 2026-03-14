# Usamos una imagen ligera de Python
FROM python:3.12-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
COPY .env .
COPY vera_app_visual.py .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto de Streamlit
EXPOSE 8501

# Comando para arrancar la App
CMD ["streamlit", "run", "vera_app_visual.py", "--server.port=8501", "--server.address=0.0.0.0"]
