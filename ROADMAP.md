# ✅ **ROADMAP v2 — Version claire, ambitieuse, réaliste**

Voici une roadmap parfaitement alignée avec le moteur actuel et la vision long terme.

A intégrer dans `ROADMAP.md`.

---

```markdown
# Roadmap v2 — quant_system

## ✅ 1. Machine Learning (phase préparatoire)
- Sélection des features pertinentes
- Normalisation et encodage avancés
- Construction d’un dataset ML propre
- Ajout d’un module `ml/` :
  - modèles supervisés (RandomForest, XGBoost)
  - modèles séquentiels (LSTM, TCN)
  - validation croisée temporelle
  - feature importance

---

## ✅ 2. Backtesting
- Moteur de simulation simple (OHLC)
- Gestion du risque :
  - stop-loss
  - take-profit
  - sizing
- Métriques :
  - Sharpe
  - Sortino
  - Max Drawdown
  - Winrate
- Visualisation des trades

---

## ✅ 3. Visualisation & Dashboard
- Graphiques matplotlib / plotly
- Heatmaps de signaux
- Visualisation de structure HH/HL/LH/LL
- Dashboard interactif (optionnel)

---

## ✅ 4. Modularisation avancée
- Configuration YAML unifiée
- Modules interchangeables
- Hooks pour ML
- Versioning des signaux

---

## ✅ 5. Documentation & onboarding
- Diagrammes d’architecture
- Tutoriels d’utilisation
- Exemple complet de pipeline
- Guide contributeur

---

## ✅ 6. Intégration continue (CI)
- Tests unitaires
- Linting automatique
- Vérification des signatures SHA256
- Build & tests GitHub Actions

---

## ✅ 7. Préparation v3
- Stratégies algorithmiques complètes
- Optimisation bayésienne
- Exécution temps réel (optionnel)
