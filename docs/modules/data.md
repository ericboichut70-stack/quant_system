# 📦 Module 2 — data/

1 Description générale
Le module data/ constitue la porte d’entrée du système. Il est responsable de :

charger les données brutes (CSV, parquet, API, etc.)

valider leur intégrité

nettoyer et normaliser les colonnes

préparer un DataFrame cohérent pour les modules suivants

Ce module garantit que toute la chaîne de traitement repose sur des données propres, fiables et standardisées.

2 Responsabilités du module
Le module data/ doit :
charger les données depuis un fichier ou une source externe

vérifier la présence des colonnes essentielles (OHLCV)

convertir les types (datetime, float, int)

gérer les valeurs manquantes

normaliser les noms de colonnes

appliquer un prétraitement minimal (tri, indexation, etc.)

renvoyer un DataFrame propre et prêt pour les indicateurs

Il ne doit pas :

calculer d’indicateurs

générer des features

produire des signaux

faire de l’orderflow

faire de la structure de marché

👉 C’est un module purement “data engineering”.

3 Entrées / sorties
Entrées
path : chemin vers un fichier CSV ou autre format

config (optionnel) : règles de nettoyage spécifiques

paramètres additionnels selon ton implémentation

Sorties
Un DataFrame Pandas contenant :

colonnes OHLCV standardisées

index temporel propre

données triées

types corrects

valeurs manquantes gérées

4 Classes / fonctions principales

* DataLoader

Responsable du chargement brut.

Méthodes typiques :

load(path)

validate_columns(df)

standardize_columns(df)

* Preprocessor

Responsable du nettoyage et de la normalisation.

Méthodes typiques :

clean(df)

normalize(df)

fix_types(df)

sort(df)

5 Exemple d’utilisation

from quant_system.data.loader import DataLoader
from quant_system.data.preprocess import Preprocessor

loader = DataLoader()
pre = Preprocessor()

df = loader.load("data/BTCUSDT.csv")
df = pre.clean(df)
df = pre.normalize(df)

print(df.head())

6 Dépendances internes

Le module data/ est indépendant des autres modules. Il ne dépend que de :

pandas

éventuellement numpy

éventuellement yaml (si config)

👉 Aucun module interne ne doit dépendre de data/ en retour (principe de flux unidirectionnel).

7 Points d’extension (v2 / v3)

v2
support des formats parquet / feather

chargement multi‑actifs

gestion des timeframes multiples

validation avancée (statistiques, anomalies)

v3
ingestion en streaming

connexion API (Binance, Coinbase, etc.)

data lake local

gestion des données tick‑level
