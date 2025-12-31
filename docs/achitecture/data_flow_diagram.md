# 🔄 Data Flow Diagram — Flux de Données

Ce document décrit le **flux complet des données** dans le moteur quantitatif, depuis les sources brutes jusqu’aux exports finaux.

Il complète `system_flow.md` en se concentrant exclusivement sur la **circulation des données**.

---

## 🧭 1. Vue Globale du Flux de Données

Sources → data/ → indicators/ → modules/quant/ → strategy/ → backtest/ → exports/

Chaque étape enrichit ou transforme les données.

---

## 🔷 2. Diagramme de Flux (Mermaid)

```mermaid
flowchart TD

    A[📥 Sources de données<br/>CSV / API / Flux] --> B[🧹 data/<br/>Nettoyage & Normalisation]

    B --> C[📊 indicators/<br/>Calcul des indicateurs]
    C --> D[🧠 modules/quant/<br/>Analyses avancées]
    D --> E[🎯 strategy/<br/>Décisions & Signaux]
    E --> F[📈 backtest/<br/>Simulation historique]
    F --> G[📤 exports/<br/>Rapports & Visuels]

🧱 3. Étapes Détaillées

3.1 Sources

CSV

API (yfinance, brokers)

flux temps réel

3.2 data/

nettoyage

normalisation

validation

alignement temporel

3.3 indicators/

EMA, RSI, ATR

signaux techniques

features enrichies

3.4 modules/quant/

structure

volatilité

orderflow

signaux avancés

3.5 strategy/

règles d’entrée

règles de sortie

gestion du risque

3.6 backtest/

exécution des ordres

métriques

journaux

3.7 exports/

CSV

JSON

rapports Markdown

visuels
