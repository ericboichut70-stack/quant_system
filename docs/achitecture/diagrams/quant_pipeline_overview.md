# 🧠 Quant Pipeline Overview — Vue d’Ensemble du Pipeline Quantitatif

Ce document présente une vue synthétique du **pipeline quantitatif complet**, depuis les données brutes jusqu’aux exports finaux.

---

## 🔷 1. Quant Pipeline Overview (Mermaid)

```mermaid
flowchart TB

    %% --- Data Layer ---
    subgraph DATA[📥 Données]
        A1[Ingestion]
        A2[Nettoyage]
        A3[Normalisation]
    end

    %% --- Indicators ---
    subgraph IND[📊 Indicateurs]
        B1[Indicateurs Techniques]
        B2[Normalisations]
        B3[Signaux Techniques]
    end

    %% --- Quant Modules ---
    subgraph QUANT[🧠 Modules Quantitatifs]
        C1[Structure]
        C2[Volatilité]
        C3[Orderflow]
        C4[Signaux Avancés]
    end

    %% --- Strategy ---
    subgraph STRAT[🎯 Stratégie]
        D1[Filtrage]
        D2[Consolidation]
        D3[Décision]
        D4[Gestion du Risque]
    end

    %% --- Backtest ---
    subgraph BACK[📈 Backtest]
        E1[Simulation]
        E2[Ordres]
        E3[Métriques]
    end

    %% --- Exports ---
    subgraph EXP[📤 Exports]
        F1[CSV]
        F2[JSON]
        F3[Rapports]
        F4[Visuels]
    end

    DATA --> IND --> QUANT --> STRAT --> BACK --> EXP

🧱 2. Description des Étapes

Données
ingestion

nettoyage

normalisation

Indicateurs
EMA, RSI, ATR

signaux techniques

Modules Quantitatifs
structure

volatilité

orderflow

signaux avancés

Stratégie
filtrage

décision

gestion du risque

Backtest
simulation

ordres

métriques

Exports
CSV

JSON

rapports

visuels
