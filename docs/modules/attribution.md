# 📦 Module 8 — attribution/

1 Description générale

Le module attribution/ est dédié à l’analyse post‑signal.
Son rôle est d’expliquer pourquoi un signal a été généré, en identifiant la contribution de chaque module :

tendance

structure

orderflow

volatilité

features dérivées

Ce module est essentiel pour :

l’auditabilité

la transparence

la validation des signaux

la compréhension du moteur

la préparation au ML supervisé (features → label → attribution)

Il transforme un signal brut en une explication structurée, indispensable pour un moteur quantitatif professionnel.

2 Responsabilités du module
Le module attribution/ doit :

analyser les signaux générés

identifier les conditions ayant déclenché le signal

mesurer la contribution de chaque composant

produire un score d’attribution

renvoyer un tableau clair et exploitable

Il ne doit pas :

générer des signaux

modifier les features

faire du ML

faire du backtesting

👉 C’est un module d’explication, pas de décision.

3 Entrées / sorties
Entrées
DataFrame de signaux

DataFrame de features

éventuellement :

structure

indicateurs

orderflow

Sorties
Un DataFrame contenant :

signal

score

attribution_tendance

attribution_structure

attribution_orderflow

attribution_volatilite

attribution_features

attribution_total

4 Classes / fonctions principales

## AttributionEngine

Cœur du module : calcule la contribution de chaque composant.

Méthodes typiques :

attribute(signals, features)  
→ renvoie un DataFrame d’attribution

Exemples de contributions :

tendance = 0.4

structure = 0.3

orderflow = 0.2

volatilité = 0.1

5 Exemple d’utilisation

from quant_system.attribution.attribution_engine import AttributionEngine

engine = AttributionEngine()

attribution = engine.attribute(
    signals=signals,
    features=features
)

print(attribution.tail())

6 Dépendances internes

Le module attribution/ dépend de :

signals/

features/

Il ne doit jamais dépendre :

de optimization/

du pipeline

de utils/ (sauf hashing si nécessaire)

👉 Le flux doit rester strictement ascendant.

7 Points d’extension (v2 / v3)

v2
attribution pondérée par volatilité

attribution multi‑horizons

attribution probabiliste

attribution compatible ML (SHAP‑like simplifié)

v3
attribution dynamique

attribution multi‑actifs

attribution en temps réel

attribution basée sur modèles ML
