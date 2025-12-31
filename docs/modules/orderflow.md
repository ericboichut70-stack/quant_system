# 📦 Module 5 — orderflow/

1 Description générale

Le module orderflow/ analyse la microstructure du marché à partir des données disponibles. Même si tu ne travailles pas avec des données tick ou des carnets d’ordres complets, tu as construit un module d’orderflow adapté aux données OHLCV, permettant d’extraire :

le delta (agressivité acheteurs vs vendeurs)

l’imbalance (déséquilibre directionnel)

l’absorption (résistance à la pression)

des signaux de microstructure simplifiés mais robustes

Ce module enrichit fortement les features et les signaux, en ajoutant une dimension comportementale au prix.

2 Responsabilités du module

Le module orderflow/ doit :

dériver des mesures d’orderflow à partir d’OHLCV

produire des séries propres, alignées sur les données

lisser ou normaliser les signaux si nécessaire

fournir des primitives réutilisables dans les features et signaux

Il ne doit pas :

générer des signaux finaux

interpréter la structure de marché

faire du clustering

produire des features complexes

👉 C’est un module d’analyse microstructurelle.

3 Entrées / sorties

Entrées
un DataFrame OHLCV propre

paramètres optionnels :

fenêtre de calcul

normalisation

seuils d’imbalance

Sorties
Un DataFrame contenant :

delta

imbalance

absorption

éventuellement des dérivés (delta_norm, imbalance_smooth, etc.)

4 Classes / fonctions principales

## Delta

Mesure l’agressivité acheteurs vs vendeurs.

Méthodes typiques :

compute(data) → renvoie une série delta

Interprétation :

delta > 0 → pression acheteuse

delta < 0 → pression vendeuse

### Imbalance

Mesure le déséquilibre directionnel.

Méthodes typiques :

compute(data) → renvoie une série d’imbalance

Utilisation :

détection de ruptures

confirmation de tendance

filtrage des faux signaux

### Absorption

Mesure la capacité du marché à absorber la pression.

Méthodes typiques :

compute(data) → renvoie une série d’absorption

Utilisation :

détection de zones de résistance

signaux de retournement

validation de swings

5 Exemple d’utilisation

from quant_system.orderflow.delta import Delta
from quant_system.orderflow.imbalance import Imbalance
from quant_system.orderflow.absorption import Absorption

df["delta"] = Delta.compute(df)
df["imbalance"] = Imbalance.compute(df)
df["absorption"] = Absorption.compute(df)

print(df[["delta", "imbalance", "absorption"]].tail())

6 Dépendances internes

Le module orderflow/ dépend uniquement de :

pandas

numpy

Il peut utiliser :

les indicateurs (EMA, volatilité) pour normaliser

la structure (swings) pour contextualiser

Mais il ne doit jamais dépendre :

des features

des signaux

du pipeline

👉 Le flux doit rester data → indicators → structure → orderflow → features → signals.

7 Points d’extension (v2 / v3)

v2
delta cumulé

imbalance multi‑horizons

absorption relative à la volatilité

normalisation adaptative

v3
microstructure avancée :

volume profile

footprint simplifié

zones d’absorption dynamiques

orderflow multi‑actifs

orderflow ML‑based
