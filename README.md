# AI Agent Éducatif - POO + Streamlit 🎓

Projet de démonstration de Programmation Orientée Objet avec interface Streamlit pour manipuler un agent IA éducatif. Classes Python simples + interface moderne pour la gestion d'un système éducatif.

## 🎯 Objectif du Projet

- **Enseigner la POO** avec des classes Python simples et compréhensibles
- **Interface utilisateur** moderne avec Streamlit pour manipuler les données
- **Agent IA éducatif** pour interagir avec le système (professeurs, étudiants, cours)
- **Stockage JSON** simple pour la persistance des données

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   AI Agent      │
│   Interface     │◄───┤   (Logic)       │
└─────────────────┘    └─────────────────┘
                                │
                       ┌─────────────────┐
                       │   Classes POO   │
                       │   (Entities)    │
                       └─────────────────┘
                                │
                       ┌─────────────────┐
                       │   JSON Files    │
                       │   (Storage)     │
                       └─────────────────┘
```

## 📁 Structure du Projet

```
ai-agent-educatif/
├── 📄 README.md                    # Documentation du projet
├── 📄 pyproject.toml               # Configuration Poetry
├── 📄 Dockerfile                   # Image Docker
├── 📄 test_prof.py                 # Tests professeurs
├── 📄 test_simple.py               # Tests simples
│
├── 📁 entities/                    # 🏗️ Classes POO (Simples)
│   ├── 📄 __init__.py
│   ├── 📄 professeur.py            # 👨‍🏫 Classe Professeur
│   ├── 📄 etudiant.py              # 👨‍🎓 Classe Etudiant
│   ├── 📄 cours.py                 # 📚 Classe Cours
│   ├── 📄 evaluation.py            # 📝 Classe Evaluation
│   ├── 📄 note.py                  # 📊 Classe Note
│   └── 📄 review.py                # ⭐ Classe Review
│
├── 📁 streamlit_app/               # 🖥️ Interface Streamlit
│   ├── 📄 __init__.py
│   ├── 📄 main.py                  # Application principale
│   └── 📁 pages/                   # Pages de l'interface
│       ├── 📄 __init__.py
│       ├── 📄 ai_agent.py          # Interface agent IA
│       └── 📄 documentation.py     # Documentation
│
├── 📁 ai_agent/                    # 🤖 Agent IA Modulaire
│   ├── 📄 __init__.py
│   ├── 📄 agent.py                 # Point d'entrée (export)
│   ├── 📁 core/                    # 🧠 Logique centrale
│   │   ├── 📄 __init__.py
│   │   └── 📄 agent_core.py        # Classe principale + process_query
│   ├── 📁 actions/                 # ⚡ Gestionnaires d'actions
│   │   ├── 📄 __init__.py
│   │   ├── 📄 entity_creators.py   # Création entités (178 lignes)
│   │   └── 📄 data_retrievers.py   # Récupération données (155 lignes)
│   └── 📁 utils/                   # 🔧 Utilitaires
│       ├── 📄 __init__.py
│       └── 📄 action_processor.py  # Traitement actions JSON (71 lignes)
│
├── 📁 data_manager/                # 💾 Gestion des données JSON
│   ├── 📄 __init__.py
│   ├── 📄 json_handler.py          # Gestionnaire JSON
│   ├── 📄 data_loader.py           # Chargement des données
│   └── 📄 data_saver.py            # Sauvegarde des données
│
├── 📁 api/                         # 🌐 API REST (Optionnelle)
│   ├── 📄 __init__.py
│   ├── 📄 main.py                  # Serveur FastAPI
│   ├── 📄 routes.py                # Routes API
│   └── 📄 stats.py                 # Statistiques
│
└── 📁 data/                        # 📁 Fichiers de données JSON
    ├── 📄 professeurs.json         # Données professeurs
    ├── 📄 etudiants.json           # Données étudiants
    ├── 📄 cours.json               # Données cours
    ├── 📄 evaluations.json         # Données évaluations
    ├── 📄 notes.json               # Données notes
    └── 📄 reviews.json             # Données reviews
```

## 🏛️ Architecture Détaillée

### **1. Couche Entities (POO Pure)**
```python
# entities/professeur.py
class Professeur:
    def __init__(self, nom, email, specialite):
        self.id = None
        self.nom = nom
        self.email = email
        self.specialite = specialite
        self.cours = []
    
    def ajouter_cours(self, cours):
        self.cours.append(cours)
    
    def __str__(self):
        return f"Prof. {self.nom} ({self.specialite})"
```

**Caractéristiques :**
- Classes Python **pures** et simples
- Pas de frameworks complexes
- Relations entre objets claires
- Parfait pour enseigner la POO

### **2. Couche Data Manager (JSON)**
```python
# data_manager/json_handler.py
import json
from typing import List
from entities.professeur import Professeur

class JSONHandler:
    def __init__(self, data_path="data/"):
        self.data_path = data_path
    
    def load_professeurs(self) -> List[Professeur]:
        """Charge les professeurs depuis JSON et les convertit en objets"""
        with open(f"{self.data_path}/professeurs.json", "r") as f:
            data = json.load(f)
        
        return [Professeur(**prof_data) for prof_data in data]
    
    def save_professeurs(self, professeurs: List[Professeur]):
        """Sauvegarde les objets Professeur en JSON"""
        data = [prof.__dict__ for prof in professeurs]
        with open(f"{self.data_path}/professeurs.json", "w") as f:
            json.dump(data, f, indent=2)
```

**Responsabilités :**
- Chargement/sauvegarde JSON ↔ Objets Python **avec json natif**
- Gestion des IDs auto-générés
- **Aucune dépendance externe** pour les données

### **3. Couche AI Agent (Intelligence) - Architecture Modulaire**

Après refactorisation, l'agent IA est maintenant divisé en 4 modules spécialisés :

#### **🧠 Core - Logique Centrale (98 lignes)**
```python
# ai_agent/core/agent_core.py
class EducationalAgent:
    def __init__(self):
        from ..utils.action_processor import ActionProcessor
        self.action_processor = ActionProcessor()
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
    def process_query(self, query: str) -> str:
        """Traite une requête utilisateur via OpenAI"""
        system_prompt = self._create_system_prompt()
        current_data = self._get_current_data()
        
        # Interaction avec OpenAI GPT-3.5
        response = self.client.chat.completions.create(...)
        ai_response = response.choices[0].message.content
        
        # Traitement des actions JSON
        return self.action_processor.execute_actions(ai_response)
```

#### **⚡ Actions - Gestionnaires Spécialisés**

**Création d'entités (178 lignes) :**
```python
# ai_agent/actions/entity_creators.py
class EntityCreators:
    def create_professeur(self, data: dict) -> str:
        """Crée un professeur avec validation et ID auto-généré"""
        
    def create_etudiant(self, data: dict) -> str:
        """Crée un étudiant avec numéro auto-généré"""
        
    def create_cours(self, data: dict) -> str:
        """Crée un cours lié à un professeur"""
        
    # + create_evaluation, create_note, create_review
```

**Récupération de données (155 lignes) :**
```python
# ai_agent/actions/data_retrievers.py
class DataRetrievers:
    def get_etudiants(self, data: dict) -> str:
        """Récupère et formate la liste des étudiants"""
        
    def get_professeurs(self, data: dict) -> str:
        """Récupère et formate la liste des professeurs"""
        
    def get_stats(self, data: dict) -> str:
        """Calcule les statistiques du système"""
        
    # + get_cours, get_notes, get_reviews, get_evaluations
```

#### **🔧 Utils - Traitement des Actions (71 lignes)**
```python
# ai_agent/utils/action_processor.py
class ActionProcessor:
    def __init__(self):
        self.entity_creators = EntityCreators()
        self.data_retrievers = DataRetrievers()
        
    def execute_actions(self, response_text: str) -> str:
        """Détecte les patterns JSON et route vers le bon handler"""
        
    def _handle_json_action(self, response_text, action_type, handler_func):
        """Parse le JSON et exécute l'action correspondante"""
```

#### **📤 Point d'entrée (4 lignes)**
```python
# ai_agent/agent.py
from .core.agent_core import EducationalAgent
__all__ = ['EducationalAgent']  # Export pour compatibilité
```

**Avantages de cette architecture modulaire :**
- ✅ **Séparation des responsabilités** : Chaque module a un rôle précis
- ✅ **Maintenabilité** : Plus facile de modifier ou étendre chaque partie
- ✅ **Lisibilité** : Code organisé en petits fichiers (~100 lignes)
- ✅ **Réutilisabilité** : Les modules peuvent être importés séparément
- ✅ **Testabilité** : Chaque module peut être testé indépendamment

### **4. Couche Streamlit (Interface)**
```python
# streamlit_app/main.py
import streamlit as st
from ai_agent.agent import EducationalAgent

def main():
    st.title("🎓 Agent IA Éducatif")
    
    # Interface simplifiée avec l'agent IA modulaire
    agent = EducationalAgent()
    
    # Chat avec l'agent
    if query := st.text_input("Posez votre question à l'agent IA :"):
        response = agent.process_query(query)
        st.write(response)
```

**Pages disponibles :**
- **Agent IA** (`pages/ai_agent.py`) : Interface de chat avec l'agent intelligent
- **Documentation** (`pages/documentation.py`) : Guide d'utilisation

### **5. Couche API (Optionnelle)**
```python
# api/main.py
from fastapi import FastAPI
from ai_agent.agent import EducationalAgent

app = FastAPI(title="AI Agent Éducatif API")
agent = EducationalAgent()

@app.post("/query")
async def process_query(query: str):
    """Endpoint pour interagir avec l'agent IA"""
    return {"response": agent.process_query(query)}
```

**Endpoints disponibles :**
- **POST /query** : Interaction avec l'agent IA
- **GET /stats** : Statistiques du système
- Routes CRUD pour chaque entité

## 🔧 Configuration

### **pyproject.toml**
```toml
[tool.poetry]
name = "ai-agent-educatif"
version = "0.1.0"
description = "Agent IA éducatif avec démonstration POO et architecture modulaire"

[tool.poetry.dependencies]
python = "^3.11"
streamlit = "^1.28.0"
openai = "^1.0.0"        # Agent IA avec GPT-3.5
python-dotenv = "^1.0.0" # Variables d'environnement
fastapi = "^0.104.0"     # API REST (optionnelle)
uvicorn = "^0.24.0"      # Serveur ASGI (optionnelle)
```

### **Dockerfile**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🚀 Utilisation

### **Configuration Requise**
```bash
# Variables d'environnement (.env)
OPENAI_API_KEY=your_openai_api_key_here
```

### **Développement Local**
```bash
# Installation
poetry install

# Configuration
cp .env.example .env  # Ajouter votre clé OpenAI

# Lancer Streamlit
poetry run streamlit run streamlit_app/main.py

# Ou lancer l'API (optionnel)
poetry run uvicorn api.main:app --reload
```

### **Avec Docker**
```bash
# Build
docker build -t ai-agent-educatif .

# Run avec variables d'environnement
docker run -p 8501:8501 -v $(pwd)/data:/app/data \
  -e OPENAI_API_KEY=your_key ai-agent-educatif
```

### **Accès**
- **Interface Streamlit** : http://localhost:8501
- **API REST** : http://localhost:8000 (optionnelle)
- **Documentation API** : http://localhost:8000/docs

## 🎓 Avantages Pédagogiques

### **Pour l'Enseignement POO :**
- ✅ Classes Python **simples** dans `entities/`
- ✅ Relations entre objets **claires**
- ✅ Code **lisible** et **compréhensible**
- ✅ Architecture **modulaire** facile à comprendre

### **Pour l'Architecture Logicielle :**
- ✅ **Séparation des couches** : Entities → Data Manager → AI Agent → Interface
- ✅ **Modularité** : Agent IA divisé en 4 modules spécialisés
- ✅ **Responsabilités claires** : Chaque module a un rôle précis
- ✅ **Maintenabilité** : Code organisé en petits fichiers (~100 lignes)

### **Pour l'Interface Moderne :**
- ✅ **Streamlit** pour interface utilisateur intuitive
- ✅ **Agent IA** avec GPT-3.5 pour interactions intelligentes
- ✅ **API REST** optionnelle pour intégrations
- ✅ **Expérience utilisateur** moderne

### **Pour la Persistance :**
- ✅ **JSON** simple et lisible
- ✅ Pas de complexité de base de données
- ✅ **Portable** et facile à comprendre
- ✅ **Versionnable** avec Git

## 📊 Métriques du Projet

**Avant refactorisation :**
- `ai_agent/agent.py` : **529 lignes** (difficile à maintenir)

**Après refactorisation :**
- `core/agent_core.py` : **98 lignes** (logique centrale)
- `actions/entity_creators.py` : **178 lignes** (création d'entités)
- `actions/data_retrievers.py` : **155 lignes** (récupération de données)
- `utils/action_processor.py` : **71 lignes** (traitement JSON)
- `agent.py` : **4 lignes** (point d'entrée)

**Résultat :** Code **modulaire**, **maintenable** et **extensible** ! 🚀

Cette architecture permet d'**enseigner la POO** et les **bonnes pratiques de développement** avec une **interface moderne** et une **IA intégrée** !