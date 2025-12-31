# 📦 Module 3 — indicators/

1 Description générale

Le module indicators/ regroupe l’ensemble des indicateurs techniques utilisés par le moteur quantitatif. Il fournit des mesures essentielles pour :

la détection de tendance

l’analyse de volatilité

la caractérisation du momentum

la préparation des features

la génération de signaux

Ce module est conçu pour être modulaire, remplaçable, et extensible, afin de permettre l’ajout futur d’indicateurs plus avancés ou spécifiques à certaines stratégies.

2 Responsabilités du module

Le module indicators/ doit :

calculer des indicateurs techniques standardisés

renvoyer des séries propres, alignées sur les données

gérer les valeurs manquantes en début de série

fournir des primitives simples, réutilisables dans d’autres modules

rester indépendant des modules de signaux ou de structure

Il ne doit pas :

générer des signaux

interpréter les indicateurs

faire de la structure de marché

faire de l’orderflow

construire des features

👉 C’est un module purement analytique.

3 Entrées / sorties

Entrées
un DataFrame OHLCV propre

paramètres d’indicateurs (périodes, seuils, etc.)

Sorties
un DataFrame ou une série Pandas contenant les valeurs de l’indicateur

toujours aligné sur l’index temporel

avec gestion propre des NaN initiaux

4 Classes / fonctions principales

Selon ton architecture, les classes typiques sont :

## EMA

Exponential Moving Average.

Méthodes :

compute(series, period) → renvoie une EMA propre, sans artefacts

Utilisation :

pente EMA

tendance

filtrage du bruit

### ADX

Average Directional Index (version simplifiée).

Méthodes :

compute(data) → renvoie ADX, +DI, -DI

Utilisation :

force de tendance

filtrage des phases neutres

### Volatility

Volatilité simple ou ATR-like.

Méthodes :

compute(data) → renvoie une mesure de volatilité

Utilisation :

régimes de volatilité

normalisation des signaux

clustering

5 Exemple d’utilisation

from quant_system.indicators.ema import EMA
from quant_system.indicators.adx import ADX
from quant_system.indicators.volatility import Volatility

ema = EMA.compute(df["close"], period=20)
adx = ADX.compute(df)
vol = Volatility.compute(df)

df["ema20"] = ema
df["adx"] = adx["adx"]
df["volatility"] = vol

6 Dépendances internes

Le module indicators/ dépend uniquement de :

pandas

numpy

Il ne doit dépendre d’aucun autre module interne, pour garantir :

modularité

testabilité

réutilisabilité

7 Points d’extension (v2 / v3)

v2
ajout d’indicateurs avancés :

RSI

MACD

Bollinger Bands

ATR

indicateurs multi‑timeframes

indicateurs basés sur la volatilité réalisée

v3
indicateurs ML‑based (trend classification)

indicateurs de microstructure avancée

indicateurs adaptatifs (KAMA, FRAMA)
