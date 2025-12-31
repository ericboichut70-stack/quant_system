# 🧠 Quant Context Layers — Couches de Contexte Quantitatif

Ce document présente une vue structurée des **couches de contexte** utilisées par le moteur quantitatif pour analyser le marché.  
Il met en évidence la hiérarchie des signaux, des contextes et des modules.

---

## 🔷 1. Quant Context Layers (Mermaid)

```mermaid
flowchart TB

    %% --- Base Layer ---
    subgraph L1[📥 Layer 1 — Données Brutes]
        A1[OHLCV]
        A2[Volume]
        A3[Timeframes]
    end

    %% --- Indicators Layer ---
    subgraph L2[📊 Layer 2 — Indicateurs]
        B1[EMA / SMA]
        B2[RSI / ATR]
        B3[Normalisations]
        B4[Signaux Techniques]
    end

    %% --- Quant Modules Layer ---
    subgraph L3[🧠 Layer 3 — Modules Quantitatifs]
        C1[Structure]
        C2[Volatilité]
        C3[Orderflow]
        C4[Signaux Avancés]
    end

    %% --- Strategy Context Layer ---
    subgraph L4[🎯 Layer 4 — Contexte Stratégique]
        D1[Filtrage]
        D2[Consolidation]
        D3[Décision]
        D4[Gestion du Risque]
    end

    %% --- Execution Layer ---
    subgraph L5[⚙️ Layer 5 — Exécution]
        E1[Ordres]
        E2[Simulation / Backtest]
    end

    A1 --> B1 --> C1 --> D1 --> E1
    A2 --> B2 --> C2 --> D2 --> E2
    A3 --> B3 --> C3 --> D3
    B4 --> C4 --> D4

🧱 2. Description des Couches

Layer 1 — Données Brutes

OHLCV

volumes

timeframes

Layer 2 — Indicateurs

signaux techniques

normalisations

dérivées

Layer 3 — Modules Quantitatifs

structure

volatilité

orderflow

signaux avancés

Layer 4 — Contexte Stratégique

filtrage

consolidation

décision

gestion du risque

Layer 5 — Exécution

ordres

simulation

métriques
