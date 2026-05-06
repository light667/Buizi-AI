# ⚡ Quick Start Commands

Commandes essentielles pour démarrer MarketAI rapidement.

## 🚀 Setup Initial (First Time)

```bash
# 1. Cloner le repo
git clone https://github.com/light667/Buizi-AI.git
cd Buizi-AI

# 2. Créer environnement virtuel
python -m venv venv

# 3. Activer l'environnement (Windows)
.\venv\Scripts\Activate.ps1

# 4. Installer dépendances
pip install -r requirements.txt

# 5. Configurer les variables d'env
cp .env.example .env
# Éditer .env avec vos clés API

# 6. Vérifier l'installation
python -c "import langchain; print('✅ Setup OK')"
```

---

## 📦 Gestion des Dépendances

```bash
# Lister packages installés
pip list

# Ajouter un nouveau package
pip install package_name
pip freeze > requirements.txt  # Mettre à jour requirements.txt

# Mettre à jour pip
python -m pip install --upgrade pip

# Installer en mode développement
pip install -e .
```

---

## 🔧 Backend (FastAPI)

```bash
# Lancer le serveur de développement
cd backend
uvicorn main:app --reload

# Accès : http://localhost:8000
# Docs API : http://localhost:8000/docs

# Lancer avec logs verbeux
uvicorn main:app --reload --log-level debug

# Écouter sur un port différent
uvicorn main:app --reload --port 8001
```

---

## 🎨 Frontend (Next.js)

```bash
# Installer dépendances (depuis /frontend)
npm install

# Lancer développement
npm run dev

# Accès : http://localhost:3000

# Build production
npm run build

# Lancer en production
npm start
```

---

## 📊 RAG & Données

```bash
# Classifier articles
python scripts/classify_articles.py

# Ingérer dans ChromaDB
python scripts/ingest_rag.py

# Tester RAG retrieval
python scripts/test_rag.py

# Tester agent
python scripts/test_agent.py
```

---

## 🧪 Testing

```bash
# Lancer tous les tests
pytest

# Tests avec couverture de code
pytest --cov=backend

# Un test spécifique
pytest backend/tests/test_rag.py

# Mode verbose
pytest -v

# Mode watch (relancer à chaque changement)
pytest-watch
```

---

## 🎨 Code Quality

```bash
# Format code avec Black
black backend/ frontend/

# Vérifier style avec Flake8
flake8 backend/

# Checker types Python
mypy backend/

# Tout d'un coup
black . && flake8 . && mypy .
```

---

## 🐛 Debugging

```bash
# Python REPL interactif
python

# Tester un import spécifique
python -c "from backend.rag import retriever; print('OK')"

# Lancer un script avec debug
python -m pdb scripts/test_rag.py

# Voir variables d'env
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.environ['GROQ_API_KEY'])"
```

---

## 📚 Documentation

```bash
# Voir aide d'une commande
python --help
pip --help
uvicorn --help

# Lancer les docs localement
# (nécessite mkdocs)
pip install mkdocs
mkdocs serve
```

---

## 🔄 Git Workflow

```bash
# Voir status
git status

# Ajouter fichiers
git add .
git add backend/

# Commit
git commit -m "feat: add RAG pipeline"

# Pousser
git push origin main

# Voir historique
git log --oneline

# Créer une branche
git checkout -b feature/new-feature

# Merger une branche
git merge feature/new-feature
```

---

## 🌐 Déploiement

### Railway

```bash
# 1. Installer CLI Railway
npm i -g @railway/cli

# 2. Login
railway login

# 3. Initialiser projet
railway init

# 4. Connecter repo
# (via Railway dashboard)

# 5. Deployer
railway up
```

### Vercel (Frontend)

```bash
# 1. Installer CLI Vercel
npm i -g vercel

# 2. Login
vercel login

# 3. Deployer
vercel
```

---

## 🚨 Troubleshooting Rapide

```bash
# L'environnement n'est pas activé
# Solution : vérifier que (venv) apparaît dans l'invite
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # Mac/Linux

# ModuleNotFoundError
# Solution : réinstaller dépendances
pip install -r requirements.txt

# Port déjà utilisé (8000, 3000)
# Solution : tuer le processus
lsof -i :8000      # Voir ce qui utilise le port
kill -9 <PID>      # Tuer le processus

# Clé API manquante
# Solution : créer .env depuis .env.example
cp .env.example .env
# Éditer avec vos clés

# Cache Python gênant
# Solution : nettoyer __pycache__
rm -r __pycache__
find . -type d -name __pycache__ -exec rm -r {} +
```

---

## 📊 Commandes Utiles Quotidiennes

```bash
# Morning routine
.\venv\Scripts\Activate.ps1
cd backend
uvicorn main:app --reload

# Dans un autre terminal
cd frontend
npm run dev

# Testing
pytest backend/

# Code quality check
black . && flake8 .

# Avant de commiter
git status
git add .
git commit -m "..."
git push
```

---

## 🎯 Workflow Développement Complet

```bash
# 1. Créer branche feature
git checkout -b feature/my-feature

# 2. Activer env & lancer serveurs
.\venv\Scripts\Activate.ps1
cd backend && uvicorn main:app --reload &
cd ../frontend && npm run dev &

# 3. Développer & tester
# (éditer code)
pytest backend/

# 4. Format & quality
black .
flake8 .

# 5. Commiter
git add .
git commit -m "feat: implement my feature"

# 6. Pousser & PR
git push origin feature/my-feature
# Créer PR sur GitHub

# 7. Merger après review
git checkout main
git pull origin main
git merge feature/my-feature
git push origin main
```

---

## 💡 Tips & Tricks

### Mettre à jour rapidement le code

```bash
# Récupérer les derniers changements
git pull origin main

# Réinstaller dépendances (si requirements.txt changé)
pip install -r requirements.txt
```

### Créer un alias pour les commandes longues

```bash
# Ajouter dans .bashrc ou .zshrc
alias activate='.\venv\Scripts\Activate.ps1'
alias serve='uvicorn main:app --reload'
alias build='black . && flake8 .'

# Puis utiliser
activate
serve
```

### Voir logs en temps réel

```bash
# Backend
uvicorn main:app --reload --log-level debug

# Frontend
npm run dev -- --verbose
```

### Debugger avec print statements

```python
# Dans le code
print(f"🐛 DEBUG: {variable = }")

# Dans terminal
python scripts/test_rag.py | grep "🐛"
```

---

## 📱 Commands par Phase

### Phase 0 — Setup
```bash
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -c "import langchain; print('✅')"
```

### Phase 1 — RAG
```bash
python scripts/scrape_articles.py
python scripts/classify_articles.py
python scripts/ingest_rag.py
python scripts/test_rag.py
```

### Phase 2 — Prompts
```bash
python backend/test_prompts.py
# Évaluation manuelle
```

### Phase 3 — Agent
```bash
python scripts/test_agent.py
cd backend && uvicorn main:app --reload
```

### Phase 4 — Fine-tuning
```bash
# Dans Google Colab
# Lancer notebook : finetuning/notebooks/02_fine_tune.ipynb
```

### Phase 5 — Interface
```bash
cd frontend && npm install && npm run dev
cd backend && uvicorn main:app --reload
```

### Phase 6 — Launch
```bash
# Tests de load
pytest backend/ -v

# Deploy
railway up  # Backend
vercel      # Frontend
```

---

## ✅ Daily Checklist

- [ ] Pull latest changes : `git pull origin main`
- [ ] Activate venv : `.\venv\Scripts\Activate.ps1`
- [ ] Install new deps : `pip install -r requirements.txt`
- [ ] Run tests : `pytest backend/`
- [ ] Start dev servers : `uvicorn` + `npm run dev`
- [ ] Before push : `git status` → `git commit` → `git push`

---

**Save this file for quick reference!** 📌
