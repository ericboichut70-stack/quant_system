# 🧹 Data Validation Flow — Flux de Validation des Données

Ce document présente un schéma complet du processus de **validation des données**, depuis l’ingestion jusqu’à leur utilisation dans les indicateurs et modules quantitatifs.

---

## 🔷 1. Data Validation Flow (Mermaid)

```mermaid
flowchart TD

    %% --- Ingestion ---
    A[📥 Ingestion<br/>CSV / API / Temps Réel]

    %% --- Validation Layer ---
    subgraph VAL[🧹 Validation Layer]
        B1[Format Check<br/>colonnes, types]
        B2[Temporal Check<br/>timestamps, ordre]
        B3[Integrity Check<br/>NaN, duplications]
        B4[Range Check<br/>valeurs extrêmes]
        B5[Normalization Check<br/>OHLCV standard]
    end

    %% --- Output ---
    C[📊 Données Validées]

    A --> B1 --> B2 --> B3 --> B4 --> B5 --> C

🧱 2. Étapes Détaillées

2.1 Format Check

colonnes obligatoires

types corrects

formats cohérents

2.2 Temporal Check

timestamps ordonnés

absence de duplications

absence de trous temporels

2.3 Integrity Check

gestion des NaN

vérification des volumes

cohérence OHLC

2.4 Range Check

valeurs plausibles

détection d’anomalies extrêmes

2.5 Normalization Check

colonnes standardisées

index temporel propre

fréquence homogène
