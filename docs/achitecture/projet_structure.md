# 🧱 Structure du Projet — Vue Architecture

Ce document présente la **structure complète du projet**, vue sous l’angle architectural.  
Il complète `folder_structure.md` en offrant une vision plus conceptuelle et plus orientée système.

---

## 🧭 1. Vue d’Ensemble

Le projet est organisé en **couches fonctionnelles**, chacune ayant une responsabilité claire :

Données → Indicateurs → Modules Quant → Stratégie → Backtest → Exports → Interfaces

Code

Chaque couche est isolée dans un dossier dédié.

---

## 🧱 2. Structure Logique

## 2.1 Couche Données (`data/`)

- ingestion  
- nettoyage  
- normalisation  
- validation  

## 2.2 Couche Indicateurs (`indicators/`)

- EMA, RSI, ATR  
- signaux techniques  
- features enrichies  

## 2.3 Couche Modules Quantitatifs (`modules/quant/`)

- structure de marché  
- volatilité  
- orderflow  
- signaux avancés  
- optimisation  

## 2.4 Couche Stratégie (`strategy/`)

- règles d’entrée  
- règles de sortie  
- gestion du risque  

## 2.5 Couche Backtest (`backtest/`)

- simulation historique  
- métriques  
- journaux  

## 2.6 Couche Exports (`exports/`)

- rapports  
- visuels  
- CSV / JSON  

## 2.7 Couche Interfaces (`interface/`, `interface_pilotage/`)

- dashboards  
- outils CLI  
- interfaces mentorales  

---

## 🧬 3. Structure Physique (Arborescence)

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

---

## 🧭 4. Principes d’Architecture

- modularité  
- séparation des responsabilités  
- extensibilité  
- documentation centralisée  
- absence de dépendances circulaires  
