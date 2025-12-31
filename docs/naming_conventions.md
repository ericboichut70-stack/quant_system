# 🏷️ Naming Conventions — Conventions de Nommage

Ce document définit les **règles de nommage** utilisées dans tout le projet.  
Il garantit la cohérence, la lisibilité et la maintenabilité du code et des fichiers.

---

## 🧭 1. Principes Généraux

- cohérence avant tout  
- noms explicites  
- éviter les abréviations obscures  
- respecter les conventions Python  
- un nom = une responsabilité  

---

## 🧱 2. Nommage des Fichiers

## 2.1 Fichiers Python

Format : `snake_case.py`

Exemples :

- `data_loader.py`
- `trend_detector.py`
- `backtest_engine.py`

## 2.2 Dossiers

Format : `snake_case/`

Exemples :

- `modules/quant/`
- `interface_pilotage/`

## 2.3 Documentation

Format : `kebab-case.md` ou `snake_case.md`

Exemples :

- `system_flow.md`
- `coding_standards.md`
- `usage-guidelines.md`

---

## 🧩 3. Nommage des Fonctions

Format : `snake_case`

Exemples :

- `compute_signal()`
- `calculate_volatility()`
- `generate_report()`

Règles :

- verbe + complément  
- pas de majuscules  
- pas d’abréviations  

---

## 🧬 4. Nommage des Classes

Format : `CamelCase`

Exemples :

- `BacktestEngine`
- `TrendDetector`
- `OrderflowReader`

Règles :

- nom explicite  
- une classe = un concept  

---

## 🔧 5. Nommage des Variables

Format : `snake_case`

Exemples :

- `entry_price`
- `stop_loss_pct`
- `signal_strength`

Règles :

- éviter les noms trop courts (`x`, `df2`, `tmp`)  
- éviter les noms trop longs  

---

## 📊 6. Nommage des Constantes

Format : `UPPER_SNAKE_CASE`

Exemples :

- `DEFAULT_EMA_LENGTH = 114`
- `MAX_POSITIONS = 3`

---

## 🧪 7. Nommage des Tests

Format : `test_<comportement>.py`

Exemples :

- `test_signal_generation.py`
- `test_backtest_engine.py`
