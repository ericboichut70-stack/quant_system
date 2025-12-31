# 🧩 UML Overview — Vue Modélisée du Système

Ce document présente une **vue UML modernisée** du moteur quantitatif et de ses interactions.  
Il sert de support visuel pour comprendre les relations entre les composants.

---

## 🔷 1. Diagramme UML — Vue de Classe (Mermaid)

```mermaid
classDiagram

    class DataLoader {
        +load()
        +clean()
        +normalize()
        +validate()
    }

    class Indicators {
        +compute_basic()
        +compute_advanced()
        +generate_signals()
    }

    class QuantModule {
        +analyze_structure()
        +analyze_volatility()
        +read_orderflow()
        +optimize()
    }

    class Strategy {
        +generate_entries()
        +generate_exits()
        +risk_management()
    }

    class BacktestEngine {
        +run()
        +simulate_orders()
        +compute_metrics()
    }

    class Exports {
        +save_csv()
        +save_json()
        +generate_reports()
    }

    class Dashboard {
        +visualize()
        +interact()
    }

    DataLoader --> Indicators
    Indicators --> QuantModule
    QuantModule --> Strategy
    Strategy --> BacktestEngine
    BacktestEngine --> Exports
    Exports --> Dashboard

🔷 2. Diagramme UML — Vue de Séquence

sequenceDiagram
    participant D as DataLoader
    participant I as Indicators
    participant Q as QuantModule
    participant S as Strategy
    participant B as BacktestEngine
    participant E as Exports

    D->>I: Données nettoyées
    I->>Q: Features enrichies
    Q->>S: Signaux avancés
    S->>B: Ordres & règles
    B->>E: Résultats & métriques

🔷 3. Diagramme UML — Vue de Composants

flowchart LR

    subgraph DATA[Data Layer]
        A[DataLoader]
    end

    subgraph IND[Indicators]
        B[Indicators Engine]
    end

    subgraph QUANT[Quant Modules]
        C[Structure]
        D[Volatility]
        E[Orderflow]
        F[Optimization]
    end

    subgraph STRAT[Strategy]
        G[Decision Engine]
    end

    subgraph BACKTEST[Backtest]
        H[Simulation Engine]
    end

    subgraph EXPORTS[Exports]
        I[Reports]
        J[CSV/JSON]
    end

    subgraph UI[Interfaces]
        K[Dashboards]
        L[Pilotage Tools]
    end

    A --> B
    B --> C
    B --> D
    B --> E
    C --> G
    D --> G
    E --> G
    G --> H
    H --> I
    H --> J
    I --> K
    J --> L
