# Fase 1: Build del sitio Hugo
FROM klakegg/hugo:0.92.2-ext AS build

WORKDIR /app

# Copiamos los archivos de Hugo
COPY . .

# Construimos el sitio Hugo
RUN hugo --minify || { echo "Hugo build failed!"; exit 1; }

# Fase 2: Configuración del servidor Flask para IA
FROM python:3.9-slim

WORKDIR /app

# Instalamos dependencias del sistema para Python y Rust
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalamos dependencias de Python y Hugging Face
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiamos el sitio Hugo estático y los scripts de IA
COPY --from=build /app/public /app/public
COPY ./agents /app/agents
COPY ./scripts /app/scripts

# Definimos el puerto y el punto de entrada del servidor Flask
EXPOSE 5000
CMD ["python", "scripts/server.py"]
