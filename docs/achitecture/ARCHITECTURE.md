# # 🧭 Architecture Globale du Projet

Ce document présente la **vision d’ensemble** de l’architecture du projet, en décrivant les couches principales, leurs responsabilités, leurs interactions et les principes qui guident la conception du système.

Il complète `system_flow.md` en offrant une vue plus structurée, plus textuelle et plus conceptuelle.

---

## 🧱 1. Principes d’Architecture

Le projet repose sur plusieurs principes fondamentaux :

## ✔️ Modularité

Chaque composant est isolé dans un dossier dédié :

- `data/`
- `indicators/`
- `modules/quant/`
- `strategy/`
- `backtest/`
- `interface/`
- `interface_pilotage/`

## ✔️ Séparation des responsabilités

Chaque couche a un rôle clair :

- données → indicateurs → modules quantitatifs → stratégie → backtest → exports → interfaces

## ✔️ Extensibilité

L’architecture permet d’ajouter :

- de nouveaux indicateurs  
- de nouveaux modules quantitatifs  
- de nouvelles stratégies  
- de nouvelles interfaces  
- de nouveaux exports  

sans casser l’existant.

## ✔️ Documentation centralisée

Toute la documentation technique vit dans `docs/`.

---

## 🧩 2. Couches du Système

## 2.1 Données (`data/`)

- ingestion  
- nettoyage  
- normalisation  
- validation  
- formats standardisés (OHLCV)

## 2.2 Indicateurs (`indicators/`)

- EMA, RSI, pivots  
- signaux techniques  
- features enrichies  
- transformations mathématiques

## 2.3 Modules Quantitatifs (`modules/quant/`)

- structure de marché  
- volatilité  
- orderflow  
- signaux avancés  
- optimisation  
- pré‑trade  
- radar & scanning  

## 2.4 Stratégie (`strategy/`)

- règles d’entrée/sortie  
- gestion du risque  
- orchestration des signaux  
- logique décisionnelle

## 2.5 Backtest (`backtest/`)

- simulation historique  
- métriques de performance  
- journaux d’exécution  
- validation des stratégies

## 2.6 Exports (`exports/`)

- rapports  
- visuels  
- CSV / JSON  
- audits  
- badges / scoring

## 2.7 Interfaces (`interface/`, `interface_pilotage/`)

- dashboards Streamlit  
- outils de pilotage  
- interfaces audio  
- CLI  
- simulateurs internes  

---

## 🔄 3. Flux d’Information

Le flux suit une direction claire :

Données → Indicateurs → Modules Quant → Stratégie → Backtest → Exports → Interfaces

Chaque couche enrichit la précédente.

---

## 🧬 4. Dépendances

- `indicators/` dépend de `data/`
- `modules/quant/` dépend de `indicators/`
- `strategy/` dépend de `modules/quant/`
- `backtest/` dépend de `strategy/`
- `interface/` dépend de `exports/`

Les dépendances sont **unidirectionnelles**, jamais circulaires.

---

## 🧭 5. Vision Long Terme

L’architecture est conçue pour accueillir :

- du machine learning  
- des modèles prédictifs  
- des stratégies multi‑actifs  
- du trading en temps réel  
- des API brokers  
- des dashboards avancés  
- des modules pédagogiques évolutifs  
