# 📤 Documentation — Formats d’Export (`exports/`)

Ce document décrit les **formats d’export** utilisés dans le projet.  
Il complète le README du dossier `exports/` en offrant une vue technique et détaillée.

---

## 🧭 1. Rôle des Exports

Les exports permettent :

- d’analyser les résultats  
- de partager les rapports  
- d’alimenter les dashboards  
- de conserver des traces  
- de générer des audits  
- de produire des visuels  

Ils constituent la **couche de sortie** du moteur quantitatif.

---

## 📂 2. Formats Supportés

## 2.1 CSV

Utilisé pour :

- signaux  
- données enrichies  
- résultats de backtest  
- optimisation  

Avantages :

- simple  
- compatible Excel  
- léger  

## 2.2 JSON

Utilisé pour :

- exports structurés  
- logs  
- configurations  
- résultats d’analyse  

Avantages :

- flexible  
- lisible  
- compatible API  

## 2.3 Markdown (`.md`)

Utilisé pour :

- rapports  
- audits  
- scoring  
- badges  
- résumés  

Avantages :

- lisible  
- versionnable  
- compatible GitHub  

## 2.4 Images (`.png`, `.jpg`)

Utilisé pour :

- visualisations  
- graphiques  
- heatmaps  
- courbes d’équité  

## 2.5 Dossiers spécialisés

- `visuals/`  
- `bot_registry_*`  
- `mentor_validations/`  

---

## 🔧 3. Conventions de Nommage

- `YYYY-MM-DD_report.md`  
- `signals_<asset>_<period>.csv`  
- `optimization_results.csv`  
- `equity_curve.png`  

---

## 🧪 4. Tests

Les tests doivent vérifier :

- la validité des formats  
- la cohérence des données exportées  
- la compatibilité avec les dashboards  
- l’absence de corruption  
