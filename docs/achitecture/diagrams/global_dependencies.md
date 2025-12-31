# 🧬 Global Dependencies — Dépendances Globales du Système

Ce document présente un schéma des **dépendances globales** entre les différentes couches du moteur quantitatif, les modules avancés, les interfaces et les exports.

Il permet de visualiser clairement :

- les dépendances ascendantes  
- les dépendances descendantes  
- les zones critiques  
- les points d’entrée et de sortie  

---

## 🔷 1. Diagramme des Dépendances Globales (Mermaid)

```mermaid
flowchart LR

    %% --- Couches principales ---
    A[data/] --> B[indicators/]
    B --> C[modules/quant/]
    C --> D[strategy/]
    D --> E[backtest/]
    E --> F[exports/]

    %% --- Interfaces ---
    F --> G1[interface/]
    F --> G2[interface_pilotage/]

    %% --- Utils ---
    H[utils/] --> A
    H --> B
    H --> C
    H --> D
    H --> E
    H --> F

    %% --- Documentation ---
    subgraph DOCS[📚 docs/]
        I1[architecture/]
        I2[quant_engine/]
        I3[interfaces/]
        I4[exports/]
        I5[dev_guides/]
        I6[roadmap/]
        I7[reference/]
    end

    A -.-> DOCS
    B -.-> DOCS
    C -.-> DOCS
    D -.-> DOCS
    E -.-> DOCS
    F -.-> DOCS
    G1 -.-> DOCS
    G2 -.-> DOCS
🧱 2. Zones Critiques
data/ → dépendance de toutes les couches

modules/quant/ → dépendance de la stratégie

backtest/ → dépendance des exports

utils/ → dépendance transversale
