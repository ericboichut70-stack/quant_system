# 🖥️ Interface System Map — Carte du Système d’Interfaces

Ce document présente une vue globale des **interfaces** du projet, incluant :

- dashboards  
- outils CLI  
- interfaces mentorales  
- outils audio  
- interactions avec les exports et le moteur  

---

## 🔷 1. Interface System Map (Mermaid)

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

    %% --- User Layer ---
    subgraph USER[👤 Utilisateur]
        C1[Analyse]
        C2[Pilotage]
        C3[Apprentissage]
        C4[Narration]
    end

    %% --- Flows ---
    CORE --> UI
    UI --> USER

    USER -.-> UI
    UI -.-> CORE

🧱 2. Description des Zones

Interfaces
dashboards Streamlit

outils CLI

interfaces mentorales

outils audio

Utilisateur
analyse des signaux

pilotage du système

apprentissage

narration
