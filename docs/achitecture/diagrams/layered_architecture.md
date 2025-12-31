# 🧱 Layered Architecture — Architecture en Couches

Ce diagramme présente une vue en couches du moteur quantitatif.

```mermaid
flowchart TB

    subgraph L1[Couche Données]
        A[data/]
    end

    subgraph L2[Couche Indicateurs]
        B[indicators/]
    end

    subgraph L3[Modules Quantitatifs]
        C[modules/quant/]
    end

    subgraph L4[Stratégie]
        D[strategy/]
    end

    subgraph L5[Backtest]
        E[backtest/]
    end

    subgraph L6[Exports]
        F[exports/]
    end

    subgraph L7[Interfaces]
        G[interface/]
        H[interface_pilotage/]
    end

    A --> B --> C --> D --> E --> F --> G
    F --> H
