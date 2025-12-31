# 🧠 Documentation — Modules Quantitatifs (`modules/quant/`)

Ce document décrit en profondeur les **modules quantitatifs**, cœur analytique avancé du moteur.  
Il complète le README du dossier `modules/quant/` en offrant une vue technique et détaillée.

---

## 🧭 1. Rôle des Modules Quantitatifs

Les modules quantitatifs fournissent :

- des analyses structurelles  
- des signaux avancés  
- des mesures de volatilité  
- des lectures d’orderflow  
- des optimisations  
- des contextes multi‑timeframes  
- des signaux composites  

Ils enrichissent la stratégie et le backtest avec des informations de haut niveau.

---

## 🧱 2. Familles de Modules

## 2.1 Structure de Marché

- `zigzag_mapper.py`  
- `structure_tracker.py`  
- `order_blocks.py`  
- `fvg_detector.py`  

## 2.2 Tendance & Momentum

- `trend_detector.py`  
- `multi_timeframe_convergence.py`  
- `multi_tf_contextualizer.py`  

## 2.3 Volatilité

- `volatility_clustering.py`  

## 2.4 Orderflow

- `orderflow_reader.py`  

## 2.5 Signalisation

- `signal_filter.py`  
- `signal_predictor.py`  
- `signal_attribution.py`  

## 2.6 Optimisation

- `optimizer.py`  
- `order_optimizer.py`  

## 2.7 Pré‑Trade & Simulation

- `pre_trade_simulator.py`  
- `pre_trade_validator.py`  

## 2.8 Radar & Scanning

- `market_radar.py`  
- `scanner_intraday.py`  

---

## 🔧 3. Pipeline des Modules Quantitatifs

1. **Réception des indicateurs**  
2. **Analyse structurelle**  
3. **Analyse dynamique (volatilité, orderflow)**  
4. **Consolidation multi‑timeframes**  
5. **Génération de signaux avancés**  
6. **Attribution & filtrage**  
7. **Transmission à la stratégie**  

---

## 📂 4. Structure du Dossier

Le dossier contient :

- modules individuels  
- utilitaires internes  
- tests associés  
- documentation locale  

---

## 🧪 5. Tests

Les tests doivent vérifier :

- cohérence des signaux  
- stabilité numérique  
- absence de lookahead  
- compatibilité avec les indicateurs  
- reproductibilité  
