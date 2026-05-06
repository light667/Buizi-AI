# 🚀 Guide de Démarrage MarketAI

## Configuration de l'Environnement Python

Ce guide vous aide à mettre en place votre environnement de développement pour MarketAI.

### 1. Installation de Python

**Actuellement configuré :**
- Python 3.13.12
- Chemin : `C:/Users/netha/AppData/Local/Programs/Python/Python313/python.exe`

Pour tester votre installation :
```bash
python --version
# Output: Python 3.13.12
```

### 2. Créer un Environnement Virtuel

Un environnement virtuel isole les dépendances du projet des dépendances système.

**Sur Windows (PowerShell) :**
```powershell
# Créer l'environnement
python -m venv venv

# Activer l'environnement
.\venv\Scripts\Activate.ps1

# Si vous avez une erreur de permission, exécutez :
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Sur macOS/Linux :**
```bash
# Créer l'environnement
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate
```

### 3. Vérifier que l'Environnement est Actif

L'invite de commande devrait commencer par `(venv)` :
```
(venv) C:\Users\netha\Dev\projet-buizi>
```

### 4. Installer les Dépendances

```bash
# Mettre à jour pip
pip install --upgrade pip

# Installer toutes les dépendances
pip install -r requirements.txt
```

**Cela installe :**
- Framework IA : LangChain, LangGraph
- RAG : ChromaDB, LlamaIndex
- Backend : FastAPI
- Fine-tuning : Unsloth, PEFT
- Utilitaires : NumPy, Pandas, etc.

### 5. Configuration des Variables d'Environnement

```bash
# Copier le fichier exemple
cp .env.example .env

# Éditer .env avec vos clés API
# (utiliser VS Code ou notepad++)
```

**Variables OBLIGATOIRES à remplir :**
- `GROQ_API_KEY` — [Obtenez-la ici](https://console.groq.com/keys)
- `GOOGLE_AI_KEY` — [Obtenez-la ici](https://aistudio.google.com)

### 6. Tester l'Installation

```bash
# Test 1 : Vérifier Python
python --version

# Test 2 : Vérifier les imports clés
python -c "import langchain; import fastapi; print('✅ Dépendances OK')"

# Test 3 : Vérifier l'accès à l'API
python -c "from langchain_groq import ChatGroq; print('✅ Groq API OK')"
```

---

## Désactiver l'Environnement

Quand vous avez terminé :
```bash
deactivate
```

L'invite revient à la normale sans `(venv)`.

---

## Structure des Dossiers

```
projet-buizi/
├── venv/                    # ← Environnement virtuel (ignoré par Git)
├── backend/                 # Code API
├── frontend/                # Code Interface
├── data/                    # Données RAG
├── finetuning/             # Fine-tuning notebooks
├── scripts/                # Utilitaires
├── requirements.txt        # Dépendances
├── .env                    # Variables (⚠️ Privé - ne pas commiter)
├── .env.example            # Template (✅ À commiter)
└── README.md               # Documentation
```

---

## Commandes Utiles

### Gestion de l'Environnement
```bash
# Lister les packages installés
pip list

# Afficher la version Python
python --version

# Localisation de Python
where python  # Windows
which python  # macOS/Linux
```

### Développement
```bash
# Lancer le backend
cd backend
uvicorn main:app --reload

# Lancer le frontend
cd frontend
npm run dev

# Exécuter un script
python scripts/classify_articles.py
```

### Testing
```bash
# Lancer les tests
pytest

# Avec couverture
pytest --cov=.
```

---

## Dépannage

### Erreur : "python : command not found"
**Solution :** Utiliser le chemin complet :
```bash
C:/Users/netha/AppData/Local/Programs/Python/Python313/python.exe -m venv venv
```

### Erreur : "venv not activated"
**Solution :** Vérifier l'invite de commande commence par `(venv)`. Si non :
```bash
# Windows
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

### Erreur : "ModuleNotFoundError: No module named 'langchain'"
**Solution :** L'environnement n'est pas activé ou les dépendances ne sont pas installées :
```bash
# Vérifier activation
echo %VIRTUAL_ENV%  # Windows
echo $VIRTUAL_ENV  # macOS/Linux

# Réinstaller si vide
pip install -r requirements.txt
```

### Erreur : "GROQ_API_KEY not found"
**Solution :** Le fichier `.env` n'existe pas ou n'est pas lu correctement :
```bash
# Créer depuis le template
cp .env.example .env

# Vérifier que la clé est présente
cat .env | grep GROQ_API_KEY
```

---

## Optimisations pour le Développement

### 1. Installation en Mode Édition
Pour développer les packages locaux :
```bash
pip install -e .
```

### 2. Requirements par Environnement
**requirements-dev.txt :**
```
-r requirements.txt
pytest==7.4.4
black==24.1.1
flake8==7.0.0
```

Installation :
```bash
pip install -r requirements-dev.txt
```

### 3. Synchroniser les Dépendances
```bash
pip freeze > requirements.txt
```

---

## Prochaines Étapes

1. ✅ **Environnement Python configuré** (vous êtes ici)
2. ⏳ **Lancer le backend FastAPI**
3. ⏳ **Configurer la base de données**
4. ⏳ **Collecter les données RAG**
5. ⏳ **Tester le pipeline complet**

---

## Resources Additionnelles

- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangChain Docs](https://python.langchain.com/docs)
- [ChromaDB Documentation](https://docs.trychroma.com)

---

**Questions ? Ouvrez une issue sur GitHub !** 🚀
