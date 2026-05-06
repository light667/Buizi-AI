# 📋 ROADMAP MarketAI — Phases de Développement

**Durée totale :** 10-14 semaines | **Budget :** 0$ (gratuit)

---

## Phase 0 — Préparation & Environnement (Semaine 1)

### 🎯 Objectif
Mettre en place un environnement de développement structuré avant d'écrire du code métier.

### ✅ Tâches Complétées
- [x] Structure GitHub créée
- [x] Environnement Python configuré (Python 3.13.12)
- [x] Requirements.txt complété (30+ dépendances)
- [x] .env.example configuré
- [x] .gitignore complet
- [x] README professionnel rédigé
- [x] SETUP_GUIDE.md créé

### ⏳ Tâches Restantes (Phase 0)
- [ ] FastAPI endpoint `/health` fonctionnel
- [ ] Déploiement skeleton sur Railway/Render
- [ ] Vérification du endpoint en production

### Critères de Validation
- ✅ Dépôt GitHub structuré avec historique
- ✅ Environnement Python isolé et fonctionnel
- [ ] Endpoint `/health` répond 200 en production

**Estimation :** 2-3 heures restantes

---

## Phase 1 — Pipeline RAG (Semaines 2-3)

### 🎯 Objectif
Construire le moteur de connaissance marketing — la base vectorielle contenant 300-500 documents de qualité.

### Tâches

#### Collecte de Données
- [ ] Scraper 100+ articles HubSpot Blog
- [ ] Télécharger 50+ articles Neil Patel
- [ ] Récupérer guides MarketingProfs
- [ ] Extraire études Think with Google
- [ ] Collecter ressources Buffer, Sprout Social

#### Structuration
- [ ] Classer documents en 8 catégories :
  - `marketing_strategy/` (stratégies générales)
  - `copywriting/` (techniques de rédaction)
  - `social_media/` (guides plateformes)
  - `ecommerce/` (conversion, panier)
  - `local_business/` (PME proximité)
  - `case_studies/` (études de cas)
  - `templates/` (modèles emails/posts)
  - `market_data/` (benchmarks, stats)

#### Pipeline RAG
- [ ] Installer ChromaDB
- [ ] Configurer embeddings (sentence-transformers)
- [ ] Implémenter chunking (500 tokens, overlap 50)
- [ ] Générer embeddings pour tous les documents
- [ ] Implémenter fonction de retrieval
- [ ] Ajouter reranking (cross-encoder)
- [ ] Tester sur 20 questions marketing
- [ ] Documenter dans Jupyter Notebook

### Critères de Validation
- ✅ 300-500 documents collectés et nettoyés
- ✅ ChromaDB opérationnel avec embeddings
- ✅ Retrieval atteint >80% précision sur jeu test
- ✅ Temps réponse <500ms pour une requête

### Estimations par Tâche
| Tâche | Durée |
|-------|-------|
| Collecte données | 4-6 heures |
| Nettoyage & structuration | 3-4 heures |
| Implémentation ChromaDB | 4-5 heures |
| Testing & optimisation | 3-4 heures |
| **Total Phase 1** | **14-19 heures** |

---

## Phase 2 — Prompt Engineering (Semaines 3-4)

### 🎯 Objectif
Créer la bibliothèque de prompts optimisés qui définissent le comportement expert du système.

### 8+ Templates à Créer

#### 1. SYSTEM_PROMPT
```
Persona : Consultant marketing senior avec 15+ ans d'expérience
Spécialités : Croissance PME, conversion, stratégie numérique
Ton : Expert bienveillant, données-driven, actionnable
```

#### 2. STRATEGY_TEMPLATE (Chain of Thought)
- Audit situation actuelle
- Analyse cible audience
- Sélection canaux
- Budget allocation
- KPIs et milestones

#### 3. COPYWRITING_TEMPLATE (Few-shot)
- 3-5 exemples de copy haute performance
- Framework AIDA/PAS/BAB
- Angles psychologiques
- Tests A/B recommendations

#### 4. SOCIAL_MEDIA_TEMPLATE
- Par plateforme : Instagram, TikTok, LinkedIn, Facebook
- Spécificités format (captions, hashtags, emojis)
- Best practices timing
- Engagement tactics

#### 5. EMAIL_TEMPLATE
- Séquence 3-7 mails
- Hook → Problem → Solution → CTA
- Taux ouverture optimisés
- Personnalisation tokens

#### 6. PAGE_VITRINE_TEMPLATE
- De brief → HTML responsive
- Structure UX proven
- Copy sections éprouvées
- CTA psychology

#### 7. COMPETITOR_ANALYSIS_TEMPLATE
- Positionnement concurrents
- Forces/faiblesses
- Gaps à exploiter
- Différenciation strategy

#### 8. PRICING_TEMPLATE
- Positionnement tarifaire
- Psychologie des prix
- Tiers pricing
- Justification valeur

### Techniques à Appliquer

| Technique | Application |
|-----------|------------|
| **Few-shot** | 3-5 exemples dans chaque template |
| **Chain of Thought** | Forcer raisonnement étape par étape |
| **Role Prompting** | "Tu es un consultant avec..." |
| **Output Formatting** | Contraindre format (JSON/Markdown/HTML) |
| **Negative Prompting** | "Ne jamais faire/dire..." |

### Critères de Validation
- ✅ 8+ templates testés sur 10 inputs différents chacun
- ✅ Score qualité humain : >8/10 en moyenne
- ✅ Consistency dans les outputs
- ✅ Pertinence marketing validée

### Estimations
| Tâche | Durée |
|-------|-------|
| Création templates | 5-7 heures |
| Testing & itération | 4-6 heures |
| Évaluation humaine | 3-4 heures |
| **Total Phase 2** | **12-17 heures** |

---

## Phase 3 — AI Agent Orchestrator (Semaines 5-6)

### 🎯 Objectif
Construire le cerveau du système — l'agent qui décompose une demande complexe en sous-tâches optimales.

### Architecture LangGraph

```
Intent Classifier
    ↓
Context Retriever (RAG + Memory)
    ↓
Task Planner
    ↓
Executor (Outils spécialisés)
    ↓
Quality Checker
    ↓
Formatter
```

### 7+ Outils à Implémenter

| Outil | Fonction | Exemple |
|-------|----------|---------|
| `web_search` | DuckDuckGo API temps réel | Tendances secteur |
| `rag_retrieve` | Interroger base connaissance | Exemples copywriting |
| `generate_html` | Page vitrine complète | Brief → HTML |
| `analyze_competitors` | Scraper + insights | Positionnement |
| `generate_calendar` | Calendrier éditorial 30j | Posts réseaux |
| `calculate_roi` | Estimation ROI campagne | Budget → Revenue |
| `save_to_memory` | Profil client persistant | Historique |

### Nœuds LangGraph

1. **Intent Classifier** → Détecte type de demande
2. **Context Retriever** → Récupère RAG + mémoire client
3. **Task Planner** → Décompose en sous-tâches
4. **Executor** → Exécute chaque tâche
5. **Quality Checker** → Vérifie et améliore
6. **Formatter** → Format final (Markdown/PDF/HTML)

### Critères de Validation
- ✅ L'agent traite demande complète sans intervention
- ✅ Temps réponse <30s pour stratégie
- ✅ Tous les outils opérationnels
- ✅ Gestion des erreurs et fallbacks

### Estimations
| Tâche | Durée |
|-------|-------|
| Architecture LangGraph | 4-5 heures |
| Implémentation outils | 8-10 heures |
| Testing end-to-end | 4-5 heures |
| **Total Phase 3** | **16-20 heures** |

---

## Phase 4 — Fine-Tuning du Modèle (Semaines 7-8)

### 🎯 Objectif
Entraîner un modèle spécialisé qui parle le langage du marketing comme un consultant senior.

### Dataset — Format Alpaca

```json
{
  "instruction": "Crée un slogan pour une boulangerie artisanale",
  "input": "Nom: La Mie Dorée. Valeurs: tradition, qualité, local.",
  "output": "Voici 3 slogans:\n1. 'Le goût du vrai' (nostalgie)..."
}
```

### 1500+ Paires à Créer

| Catégorie | Nombre |
|-----------|--------|
| Slogans & taglines | 150 |
| Emails de vente | 200 |
| Scripts social media | 200 |
| Stratégies sectorielles | 300 |
| Analyse concurrence | 100 |
| Conseils pricing | 100 |
| Calendriers contenu | 150 |
| Copywriting landing pages | 150 |
| Réponses problèmes marketing | 200 |
| **TOTAL** | **1500+** |

### Pipeline Fine-Tuning

1. **Collecte & Validation** (20h)
   - Générer avec GPT-4
   - Vérifier manuellement
   - Enrichir avec vrais cas

2. **Préparation Google Colab** (2h)
   - Setup GPU T4 gratuit
   - Installer Unsloth + TRL

3. **Entraînement QLoRA** (6-8h)
   - Modèle base : Mistral 7B
   - 4-bit quantization
   - Learning rate : 2e-4
   - Epochs : 3

4. **Évaluation & Deployment** (4h)
   - Test blind 50 questions
   - Push Hugging Face Hub
   - Intégration pipeline

### Métriques d'Évaluation

| Métrique | Cible |
|----------|--------|
| Préférence humaine | >70% vs base |
| Pertinence marketing | >8/10 |
| Hallucination rate | <5% |
| Coherence output | >9/10 |

### Critères de Validation
- ✅ Modèle fine-tuné préféré 70%+ des cas
- ✅ Disponible sur Hugging Face Hub
- ✅ Intégré dans pipeline principal

### Estimations
| Tâche | Durée |
|-------|-------|
| Collecte dataset | 15-20 heures |
| Validation qualité | 5-7 heures |
| Fine-tuning | 6-8 heures |
| Évaluation | 3-4 heures |
| **Total Phase 4** | **29-39 heures** |

---

## Phase 5 — Interface & Livrables Avancés (Semaines 9-10)

### 🎯 Objectif
Construire l'interface utilisateur professionnelle qui fait de MarketAI un vrai produit.

### Frontend (Next.js)

- [ ] Chat interface avec streaming token/token
- [ ] Dashboard client avec historique
- [ ] Téléchargement livrables (HTML, PDF, DOCX)
- [ ] Profil entreprise (secteur, taille, concurrents)
- [ ] Bibliothèque pages vitrine générées

### Backend Finalisé

- [ ] Génération page vitrine : brief → HTML responsive
- [ ] Export PDF (WeasyPrint)
- [ ] Mémoire persistante (profil client)
- [ ] Webhooks Zapier/Make
- [ ] Rate limiting par plan

### Critères de Validation
- ✅ Utilisateur non-technique peut utiliser sans aide
- ✅ Page vitrine générée en <60s
- ✅ Chat responsive et fluide

### Estimations
| Tâche | Durée |
|-------|-------|
| Frontend Next.js | 8-10 heures |
| Backend finitions | 6-8 heures |
| Testing UX | 4-5 heures |
| **Total Phase 5** | **18-23 heures** |

---

## Phase 6 — Startup-Ready & Lancement (Semaines 11-14)

### 🎯 Objectif
Transformer le projet technique en produit commercial viable.

### Tâches Produit

- [ ] Landing page marketing (Next.js + Tailwind)
- [ ] Système paiement Stripe
- [ ] Onboarding guidé
- [ ] Limit tokens par plan (Free/Pro/Enterprise)
- [ ] Dashboard analytics
- [ ] Documentation API

### Go-to-Market

- [ ] Recruter 10 beta-testeurs
- [ ] Collecter feedback structuré
- [ ] Pitch deck 8 slides
- [ ] Publish Product Hunt
- [ ] Communauté Discord/Twitter

### Critères de Validation
- ✅ 10 beta-utilisateurs actifs
- ✅ Feedback positif documenté
- ✅ Infra <50€/mois
- ✅ Pitch deck finalisé

### Estimations
| Tâche | Durée |
|-------|-------|
| Landing page | 4-6 heures |
| Système paiement | 3-4 heures |
| Admin dashboard | 5-6 heures |
| Beta testing | 8-10 heures |
| Go-to-market | 6-8 heures |
| **Total Phase 6** | **26-34 heures** |

---

## 📊 Timeline Global

```
Week 1  : Phase 0 ✅ (Env)
Week 2-3: Phase 1 (RAG)
Week 3-4: Phase 2 (Prompts)
Week 5-6: Phase 3 (Agent)
Week 7-8: Phase 4 (Fine-tuning)
Week 9-10: Phase 5 (Interface)
Week 11-14: Phase 6 (Startup)
```

**Total estimé :** 120-160 heures (~3-4 semaines full-time)

---

## ✅ Checklist Globale

### Phase 0 — Environnement
- [x] Dépôt GitHub créé
- [x] Comptes gratuits ouverts
- [x] Python 3.13 configuré
- [x] Requirements.txt complet
- [x] .env.example créé
- [ ] FastAPI /health en prod

### Phase 1 — RAG
- [ ] 300-500 documents collectés
- [ ] ChromaDB opérationnel
- [ ] Retrieval >80% précision
- [ ] Documentation RAG

### Phase 2 — Prompts
- [ ] 8+ templates créés
- [ ] Score humain >8/10
- [ ] Chain of Thought implémenté

### Phase 3 — Agent
- [ ] LangGraph avec 7+ outils
- [ ] Test end-to-end <30s
- [ ] Gestion erreurs robuste

### Phase 4 — Fine-Tuning
- [ ] Dataset 1500+ paires
- [ ] Modèle sur Hugging Face
- [ ] Préférence humaine >70%

### Phase 5 — Interface
- [ ] Next.js frontend
- [ ] Chat avec streaming
- [ ] Générateur page vitrine <60s

### Phase 6 — Startup
- [ ] 10 beta-testeurs
- [ ] Infra <50€/mois
- [ ] Pitch deck prêt

---

## 🚀 Prochaines Actions

**Aujourd'hui :**
1. ✅ Configurer environnement Python (FAIT)
2. ✅ Rédiger README professionnel (FAIT)
3. [ ] **Lancer FastAPI endpoint /health**

**Cette semaine (Phase 0 finale) :**
4. [ ] Déployer skeleton sur Railway
5. [ ] Tester endpoint en production
6. [ ] Commiter tout sur GitHub

**Prochaine semaine (Phase 1) :**
7. [ ] Démarrer collecte articles
8. [ ] Setup ChromaDB local

---

## 📚 Documentation Associée

- [SETUP_GUIDE.md](SETUP_GUIDE.md) — Configuration Python
- [README.md](../README.md) — Vue d'ensemble projet
- [Architecture RAG](RAG_ARCHITECTURE.md) — Détails pipeline
- [Prompt Library](PROMPTS.md) — Templates optimisés

---

**Dernière mise à jour :** May 6, 2026  
**Statut :** Phase 0 avancée ⏳
