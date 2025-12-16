FROM python:3.10-slim-buster

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copier seulement requirements d’abord pour profiter du cache Docker
COPY requirements.txt .

# Installer les packages Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Commande pour lancer Flask
CMD ["python3", "app.py"]
