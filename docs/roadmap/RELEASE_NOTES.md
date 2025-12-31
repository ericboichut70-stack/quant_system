# 📝 Release Notes — Notes de Version

Ce document présente les **changements détaillés** introduits à chaque version du projet.  
Il complète `version_history.md` en offrant une vue plus technique, centrée sur les modifications concrètes.

---

## 🔖 Version 1.5.0 — Pré‑Trade & Simulation

***Date : 2025‑06‑15**

### Nouveautés

- ajout de `pre_trade_simulator.py`
- ajout de `pre_trade_validator.py`
- intégration dans la stratégie
- nouveaux tests d’intégration

### Améliorations

- optimisation du pipeline quantitatif
- meilleure gestion des signaux multi‑timeframes
- stabilisation du module de volatilité

### Corrections

- correction d’un bug dans le calcul des pivots UT
- correction d’un problème d’alignement temporel dans les exports

---

## 🔖 Version 1.4.0 — Préparation ML

***Date : 2025‑05‑20**

### Nouveautés 1.4.0

- ajout de hooks pour modèles ML
- normalisation avancée des données
- pipeline multi‑actifs

### Améliorations 1.4.0

- optimisation du backtest
- meilleure gestion des trous temporels

### Corrections 1.4.0

- correction d’un bug dans le module orderflow

---

## 🔖 Version 1.3.0 — Interfaces & Pilotage

***Date : 2025‑04‑01**

### Nouveautés 1.3.0

- enrichissement des dashboards
- ajout d’outils CLI
- intégration des modules narratifs

### Améliorations 1.3.0

- meilleure gestion des exports visuels
- amélioration du scoring interne

---

## 🔖 Version 1.2.0 — Modules Quantitatifs Avancés

***Date : 2025‑03‑05**

### Nouveautés 1.2.0

- ajout de `multi
_tf_contextualizer.py`
- amélioration du module de volatilité
- optimisation du module orderflow

### Corrections 1.2.0

- correction d’un bug dans le calcul des swings

---

## 🔖 Version 1.1.0 — Documentation & Structure

***Date : 2025‑02‑10**

### Nouveautés 1.1.0

- création de la structure complète `docs/`
- ajout des sous‑dossiers architecture / quant_engine / interfaces / exports
- intégration de `documentation_complete.md`

### Améliorations 1.1.0

- ajout des schémas Mermaid
- documentation interne enrichie

---

## 🔖 Version 1.0.0 — Stabilisation Initiale

***Date : 2025‑01‑15**

### Nouveautés 1.0.0

- architecture du moteur consolidée
- pipeline quantitatif complet
- modules quantitatifs stabilisés
- premiers dashboards fonctionnels
