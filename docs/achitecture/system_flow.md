# 🧭 System Flow — Architecture Globale du Projet

Ce document présente la **vue d’ensemble du système**, depuis les données brutes jusqu’aux interfaces utilisateur, en passant par le moteur quantitatif, les modules avancés et les exports.

Il sert de **référence visuelle** pour comprendre comment toutes les couches du projet interagissent.

---

## 🔷 Vue Globale (Mermaid)

```mermaid
flowchart TD

    %% --- Sources de données ---
    A[📥 Données brutes<br/>CSV / API / Flux] --> B[🧹 data/<br/>Ingestion & Nettoyage]

    %% --- Indicateurs ---
    B --> C[📊 indicators/<br/>Indicateurs techniques]

    %% --- Modules quantitatifs ---
    C --> D[🧠 modules/quant/<br/>Analyses avancées<br/>Structure / Volatilité / Orderflow]

    %% --- Stratégie ---
    D --> E[🎯 strategy/<br/>Règles d'entrée/sortie]

    %% --- Backtest ---
    E --> F[📈 backtest/<br/>Simulation & Performance]

    %% --- Exports ---
    F --> G[📤 exports/<br/>Rapports / Visuels / CSV]

    %% --- Interfaces ---
    G --> H[🖥️ interface/<br/>Dashboards principaux]
    G --> I[⚙️ interface_pilotage/<br/>Pilotage & Outils avancés]

    %% --- Documentation ---
    subgraph DOCS[📚 Documentation]
        J1[architecture/<br/>Schémas & UML]
        J2[quant_engine/<br/>Documentation moteur]
        J3[interfaces/<br/>Docs dashboards & CLI]
        J4[exports/<br/>Formats & usages]
        J5[dev_guides/<br/>Conventions & contribution]
        J6[roadmap/<br/>Vision & versions]
        J7[reference/<br/>documentation_complete.md]
    end

    %% --- Liens documentation ---
    B -.-> DOCS
    C -.-> DOCS
    D -.-> DOCS
    E -.-> DOCS
    F -.-> DOCS
    H -.-> DOCS
    I -.-> DOCS

📘 system_flow.md

🧩 Description des Couches

1. Données (data/)

ingestion

nettoyage

normalisation

validation

2. Indicateurs (indicators/)

EMA, RSI, pivots

signaux techniques

features enrichies

3. Modules quantitatifs (modules/quant/)

structure de marché

volatilité

orderflow

signaux avancés

optimisation

4. Stratégie (strategy/)

règles d’entrée/sortie

gestion du risque

orchestration des signaux

5. Backtest (backtest/)

simulation historique

métriques de performance

journaux d’exécution

6. Exports (exports/)

rapports

visuels

CSV / JSON

audits

7. Interfaces (interface/, interface_pilotage/)

dashboards Streamlit

outils de pilotage

interfaces audio

CLI

8. Documentation (docs/)

architecture

moteur quantitatif

interfaces

exports

guides développeurs

roadmap

référence complète

🎯 Objectif du Schéma

Ce schéma permet :

de comprendre la circulation de l’information

de visualiser les dépendances

de clarifier les couches du système

d’aider les contributeurs à naviguer

de servir de référence stable pour l’évolution du projet
