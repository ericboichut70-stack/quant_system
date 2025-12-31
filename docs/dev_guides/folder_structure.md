# 🗂️ Folder Structure — Structure des Dossiers

Ce document décrit la **structure complète du projet**, son organisation interne, et les responsabilités de chaque dossier.  
Il sert de référence pour les contributeurs, les auditeurs et les futurs développeurs.

---

## 🧭 1. Vue d’Ensemble

project_root/
│
├── data/
├── indicators/
├── modules/
│   └── quant/
├── strategy/
├── backtest/
├── interface/
├── interface_pilotage/
├── exports/
├── utils/
├── tests/
├── scripts/
├── docs/
│   ├── architecture/
│   ├── quant_engine/
│   ├── interfaces/
│   ├── exports/
│   ├── dev_guides/
│   ├── roadmap/
│   └── reference/
└── documentation_md/

Chaque dossier a une responsabilité claire et ne doit jamais en assumer plusieurs.

---

## 🧱 2. Description des Dossiers

## 2.1 `data/`

- ingestion  
- nettoyage  
- normalisation  
- validation  
- formats OHLCV  

## 2.2 `indicators/`

- EMA, RSI, ATR  
- signaux techniques  
- features enrichies  

## 2.3 `modules/`

- modules avancés  
- scoring, progression, narration  
- simulateurs internes  

## 2.4 `modules/quant/`

- structure de marché  
- volatilité  
- orderflow  
- signaux avancés  
- optimisation  

## 2.5 `strategy/`

- règles d’entrée/sortie  
- gestion du risque  
- logique décisionnelle  

## 2.6 `backtest/`

- simulation historique  
- métriques  
- journaux  

## 2.7 `interface/`

- dashboards principaux  
- visualisations  
- analyses interactives  

## 2.8 `interface_pilotage/`

- dashboards avancés  
- outils CLI  
- interfaces mentorales  
- modules narratifs  

## 2.9 `exports/`

- rapports  
- visuels  
- CSV / JSON  
- audits  

## 2.10 `utils/`

- helpers transverses  
- fonctions génériques  

## 2.11 `tests/`

- tests unitaires  
- tests fonctionnels  

## 2.12 `scripts/`

- scripts utilitaires  
- automatisations ponctuelles  

## 2.13 `docs/`

- documentation technique  
- architecture  
- moteur quantitatif  
- interfaces  
- exports  
- guides développeurs  
- roadmap  
- référence complète  

## 2.14 `documentation_md/`

- rituels internes  
- scripts documentaires  
- annexes  
- cosmogrammes  

---

## 🧬 3. Principes d’Organisation

- **une responsabilité par dossier**  
- **pas de duplication**  
- **pas de dépendances circulaires**  
- **documentation centralisée dans `docs/`**  
- **rituels internes dans `documentation_md/`**  
