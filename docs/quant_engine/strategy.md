# 🎯 Documentation — Couche Stratégie (`strategy/`)

Ce document décrit la couche **stratégie**, cœur décisionnel du moteur quantitatif.

---

## 🧭 1. Rôle de la Stratégie

La stratégie transforme les signaux en **décisions de trading** :

- entrées  
- sorties  
- gestion du risque  
- sizing  
- filtres de marché  

Elle orchestre les signaux issus :

- des indicateurs  
- des modules quantitatifs  
- des analyses structurelles  

---

## 🧱 2. Pipeline Stratégique

1. **Réception des signaux**
2. **Filtrage**
3. **Décision**
4. **Gestion du risque**
5. **Génération d’ordres**
6. **Transmission au backtest**

---

## 🔧 3. Structure du Dossier

- `strategy_core.py`  
- `risk_management.py`  
- `filters.py`  
- `decision_engine.py`  

---

## 🧪 4. Tests

Les tests doivent vérifier :

- absence de lookahead  
- cohérence des règles  
- stabilité des décisions  
- compatibilité avec les modules quantitatifs
