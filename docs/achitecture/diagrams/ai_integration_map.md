# 🤖 AI Integration Map — Intégration de l’IA dans le Système

Ce document présente une vue claire de la manière dont l’IA peut s’intégrer dans le moteur quantitatif, en respectant l’architecture existante.

Il ne s’agit pas d’une implémentation, mais d’une **carte conceptuelle**.

---

## 🔷 1. AI Integration Map (Mermaid)

```mermaid
flowchart TB

    %% --- Data Layer ---
    A[data/] --> B[indicators/]

    %% --- Indicators to ML ---
    B --> C1[ML Feature Engineering]

    %% --- ML Models ---
    subgraph ML[🧠 Machine Learning Layer]
        C1
        C2[Model Training]
        C3[Model Validation]
        C4[Model Inference]
    end

    C4 --> D[modules/quant/]

    %% --- Strategy ---
    D --> E[strategy/]

    %% --- Backtest ---
    E --> F[backtest/]

    %% --- Exports ---
    F --> G[exports/]

    %% --- Interfaces ---
    G --> H1[Dashboards]
    G --> H2[CLI Tools]
    G --> H3[Audio Tools]

🧱 2. Points d’Intégration Potentiels

2.1 Feature Engineering

enrichissement des indicateurs

extraction de patterns

normalisation avancée

2.2 Modèles ML

classification (buy/sell/hold)

régression (target future price)

clustering (régimes de marché)

2.3 Inference Layer

signaux ML → modules quantitatifs

signaux ML → stratégie

🧬 3. Contraintes Architecturales

pas de dépendance circulaire

ML doit rester modulaire

ML ne remplace pas les modules quantitatifs

ML doit être testable et explicable
