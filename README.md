# Buizi AI — L'IA Consultant Marketing

![Status](https://img.shields.io/badge/Status-Development-yellow?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.13+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**Un système d'intelligence artificielle multi-agent générant plus de revenus pour les PME, artisans et créateurs.**

> 📊 Stratégies complètes • 🎨 Copywriting haute conversion • 📱 Calendriers éditoriaux • 💰 Plans de pricing intelligent

---

## 🎯 Vision du Projet

Buizi AI n'est **pas un chatbot**. C'est un système d'IA multi-agent conçu pour exécuter des **missions marketing complètes** et mesurables.

### Proposition de Valeur Unique

| Défi | Avant | Avec Buizi AI |
|------|-------|----------------|
| **Coût d'un consultant** | 3 000 à 10 000€/mois | 49 à 199€/mois |
| **Disponibilité** | 9h-18h (limité) | 24/24, 365j |
| **Setup** | 2-3 semaines | Immédiat |
| **Assets prêts à l'emploi** | Non | Oui ✓ |

### Cible Marché

- 💼 **PME et TPE** (1-50 collaborateurs)
- 🎨 **Artisans & Créateurs** (indépendants)
- 🚀 **Startups en croissance** (early stage)
- 📦 **E-commerçants** (boutiques en ligne)

### Marché Adressable
- **France** : 3,5 millions de TPE/PME
- **Europe** : +15 millions d'entreprises de petite taille
- **Tarif visé** : 49€ (Starter) → 199€ (Pro) → Custom (Enterprise)

---

## 🚀 Livrables Clés

| Livrable | Description | Temps |
|----------|-------------|--------|
| **Stratégie complète** | Positionnement + canaux + budget + KPIs | ~5 min |
| **Page vitrine HTML** | Générée, responsive, téléchargeable | ~3 min |
| **Calendrier éditorial** | 30 posts réseaux sociaux prêts à publier | ~4 min |
| **Copywriting publicitaire** | Facebook Ads, TikTok, Google Ads | ~5 min |
| **Séquence emails de vente** | 3-7 mails avec CTA optimisés | ~3 min |
| **Analyse concurrentielle** | Web scraping temps réel + insights | ~10 min |
| **Plan de pricing** | Positionnement tarifaire psychologique | ~3 min |
| **Rapport de performance** | Analyse + recommandations d'amélioration | ~5 min |

---

## 🏗️ Architecture Technique

### Stack — Budget 0$

```
┌─────────────────────────────────────────────┐
│         Frontend (Next.js + React)          │
│   Chat streaming • Dashboards • Téléchargements│
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│       Backend (FastAPI + Python)            │
│  Routes API • Gestion des tâches            │
└────────────────────┬────────────────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌────────┐  ┌──────────┐  ┌────────────┐
   │ Agent  │  │   RAG    │  │   LLM      │
   │ Graph  │  │(ChromaDB)│  │ (Groq/Gemini)
   │LangGraph   └──────────┘  └────────────┘
   └────────┘
        │
   ┌────▼──────────────────────┐
   │  Outils spécialisés       │
   │  • Web Search             │
   │  • HTML Generator         │
   │  • Competitor Analysis    │
   │  • PDF Export             │
   └───────────────────────────┘
```

### Technologies Utilisées

#### LLM & AI
- **Groq API** — Llama 3.1 70B (30 req/min gratuit)
- **Google Gemini** — 1M tokens/mois gratuit
- **Ollama** — Local LLM (0$ absolu)

#### RAG (Retrieval Augmented Generation)
- **ChromaDB** — Base vectorielle open-source
- **LlamaIndex** — Framework RAG
- **sentence-transformers** — Embeddings

#### Orchestration d'Agents
- **LangGraph** — Graphe d'agents robuste
- **LangChain** — Framework IA mature

#### Backend & Frontend
- **FastAPI** — Backend API ultra-rapide
- **Next.js 14** — Frontend React moderne
- **Supabase** — BDD PostgreSQL gratuite
- **Vercel** — Déploiement frontend (gratuit)
- **Railway/Render** — Déploiement backend (gratuit)

#### Fine-Tuning
- **Unsloth** — Fine-tuning ultra-optimisé
- **QLoRA** — Adaptation légère et efficace
- **Google Colab** — GPU T4 gratuit

---

## 📂 Structure du Projet

```
marketai/
├── backend/                    # 🔧 API & Orchestration
│   ├── agents/                 # LangGraph agents
│   ├── rag/                    # Pipeline RAG
│   ├── prompts/                # Templates de prompts
│   ├── tools/                  # Web search, HTML gen, etc.
│   ├── api/                    # Routes FastAPI
│   └── main.py                 # Entrée backend
│
├── frontend/                   # 🎨 Interface utilisateur
│   ├── pages/                  # Next.js pages
│   ├── components/             # Composants React
│   └── styles/                 # TailwindCSS
│
├── data/                       # 📊 Données pour le RAG
│   ├── raw/                    # Documents bruts
│   │   ├── marketing_strategy/
│   │   ├── copywriting/
│   │   ├── social_media/
│   │   ├── ecommerce/
│   │   ├── local_business/
│   │   ├── case_studies/
│   │   ├── templates/
│   │   └── market_data/
│   └── processed/              # Données nettoyées & vectorisées
│
├── finetuning/                 # 🤖 Fine-tuning du modèle
│   ├── dataset.json            # Paires d'entraînement
│   └── notebooks/              # Google Colab notebooks
│
├── scripts/                    # 🛠️ Utilitaires
│   ├── scrape_articles.py      # Collecte de données web
│   ├── classify_articles.py    # Classification automatique
│   └── ingest_rag.py           # Ingestion dans ChromaDB
│
├── docs/                       # 📚 Documentation
│   └── ROADMAP.md              # Phases de développement
│
├── requirements.txt            # Dépendances Python
├── .env.example                # Variables d'environnement
└── README.md                   # Ce fichier
```

---

## 🚀 Démarrage Rapide

### Prérequis

- **Python 3.13+** ✅ (configuré)
- **Git** (pour le versioning)
- **Comptes gratuits** :
  - [Groq API](https://console.groq.com/keys)
  - [Google AI Studio](https://aistudio.google.com)
  - [Hugging Face](https://huggingface.co)
  - [Supabase](https://supabase.com)
  - [Vercel](https://vercel.com)

### Installation

#### 1️⃣ Cloner et configurer

```bash
git clone https://github.com/light667/Buizi-AI.git
cd Buizi-AI
```

#### 2️⃣ Créer un environnement virtuel

```bash
# Sur Windows
python -m venv venv
venv\Scripts\activate

# Sur macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configurer les variables d'environnement

```bash
cp .env.example .env
# Puis éditer .env avec vos clés API
```

#### 5️⃣ Lancer le backend

```bash
cd backend
uvicorn main:app --reload
# API disponible à http://localhost:8000
```

#### 6️⃣ Lancer le frontend (dans un autre terminal)

```bash
cd frontend
npm install
npm run dev
# App disponible à http://localhost:3000
```

---

## 📋 Roadmap de Développement

### Phase 0 — Environnement (Sem. 1)
- [x] Structure GitHub
- [x] Comptes gratuits ouverts
- [x] Environnement Python configuré ✅
- [ ] FastAPI /health endpoint

### Phase 1 — RAG (Sem. 2-3)
- [ ] Collecte 100+ documents marketing
- [ ] ChromaDB opérationnel
- [ ] Retrieval >80% précision
- [ ] Documentation RAG

### Phase 2 — Prompt Engineering (Sem. 3-4)
- [ ] 8+ templates optimisés
- [ ] Chain of Thought prompting
- [ ] Few-shot examples
- [ ] Tests de qualité humains

### Phase 3 — AI Agent (Sem. 5-6)
- [ ] LangGraph orchestrator
- [ ] 7+ outils spécialisés
- [ ] Intent classification
- [ ] Task decomposition

### Phase 4 — Fine-Tuning (Sem. 7-8)
- [ ] Dataset 1500+ paires
- [ ] Unsloth + QLoRA
- [ ] Modèle sur Hugging Face
- [ ] Évaluation >70% préférence

### Phase 5 — Interface (Sem. 9-10)
- [ ] Chat Next.js avec streaming
- [ ] Dashboard client
- [ ] Générateur page vitrine
- [ ] Export PDF/DOCX

### Phase 6 — Startup (Sem. 11-14)
- [ ] Landing page
- [ ] Système Stripe
- [ ] 10 beta-testeurs
- [ ] Pitch deck

---

## 📚 Ressources & Documentation

### Guides d'Apprentissage
- **LangChain** → [python.langchain.com/docs](https://python.langchain.com/docs)
- **LangGraph Academy** → [academy.langchain.com](https://academy.langchain.com)
- **RAG from Scratch** → YouTube LangChain (15 vidéos)
- **Hugging Face Course** → [huggingface.co/learn](https://huggingface.co/learn)

### Papers & Recherches
- RAG : "Retrieval-Augmented Generation" (Lewis et al. 2020)
- Fine-Tuning : "LoRA: Low-Rank Adaptation" (arXiv 2106.09685)

---

## ⚙️ Configuration Détaillée

### Variables d'Environnement

```env
# LLM APIs
GROQ_API_KEY=your_groq_key
GOOGLE_AI_KEY=your_gemini_key

# Database
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000

# LangSmith (optional monitoring)
LANGCHAIN_API_KEY=your_langchain_key
LANGCHAIN_TRACING_V2=true
```

### Installation des Dépendances Principales

```bash
# RAG & LLM
pip install langchain langgraph chromadb llamaindex sentence-transformers

# Backend
pip install fastapi uvicorn pydantic

# Frontend (depuis dossier frontend/)
npm install next react tailwindcss

# Fine-tuning
pip install unsloth bitsandbytes peft

# Web scraping
pip install trafilatura newspaper3k beautifulsoup4
```

---

## 🧪 Tests & Validation

### Test basique du RAG

```bash
python scripts/test_rag.py
# Devrait retourner >80% de précision
```

### Test de l'agent

```bash
python backend/test_agent.py
# Brief → Stratégie complète en <30s
```

### Test du prompt engineering

```bash
python backend/test_prompts.py
# Évaluation humaine >8/10
```

---

## 🤝 Contribution

Les contributions sont bienvenues ! Pour développer :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amazing-feature`)
3. Commit vos changements (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

---

## 📊 Métriques de Succès

| Métrique | Cible | Statut |
|----------|--------|--------|
| Documents RAG | 300-500 | ⏳ En cours |
| Précision retrieval | >80% | ⏳ En cours |
| Score prompt (humain) | >8/10 | ⏳ Planifié |
| Fine-tuning préférence | >70% vs base | ⏳ Planifié |
| Temps génération stratégie | <30s | ⏳ Planifié |
| Coût infrastructure/mois | <50€ | ✅ Sur track |

---

## 📞 Support & Contact

- **GitHub Issues** → Bugs & suggestions
- **Discussions** → Idées & feedback
- **Email** → light667@github.com

---

## 📄 Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour détails.

---

<div align="center">

### 🚀 Prêt à transformer le marketing des PME ?

**[⭐ Star le repo](#)** pour suivre le développement

**[📖 Lire la documentation complète](docs/ROADMAP.md)**

</div>
