# 🧠 Quant System Layers — Couches du Système Quantitatif

Ce document présente une vue hiérarchique des couches du système quantitatif, depuis les données jusqu’aux interfaces.

---

## 🔷 1. Quant System Layers (Mermaid)

```mermaid
flowchart TB

    subgraph L1[📥 Layer 1 — Données]
        A1[Ingestion]
        A2[Nettoyage]
        A3[Normalisation]
    end

    subgraph L2[📊 Layer 2 — Indicateurs]
        B1[Indicateurs Techniques]
        B2[Normalisations]
        B3[Signaux Techniques]
    end

    subgraph L3[🧠 Layer 3 — Modules Quantitatifs]
        C1[Structure]
        C2[Volatilité]
        C3[Orderflow]
        C4[Signaux Avancés]
    end

    subgraph L4[🎯 Layer 4 — Stratégie]
        D1[Filtrage]
        D2[Consolidation]
        D3[Décision]
        D4[Gestion du Risque]
    end

    subgraph L5[📈 Layer 5 — Backtest]
        E1[Simulation]
        E2[Ordres]
        E3[Métriques]
    end

    subgraph L6[📤 Layer 6 — Exports]
        F1[CSV]
        F2[JSON]
        F3[Rapports]
        F4[Visuels]
    end

    subgraph L7[🖥️ Layer 7 — Interfaces]
        G1[Dashboards]
        G2[CLI Tools]
        G3[Interfaces Mentorales]
        G4[Audio Tools]
    end

    L1 --> L2 --> L3 --> L4 --> L5 --> L6 --> L7
