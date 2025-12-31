# 🌐 System Context — Contexte Système

Ce diagramme présente une vue **macro** du système, montrant ses interactions avec les sources externes, les utilisateurs, les interfaces et les exports.

---

## 🔷 1. Diagramme de Contexte (Mermaid)

```mermaid
flowchart LR

    subgraph EXT[🌍 Sources Externes]
        A1[API Market Data]
        A2[CSV / JSON]
        A3[Flux Temps Réel]
    end

    subgraph CORE[🧠 Moteur Quantitatif]
        B1[data/]
        B2[indicators/]
        B3[modules/quant/]
        B4[strategy/]
        B5[backtest/]
        B6[exports/]
    end

    subgraph UI[🖥️ Interfaces]
        C1[Dashboards]
        C2[CLI Tools]
        C3[Interfaces Mentorales]
        C4[Audio Tools]
    end

    A1 --> B1
    A2 --> B1
    A3 --> B1

    B6 --> C1
    B6 --> C2
    B6 --> C3
    B6 --> C4

    C1 -->|Interaction| CORE
    C2 -->|Pilotage| CORE
    C3 -->|Validation| CORE
    C4 -->|Narration| CORE

🧱 2. Description des Zones

2.1 Sources Externes

données marché

fichiers locaux

flux temps réel

2.2 Moteur Quantitatif

pipeline complet

analyses avancées

stratégie

backtest

exports

2.3 Interfaces

dashboards

outils CLI

interfaces mentorales

outils audio
