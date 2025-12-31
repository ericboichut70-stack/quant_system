# 🌐 Quant Ecosystem Map — Écosystème Quantitatif Global

Ce document présente une vue d’ensemble de l’écosystème quantitatif complet, incluant :

- moteur interne  
- modules avancés  
- interfaces  
- exports  
- documentation  
- extensions futures  

---

## 🔷 1. Quant Ecosystem Map (Mermaid)

```mermaid
flowchart TB

    %% --- Core Engine ---
    subgraph CORE[🧠 Moteur Quantitatif]
        A1[data/]
        A2[indicators/]
        A3[modules/quant/]
        A4[strategy/]
        A5[backtest/]
        A6[exports/]
    end

    %% --- Interfaces ---
    subgraph UI[🖥️ Interfaces]
        B1[Dashboards]
        B2[CLI Tools]
        B3[Interfaces Mentorales]
        B4[Audio Tools]
    end

    %% --- Extensions ---
    subgraph EXT[🔮 Extensions Futures]
        C1[Machine Learning]
        C2[Trading Temps Réel]
        C3[Optimisation Avancée]
        C4[Multi‑Actifs]
    end

    %% --- Documentation ---
    subgraph DOCS[📚 Documentation]
        D1[Architecture]
        D2[Quant Engine]
        D3[Interfaces]
        D4[Exports]
        D5[Dev Guides]
        D6[Roadmap]
        D7[Reference]
    end

    %% --- Flows ---
    CORE --> UI
    CORE --> EXT
    CORE -.-> DOCS
    UI -.-> DOCS
    EXT -.-> DOCS

🧱 2. Description des Zones

2.1 Moteur Quantitatif

Le cœur du système, pipeline complet.

2.2 Interfaces

Accès utilisateur, visualisation, pilotage.

2.3 Extensions Futures

ML, temps réel, optimisation intelligente.

2.4 Documentation

Source d’autorité technique.
