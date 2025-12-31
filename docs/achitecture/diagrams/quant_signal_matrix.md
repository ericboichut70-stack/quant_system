# 🧠 Quant Signal Matrix — Matrice des Signaux Quantitatifs

Ce document présente une **matrice des signaux** produits par les différentes couches du moteur quantitatif.

Elle permet de visualiser :

- quels signaux proviennent de quelles sources  
- comment ils se combinent  
- comment ils alimentent la stratégie  

---

## 🔷 1. Quant Signal Matrix (Mermaid)

```mermaid
flowchart LR

    %% --- Sources ---
    subgraph DATA[📥 Données]
        A1[OHLCV]
        A2[Volume]
        A3[Timeframes]
    end

    %% --- Indicators ---
    subgraph IND[📊 Indicateurs]
        B1[EMA]
        B2[RSI]
        B3[ATR]
        B4[Signaux Techniques]
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
    end

    A1 --> B1 --> C1 --> D1
    A2 --> B2 --> C2 --> D2
    A3 --> B3 --> C3 --> D3
    B4 --> C4 --> D2

🧱 2. Description des Signaux

2.1 Signaux Indicateurs

EMA cross

RSI zones

ATR volatilité

signaux techniques

2.2 Signaux Quantitatifs

structure

swings

volatilité avancée

orderflow

signaux composites

2.3 Signaux Stratégie

signaux filtrés

signaux consolidés

signaux décisionnels
