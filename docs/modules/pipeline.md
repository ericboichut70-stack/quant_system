# 📦 Module 1 — pipeline/

1 Description générale

Le module pipeline orchestre l’ensemble du système. Il constitue le point d’entrée unique du moteur quantitatif : il charge les données, applique les modules d’analyse, construit les features, génère les signaux, calcule les scores et produit un résultat final cohérent et traçable.

C’est le cœur du système, garantissant :

la cohérence du flux de données

l’ordre d’exécution des modules

la traçabilité (hashing SHA256)

la reproductibilité des résultats

2 Responsabilités du module

Le pipeline :

charge les données brutes

applique les prétraitements

calcule les indicateurs techniques

détecte la structure de marché

calcule l’orderflow

construit les features

génère les signaux

attribue les signaux

calcule les signatures SHA256

renvoie un objet final contenant toutes les étapes

3 Entrées / sorties

Entrées
data_path : chemin vers les données OHLCV

config_path : fichier YAML de configuration

paramètres optionnels (selon ton implémentation)

Sorties
Un objet PipelineResult contenant :

data : données nettoyées

indicators : indicateurs calculés

structure : swings, HH/HL/LH/LL

orderflow : delta, imbalance, absorption

features : matrice de features

signals : signaux générés

hash : signature SHA256 du run

4 Classes / fonctions principales

* run_pipeline(data_path, config_path)

Fonction principale orchestrant l’ensemble du système.

Responsabilités :

charger les données

appliquer les modules dans le bon ordre

gérer les erreurs

produire un résultat final cohérent

5 Exemple d’utilisation

from quant_system.pipeline import run_pipeline

results = run_pipeline(
    data_path="data/BTCUSDT.csv",
    config_path="config/default.yaml"
)

print("Signaux générés :")
print(results.signals.head())

print("Hash du run :", results.hash)

6 Dépendances internes

Le pipeline dépend des modules suivants :

data

indicators

structure

orderflow

features

signals

attribution

utils.hashing

Il ne dépend d’aucun module externe du système (principe d’inversion des dépendances).

7 Points d’extension (v2 / v3)

v2
ajout d’un module ml/

intégration du backtesting

configuration YAML avancée

hooks modulaires

v3
exécution temps réel

optimisation bayésienne

gestion multi‑actifs

pipeline parallèle / distribué
