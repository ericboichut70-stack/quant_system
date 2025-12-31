# 🎯 Strategy Flow (Advanced) — Flux Avancé de la Stratégie

Ce document présente un schéma avancé du fonctionnement interne de la stratégie, incluant :

- filtrage  
- décision  
- gestion du risque  
- sizing  
- signaux ML (optionnel)  
- intégration modules quantitatifs  

---

## 🔷 1. Strategy Flow (Advanced) — Mermaid

```mermaid
flowchart TD

    %% --- Inputs ---
    A1[📊 Signaux Indicateurs]
    A2[🧠 Signaux Modules Quant]
    A3[🤖 Signaux ML (optionnel)]

    %% --- Strategy Engine ---
    subgraph STRAT[🎯 Strategy Engine]
        B1[Filtrage des Signaux]
        B2[Consolidation]
        B3[Décision]
        B4[Gestion du Risque]
        B5[Position Sizing]
    end

    %% --- Output ---
    C[📝 Ordres]

    A1 --> B1
    A2 --> B1
    A3 --> B1

    B1 --> B2 --> B3 --> B4 --> B5 --> C

🧱 2. Étapes Détaillées

2.1 Filtrage

élimination des signaux faibles

vérification du contexte

validation multi‑timeframes

2.2 Consolidation

fusion des signaux

pondération

attribution

2.3 Décision

entrée / sortie

maintien de position

annulation

2.4 Gestion du Risque

stop loss

take profit

trailing stop

2.5 Position Sizing

taille optimale

gestion du capital

limites de risque
