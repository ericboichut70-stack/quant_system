# 🗺️ Full System Map — Vue Globale Ultime

Ce diagramme présente une **vue holistique** du système, combinant :

- flux de données  
- flux de signaux  
- interactions modules ↔ interfaces  
- exports  
- documentation  

C’est la carte maîtresse du projet.

---

## 🔷 1. Full System Map (Mermaid)

```mermaid
flowchart TB

    %% --- Sources ---
    subgraph SRC[🌍 Sources Externes]
        A1[API Market Data]
        A2[CSV / JSON]
        A3[Flux Temps Réel]
    end

    %% --- Data Layer ---
    subgraph DATA[📥 data/]
        B1[Ingestion]
        B2[Nettoyage]
        B3[Normalisation]
        B4[Validation]
    end

    %% --- Indicators ---
    subgraph IND[📊 indicators/]
        C1[Indicateurs de Base]
        C2[Indicateurs Avancés]
        C3[Signaux Techniques]
    end

    %% --- Quant Modules ---
    subgraph QUANT[🧠 modules/quant/]
        D1[Structure]
        D2[Volatilité]
        D3[Orderflow]
        D4[Signaux Avancés]
        D5[Optimisation]
    end

    %% --- Strategy ---
    subgraph STRAT[🎯 strategy/]
        E1[Filtrage]
        E2[Décision]
        E3[Gestion du Risque]
        E4[Position Sizing]
    end

    %% --- Backtest ---
    subgraph BACK[📈 backtest/]
        F1[Simulation]
        F2[Trade Log]
        F3[Métriques]
    end

    %% --- Exports ---
    subgraph EXP[📤 exports/]
        G1[CSV]
        G2[JSON]
        G3[Rapports]
        G4[Visuels]
        G5[Logs]
    end

    %% --- Interfaces ---
    subgraph UI[🖥️ Interfaces]
        H1[Dashboards]
        H2[CLI Tools]
        H3[Interfaces Mentorales]
        H4[Audio Tools]
    end

    %% --- Documentation ---
    subgraph DOCS[📚 Documentation]
        I1[Architecture]
        I2[Quant Engine]
        I3[Interfaces]
        I4[Exports]
        I5[Dev Guides]
        I6[Roadmap]
        I7[Reference]
    end

    %% --- Flows ---
    SRC --> DATA
    DATA --> IND
    IND --> QUANT
    QUANT --> STRAT
    STRAT --> BACK
    BACK --> EXP
    EXP --> UI

    DATA -.-> DOCS
    IND -.-> DOCS
    QUANT -.-> DOCS
    STRAT -.-> DOCS
    BACK -.-> DOCS
    EXP -.-> DOCS
    UI -.-> DOCS
