# 📁 Structure du Projet MarketAI

Guide complet de l'organisation des fichiers et dossiers.

---

## 🏗️ Vue d'Ensemble

```
marketai/
├── 📄 README.md                    # Documentation principale
├── 📄 requirements.txt             # Dépendances Python
├── 📄 .env.example                 # Template variables d'env
├── 📄 .gitignore                   # Fichiers ignorés Git
│
├── 📁 backend/                     # 🔧 API & Orchestration
│   ├── main.py                     # Entrée FastAPI
│   ├── requirements-backend.txt    # Deps backend
│   ├── .env.backend                # Vars d'env backend
│   │
│   ├── 📁 agents/                  # Agents LangGraph
│   │   ├── __init__.py
│   │   ├── orchestrator.py         # Orchestrateur principal
│   │   ├── nodes.py                # Nœuds du graphe
│   │   └── tools.py                # Outils de l'agent
│   │
│   ├── 📁 rag/                     # Pipeline RAG
│   │   ├── __init__.py
│   │   ├── retriever.py            # ChromaDB retriever
│   │   ├── embeddings.py           # Configuration embeddings
│   │   ├── reranker.py             # Cross-encoder reranking
│   │   └── chunking.py             # Smart chunking
│   │
│   ├── 📁 prompts/                 # Templates de prompts
│   │   ├── system_prompt.py        # Persona consultant
│   │   ├── strategy.py             # Strategy template
│   │   ├── copywriting.py          # Copywriting template
│   │   ├── social_media.py         # Social media template
│   │   ├── email.py                # Email sequences
│   │   ├── page_vitrine.py         # Landing page template
│   │   ├── competitor.py           # Competitor analysis
│   │   └── pricing.py              # Pricing strategy
│   │
│   ├── 📁 tools/                   # Outils spécialisés
│   │   ├── web_search.py           # DuckDuckGo search
│   │   ├── html_generator.py       # Page vitrine Gen
│   │   ├── competitor_analyzer.py  # Web scraping
│   │   ├── calendar_generator.py   # Calendrier éditorial
│   │   ├── roi_calculator.py       # ROI estimator
│   │   └── pdf_exporter.py         # Export PDF
│   │
│   ├── 📁 api/                     # Routes FastAPI
│   │   ├── __init__.py
│   │   ├── routes.py               # Endpoints principaux
│   │   ├── auth.py                 # Authentification
│   │   ├── middleware.py           # Middlewares
│   │   └── models.py               # Pydantic models
│   │
│   └── 📁 tests/                   # Tests backend
│       ├── test_rag.py
│       ├── test_agents.py
│       └── test_prompts.py
│
├── 📁 frontend/                    # 🎨 Interface utilisateur
│   ├── package.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   │
│   ├── 📁 pages/                   # Pages Next.js
│   │   ├── index.tsx               # Home
│   │   ├── dashboard.tsx           # User dashboard
│   │   ├── chat.tsx                # Chat interface
│   │   ├── generator.tsx           # Page generator
│   │   └── api/                    # API routes
│   │
│   ├── 📁 components/              # Composants React
│   │   ├── ChatInterface.tsx
│   │   ├── Dashboard.tsx
│   │   ├── Navbar.tsx
│   │   ├── Footer.tsx
│   │   └── widgets/                # Widgets réutilisables
│   │
│   ├── 📁 styles/                  # CSS/TailwindCSS
│   │   ├── globals.css
│   │   └── components.css
│   │
│   ├── 📁 utils/                   # Helpers
│   │   ├── api.ts                  # API client
│   │   └── format.ts               # Formatters
│   │
│   ├── 📁 public/                  # Assets statiques
│   │   ├── logo.svg
│   │   ├── favicon.ico
│   │   └── images/
│   │
│   └── 📁 types/                   # TypeScript types
│       └── index.ts
│
├── 📁 data/                        # 📊 Données RAG
│   ├── 📁 raw/                     # Documents bruts
│   │   ├── 📁 marketing_strategy/  # Stratégie générale
│   │   ├── 📁 copywriting/         # Rédaction persuasive
│   │   ├── 📁 social_media/        # Guides plateformes
│   │   ├── 📁 ecommerce/           # Conversion, panier
│   │   ├── 📁 local_business/      # PME proximité
│   │   ├── 📁 case_studies/        # Études de cas
│   │   ├── 📁 templates/           # Modèles emails/posts
│   │   └── 📁 market_data/         # Benchmarks, stats
│   │
│   └── 📁 processed/               # Données traitées
│       ├── chroma_db/              # ChromaDB vectorisée
│       └── embeddings.pkl          # Cache embeddings
│
├── 📁 finetuning/                  # 🤖 Fine-tuning
│   ├── requirements-ft.txt
│   ├── dataset.json                # 1500+ paires Alpaca
│   ├── 📁 notebooks/
│   │   ├── 01_data_prep.ipynb      # Préparation dataset
│   │   ├── 02_fine_tune.ipynb      # Fine-tuning QLoRA
│   │   └── 03_evaluation.ipynb     # Évaluation modèle
│   ├── 📁 models/                  # Modèles locaux
│   │   └── mistral-7b-finetuned/
│   └── 📁 eval_results/            # Résultats évaluation
│
├── 📁 scripts/                     # 🛠️ Utilitaires
│   ├── scrape_articles.py          # Collecte web
│   ├── classify_articles.py        # Classification docs
│   ├── ingest_rag.py               # Ingestion ChromaDB
│   ├── test_rag.py                 # Test RAG
│   ├── test_agent.py               # Test agent
│   └── setup_env.py                # Setup initial
│
├── 📁 docs/                        # 📚 Documentation
│   ├── README.md                   # Vue d'ensemble
│   ├── ROADMAP.md                  # Phases développement
│   ├── SETUP_GUIDE.md              # Configuration Python
│   ├── RAG_ARCHITECTURE.md         # Détails RAG
│   ├── AGENT_ARCHITECTURE.md       # Détails agent
│   ├── PROMPTS.md                  # Library prompts
│   ├── API_REFERENCE.md            # Documentation API
│   └── DEPLOYMENT.md               # Déploiement prod
│
├── 📁 .github/                     # GitHub config
│   └── workflows/
│       ├── ci.yml                  # CI/CD tests
│       ├── deploy.yml              # Déploiement
│       └── code-quality.yml        # Code quality
│
├── 📁 logs/                        # 📝 Logs application
│   └── .gitkeep
│
└── 📁 venv/                        # 🐍 Env virtuel (ignoré)
    └── [Python packages]
```

---

## 📄 Fichiers Clés

### Racine du Projet

| Fichier | Rôle |
|---------|------|
| `README.md` | Documentation principale & overview |
| `requirements.txt` | Toutes les dépendances Python |
| `.env.example` | Template variables (commiter) |
| `.env` | Secrets réels (NE PAS commiter) |
| `.gitignore` | Fichiers à ignorer dans Git |

### Backend (`/backend`)

| Fichier | Rôle |
|---------|------|
| `main.py` | Entrée FastAPI, config server |
| `agents/orchestrator.py` | Orchestration LangGraph |
| `rag/retriever.py` | ChromaDB retrieval |
| `prompts/*.py` | Templates de prompts optimisés |
| `tools/*.py` | Outils agent (search, gen HTML, etc.) |
| `api/routes.py` | Endpoints FastAPI |

### Frontend (`/frontend`)

| Fichier | Rôle |
|---------|------|
| `pages/index.tsx` | Homepage landing |
| `pages/dashboard.tsx` | Dashboard utilisateur |
| `pages/chat.tsx` | Interface chat principale |
| `components/ChatInterface.tsx` | Composant chat |
| `utils/api.ts` | Client API + endpoints |

### Données (`/data`)

| Dossier | Contenu |
|---------|---------|
| `raw/marketing_strategy/` | Articles stratégie générale |
| `raw/copywriting/` | Techniques de rédaction |
| `raw/social_media/` | Guides Instagram, TikTok, etc. |
| `raw/ecommerce/` | Conversion, panier, fidélisation |
| `raw/case_studies/` | Études de cas avec métriques |
| `processed/chroma_db/` | Base vectorielle ChromaDB |

### Documentation (`/docs`)

| Fichier | Contenu |
|---------|---------|
| `ROADMAP.md` | Phases 0-6 détaillées |
| `SETUP_GUIDE.md` | Configuration Python |
| `RAG_ARCHITECTURE.md` | Pipeline RAG expliqué |
| `AGENT_ARCHITECTURE.md` | LangGraph détaillé |
| `API_REFERENCE.md` | Documentation endpoints |

---

## 🔄 Workflow Typique

### Ajouter un Document RAG
```bash
# 1. Placer le fichier
cp document.txt data/raw/category/

# 2. Exécuter ingestion
python scripts/ingest_rag.py

# 3. Vérifier dans ChromaDB
python -c "from backend.rag import retriever; retriever.test()"
```

### Créer un Nouveau Prompt
```bash
# 1. Créer dans /backend/prompts/
touch backend/prompts/new_template.py

# 2. Implémenter template
# 3. Tester
python -c "from backend.prompts import new_template"

# 4. Intégrer dans orchestrateur
```

### Développer une Feature Frontend
```bash
# 1. Créer la page
touch frontend/pages/feature.tsx

# 2. Ajouter composants
mkdir frontend/components/Feature/

# 3. Tester localement
npm run dev

# 4. Commiter
git add frontend/
git commit -m "feat: add feature page"
```

---

## 📊 Taille des Dossiers

### Estimations
```
backend/          : ~500 KB (code + configs)
frontend/         : ~1 MB (node_modules exclus)
data/raw/         : ~50-100 MB (documents)
data/processed/   : ~5-10 MB (embeddings)
finetuning/       : ~500 MB (modèles)
docs/             : ~500 KB (markdown)
```

**Total projet :** ~600 MB-1 GB (avec dépendances)

---

## 🔐 Sécurité & Secrets

### Fichiers à NE PAS Commiter
```
.env              # Secrets réels
venv/             # Env virtuel
node_modules/     # Dépendances npm
__pycache__/      # Cache Python
.chroma/          # Base vectorielle locale
*.log             # Logs
*.pkl             # Modèles sérializés
```

### Fichiers à Commiter
```
.env.example      # Template (pas de secrets)
requirements.txt  # Dependencies
.gitignore        # Config ignore
docs/             # Documentation
src/              # Code source
```

---

## 🚀 Bonnes Pratiques

### Nommage des Fichiers
- `snake_case` pour Python : `my_module.py`
- `camelCase` pour TypeScript : `MyComponent.tsx`
- `kebab-case` pour folders : `/my-folder/`

### Structure Code
```python
# backend/agents/orchestrator.py
from typing import Dict, List
from langchain import LLMChain
from .tools import web_search, rag_retrieve

class MainOrchestrator:
    """Main agent orchestrator."""
    
    def __init__(self, llm):
        self.llm = llm
    
    def execute(self, task: str) -> str:
        """Execute a task."""
        pass
```

### Imports
```python
# Order: stdlib → third-party → local
import os
from typing import Dict

import langchain
from dotenv import load_dotenv

from backend.rag import retriever
```

---

## 📋 Checklist Maintenance

### Hebdomadaire
- [ ] Lancer tests : `pytest backend/`
- [ ] Vérifier code quality : `flake8 backend/`
- [ ] Format code : `black backend/`

### Mensuellement
- [ ] Mettre à jour dépendances
- [ ] Archiver vieux logs
- [ ] Backup données RAG
- [ ] Review documentation

### À Chaque Commit
- [ ] Pas de `.env` réel
- [ ] Pas de `venv/` commité
- [ ] Tests passent
- [ ] Code formaté

---

## 🔗 Liens Utiles

- [FastAPI Structure](https://fastapi.tiangolo.com/tutorial/)
- [Next.js File-based Routing](https://nextjs.org/docs/routing/introduction)
- [Python Project Structure](https://docs.python-guide.org/writing/structure/)

---

**Dernière mise à jour :** May 6, 2026
