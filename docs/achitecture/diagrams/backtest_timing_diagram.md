# ⏱️ Backtest Timing Diagram — Diagramme de Timing du Backtest

Ce document présente un **diagramme temporel** du backtest, montrant l’ordre exact des opérations à chaque bougie.

---

## 🔷 1. Backtest Timing Diagram (Mermaid)

```mermaid
sequenceDiagram
    participant T as Time (Bougie)
    participant D as Data
    participant I as Indicators
    participant Q as Quant Modules
    participant S as Strategy
    participant O as Order Simulator
    participant M as Metrics

    T->>D: Charger OHLCV
    D->>I: Calcul des indicateurs
    I->>Q: Features enrichies
    Q->>S: Signaux avancés
    S->>O: Ordres potentiels
    O->>S: Exécution / Rejet
    O->>M: Mise à jour des métriques
    M->>T: Fin de la bougie

🧱 2. Étapes Détaillées

2.1 Chargement des données

OHLCV

volumes

timeframes

2.2 Calcul des indicateurs

EMA, RSI, ATR

signaux techniques

2.3 Modules quantitatifs

structure

volatilité

orderflow

2.4 Stratégie

filtrage

décision

gestion du risque

2.5 Simulation d’ordres

slippage

spread

frais

2.6 Mise à jour des métriques

rendement

drawdown

Sharpe
