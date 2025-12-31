# 📦 Module 7 — signals/

1 Description générale

Le module signals/ est l’un des modules les plus stratégiques de ton moteur quantitatif.
Il a pour rôle de transformer :

les features

la structure

les indicateurs

l’orderflow

… en signaux exploitables, robustes, auditables et reproductibles.

Ce module constitue la couche décisionnelle du système.
Il ne prend pas de positions, mais il génère des signaux qui pourront être utilisés :

pour du backtesting

pour du ML supervisé

pour des stratégies futures

pour de l’analyse statistique

2 Responsabilités du module

Le module signals/ doit :

définir des conditions de signal basées sur plusieurs modules

combiner les informations (tendance, structure, orderflow, volatilité…)

produire un signal clair :

1 = signal haussier

-1 = signal baissier

0 = neutre

attribuer un score de confiance

renvoyer un DataFrame propre et aligné

Il ne doit pas :

exécuter des trades

gérer le risque

faire du ML

faire du backtesting

👉 C’est un module de logique décisionnelle, pas d’exécution.

3 Entrées / sorties

Entrées
DataFrame de features

éventuellement :

structure

indicateurs

orderflow

paramètres optionnels :

seuils

règles de filtrage

scoring

Sorties
Un DataFrame contenant :

signal (1, -1, 0)

score (confiance)

components (optionnel : contributions des modules)

4 Classes / fonctions principales

## SignalEngine

Cœur du module : génère les signaux.

Méthodes typiques :

generate(features)  
→ renvoie un DataFrame avec signal et score

Exemples de règles :

tendance haussière + structure HL + delta positif → signal haussier

tendance baissière + structure LH + imbalance vendeuse → signal baissier

volatilité extrême → neutralisation

### Scoring

Attribue un score de confiance.

Méthodes typiques :

score(signals)  
→ renvoie une colonne score

Exemples de scoring :

somme pondérée des modules

normalisation

pénalisation en cas de volatilité extrême

5 Exemple d’utilisation

from quant_system.signals.signal_engine import SignalEngine
from quant_system.signals.scoring import Scoring

engine = SignalEngine()
scorer = Scoring()

signals = engine.generate(features)
signals = scorer.score(signals)

print(signals.tail())

6 Dépendances internes

Le module signals/ dépend de :

features/

indicators/

structure/

orderflow/

Il ne doit jamais dépendre :

de optimization/

de pipeline/

de utils/ (sauf hashing si nécessaire)

👉 Le flux doit rester strictement ascendant.

7 Points d’extension (v2 / v3)

v2
signaux probabilistes

signaux multi‑horizons

signaux ML‑based (classification supervisée)

signaux pondérés par volatilité

v3
signaux adaptatifs

signaux multi‑actifs

signaux basés sur clustering dynamique

signaux en temps réel
