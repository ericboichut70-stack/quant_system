# TRADING_BOT — Version 1.0.0

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.10+-yellow)
![License](https://img.shields.io/badge/license-private-lightgrey)

---

Bot de trading modulaire, audité, documenté et entièrement testable.  
Cette version constitue la base stable pour les développements futurs.

---

## ✅ Fonctionnalités principales

- Analyse de tendance (EMA slope + ADX simplifié)
- Clustering de volatilité
- Détection de structure de marché (HH/HL/LH/LL)
- ZigZag simplifié
- Lecture d’orderflow (Delta, Imbalance, Absorption)
- Analyse de sentiment
- Extraction et enrichissement de features
- Prédiction de signaux
- Optimisation de paramètres
- Attribution de signaux
- Génération de signatures SHA256
- API de trading simulée
- Pipeline end‑to‑end complet

---

## ✅ Architecture

Voir `ARCHITECTURE.md` pour le diagramme complet.

---

## ✅ Pipeline complet

Le pipeline complet est disponible dans : pipeline_demo.py.

pipeline_demo.py exécute :

1. Analyse de marché  
2. Structure & ZigZag  
3. Orderflow  
4. Features & signaux  
5. Optimisation  
6. Attribution  
7. Signature  
8. Exécution simulée

---

## ✅ Documentation technique

- `MANIFEST_TECHNIQUE.md`  
- `ARCHITECTURE.md`  
- `audit_notes.md`  
- `CHANGELOG.md`  
- `RELEASE_NOTES.md`

---

## ✅ Tests

Chaque module dispose d’un script `test_*.py`.  
Un plan de tests automatisés est fourni dans `tests/`.

---

## ✅ Version

- Version stable : **v1.0.0**
- Tag Git : `v1.0.0`
- Release GitHub : publiée

---

## ✅ Licence

À définir selon ton choix (MIT, Apache 2.0, etc.).

## quant_system

## Moteur quantitatif modulaire pour analyse de marché, extraction de signaux et préparation à l’intégration ML

`quant_system` est un moteur quantitatif structuré, modulaire et extensible, conçu pour analyser les marchés financiers, extraire des signaux robustes, et préparer un pipeline complet pour des stratégies algorithmiques ou des modèles de machine learning.

Ce projet constitue une base stable, auditée et documentée, destinée à évoluer vers un système complet de trading algorithmique.

---

## ✅ Objectifs du projet

- Fournir une architecture claire, modulaire et extensible  
- Offrir un pipeline complet d’analyse de marché  
- Générer des signaux robustes et auditables  
- Préparer l’intégration future de modèles ML  
- Garantir la traçabilité via signatures SHA256  
- Permettre l’évolution vers un moteur de backtesting et de stratégie

---

## ✅ Architecture générale

Le système est organisé en modules indépendants :

quant_system/
│
├── data/ # Chargement, normalisation, prétraitement
├── indicators/   # Indicateurs techniques (EMA, ADX, volatilité…)
├── structure/    # HH/HL/LH/LL, ZigZag simplifié
├── orderflow/    # Delta, Imbalance, Absorption
├── features/     # Extraction de features multi-niveaux
├── signals/      # Génération de signaux
├── optimization/ # Optimisation de paramètres
├── attribution/  # Attribution et scoring des signaux
├── utils/        # Fonctions transversales, hashing SHA256
└── pipeline/     # Pipeline end-to-end

Chaque module est indépendant, documenté, et conçu pour être remplacé ou étendu sans casser l’ensemble.

---

## Fonctionnalités principales

### 🔹 Détection de tendance

- Pente EMA  
- ADX simplifié  
- Détection de phases directionnelles / neutres  

### 🔹 Structure de marché

- Identification HH / HL / LH / LL  
- ZigZag simplifié  
- Détection de swings  

### 🔹 Orderflow

- Delta  
- Imbalance  
- Absorption  
- Microstructure simplifiée  

### 🔹 Volatilité & clustering

- Volatility regimes  
- Clustering KMeans / DBSCAN (optionnel)  

### 🔹 Extraction de features

- Features multi‑horizons  
- Normalisation  
- Encodage temporel  

### 🔹 Génération de signaux

- Conditions multi‑modules  
- Scoring  
- Attribution  

### 🔹 Pipeline complet

- Chargement → Analyse → Features → Signaux → Hashing  
- Traçabilité complète via SHA256  

---

## ✅ Installation

```bash
git clone git@github.com:ericboichut70-stack/quant_system.git
cd quant_system
pip install -r requirements.txt

---

## ✅ Exemple d’utilisation

Voici un exemple minimal montrant comment exécuter le pipeline complet :

```python
from quant_system.pipeline import run_pipeline

results = run_pipeline(
    data_path="data/BTCUSDT.csv",
    config_path="config/default.yaml"
)

print("Signaux générés :")
print(results.signals.head())

print("Features extraites :")
print(results.features.columns)

---


---

# ✅ 7. Exemple complet d’utilisation (pipeline complet)

À mettre dans `examples/example_pipeline.py` ou dans le README :

```python
from quant_system.pipeline import run_pipeline
from quant_system.utils.hashing import compute_hash

DATA = "data/BTCUSDT.csv"
CONFIG = "config/default.yaml"

results = run_pipeline(
    data_path=DATA,
    config_path=CONFIG
)

print("=== Résumé du pipeline ===")
print("Nombre de lignes :", len(results.data))
print("Nombre de features :", len(results.features.columns))
print("Nombre de signaux :", results.signals['signal'].sum())

print("Hash du run :", compute_hash(results.signals))

---
✅ DIAGRAMME UML — VERSION TEXTUELLE ✅ Version simplifiée README

quant_system
│
├── data
│   ├── DataLoader → charge les données
│   └── Preprocessor → nettoie et normalise
│
├── indicators
│   ├── EMA
│   ├── ADX
│   └── Volatility
│
├── structure
│   ├── SwingDetector
│   └── ZigZag
│
├── orderflow
│   ├── Delta
│   ├── Imbalance
│   └── Absorption
│
├── features
│   ├── FeatureBuilder
│   └── Encoders
│
├── signals
│   ├── SignalEngine
│   └── Scoring
│
├── optimization
│   └── ParameterSearch
│
├── attribution
│   └── AttributionEngine
│
├── utils
│   ├── Hashing
│   └── Helpers
│
└── pipeline
    └── Pipeline (run_pipeline)
