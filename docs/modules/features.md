# 📦 Module 6 — features/

1 Description générale

Le module features/ est l’un des piliers centraux de ton moteur quantitatif.
Il a pour rôle de transformer :

les données brutes (OHLCV)

les indicateurs

la structure de marché

l’orderflow

… en un ensemble cohérent de features exploitables, destinées à :

la génération de signaux

l’analyse statistique

l’optimisation

les modèles de machine learning (v2)

Ce module est conçu pour être modulaire, extensible, et strictement déterministe, garantissant une reproductibilité parfaite.

2 Responsabilités du module

Le module features/ doit :

agréger les données provenant des modules précédents

construire des features multi‑niveaux (tendance, structure, volatilité, orderflow…)

normaliser ou standardiser certaines colonnes

encoder des informations temporelles si nécessaire

renvoyer une matrice de features propre, alignée, prête à être utilisée

Il ne doit pas :

générer des signaux

faire de l’optimisation

interpréter les features

faire du ML (ce sera dans ml/ en v2)

👉 C’est un module de transformation, pas d’interprétation.

3 Entrées / sorties

Entrées
DataFrame contenant :

OHLCV

indicateurs

structure

orderflow

paramètres optionnels :

normalisation

sélection de features

encodage temporel

Sorties
Un DataFrame contenant :

toutes les features construites

index temporel propre

colonnes normalisées si nécessaire

aucune fuite de données (pas de lookahead)

4 Classes / fonctions principales

## FeatureBuilder

Cœur du module : construit les features à partir des données enrichies.

Méthodes typiques :

build(data, indicators, structure, orderflow)  
→ renvoie un DataFrame de features

Exemples de features :

pente EMA

ADX normalisé

swings encodés

delta normalisé

imbalance smoothed

volatilité relative

ratio high/low

returns log

### Encoders

Encode des informations supplémentaires.

Méthodes typiques :

encode_time(data)  
→ encode heure, jour, semaine, etc.

normalize(data)  
→ normalisation min‑max ou z‑score

5 Exemple d’utilisation

from quant_system.features.feature_builder import FeatureBuilder
from quant_system.features.encoders import Encoders

builder = FeatureBuilder()
enc = Encoders()

features = builder.build(
    data=df,
    indicators=indicators_df,
    structure=structure_df,
    orderflow=orderflow_df
)

features = enc.normalize(features)
features = enc.encode_time(features)

print(features.head())

6 Dépendances internes

Le module features/ dépend de :

pandas

numpy

modules internes :

indicators/

structure/

orderflow/

Il ne doit jamais dépendre :

de signals/

de optimization/

du pipeline

👉 Le flux doit rester strictement ascendant.

7 Points d’extension (v2 / v3)

v2
sélection automatique de features (feature selection)

normalisation adaptative

encodage avancé (cyclic encoding, Fourier time encoding)

extraction de features multi‑timeframes

v3
features ML‑based (autoencoders, embeddings)

features cross‑assets

features basées sur la microstructure avancée

features dynamiques (rolling PCA, rolling clustering)
