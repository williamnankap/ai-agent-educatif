FROM python:3.11-slim

WORKDIR /app

# Installer Poetry
RUN pip install poetry

# Copier les fichiers de configuration
COPY pyproject.toml poetry.lock* ./

# Configurer Poetry et installer les dépendances
RUN poetry config virtualenvs.create false
RUN poetry install --without dev --no-root

# Copier le code source
COPY . .

# Créer le dossier data s'il n'existe pas
RUN mkdir -p data

# Exposer les ports Streamlit et FastAPI
EXPOSE 8501 8000

# Variables d'environnement
ENV PYTHONPATH=/app
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Commande par défaut : Streamlit
CMD ["streamlit", "run", "streamlit_app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]