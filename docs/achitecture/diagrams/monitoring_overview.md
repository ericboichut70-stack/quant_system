# 📈 Monitoring Overview — Supervision & Observabilité

Ce document présente une vue d’ensemble du **monitoring** du moteur quantitatif, incluant :

- supervision des modules  
- suivi des performances  
- logs temps réel  
- alertes  
- dashboards de contrôle  

---

## 🔷 1. Monitoring Overview (Mermaid)

```mermaid
flowchart LR

    %% --- Sources ---
    A[📥 Moteur Quantitatif<br/>Pipeline Complet]

    %% --- Monitoring Layer ---
    subgraph MON[📈 Monitoring Layer]
        B1[Collecte de métriques]
        B2[Collecte de logs]
        B3[Analyse temps réel]
        B4[Alertes]
        B5[Dashboards de supervision]
    end

    %% --- Exports ---
    subgraph EXP[📤 Exports]
        C1[CSV]
        C2[JSON]
        C3[Rapports]
        C4[Visuels]
    end

    A --> B1
    A --> B2
    B1 --> B3
    B2 --> B3
    B3 --> B4
    B3 --> B5
    B5 --> EXP

🧱 2. Composants du Monitoring

2.1 Collecte de métriques

rendement

drawdown

Sharpe

latence

stabilité des signaux

2.2 Collecte de logs

logs de stratégie

logs de backtest

logs des modules quantitatifs

logs des interfaces

2.3 Analyse temps réel

détection d’anomalies

suivi des signaux

monitoring des erreurs

2.4 Alertes

seuils critiques

anomalies détectées

erreurs système

2.5 Dashboards

supervision globale

suivi des performances

analyse des logs
