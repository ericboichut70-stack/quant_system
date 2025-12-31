# 📦 Module 9 — optimization/

1 Description générale

Le module optimization/ est dédié à la recherche de paramètres optimaux pour ton moteur quantitatif.
Il permet d’explorer, tester et comparer différentes configurations afin d’améliorer :

la qualité des signaux

la robustesse des features

la stabilité des modules

la performance globale du pipeline

Ce module constitue la base d’un futur système d’optimisation avancée (v2/v3), incluant :

optimisation brute

optimisation heuristique

optimisation bayésienne

optimisation multi‑objectifs

2 Responsabilités du module

Le module optimization/ doit :

tester différentes combinaisons de paramètres

exécuter le pipeline avec ces paramètres

mesurer la qualité des résultats (score, stabilité, cohérence)

renvoyer les meilleurs paramètres selon une métrique définie

rester indépendant du backtesting (qui arrivera en v2)

Il ne doit pas :

générer des signaux

modifier les modules internes

faire du ML

exécuter des stratégies de trading

👉 C’est un module d’exploration paramétrique, pas d’exécution.

3 Entrées / sorties

Entrées
un dictionnaire de paramètres à tester

un pipeline ou une fonction d’évaluation

une métrique d’optimisation (score, stabilité, etc.)

Sorties
Un dictionnaire contenant :

les meilleurs paramètres trouvés

la valeur de la métrique associée

éventuellement un historique des essais

4 Classes / fonctions principales

## ParameterSearch

Cœur du module : explore l’espace des paramètres.

Méthodes typiques :

optimize(config)  
→ renvoie les meilleurs paramètres

Exemples de paramètres optimisables :

période EMA

seuil ZigZag

profondeur de swing

fenêtre de volatilité

seuil d’imbalance

pondérations du scoring

5 Exemple d’utilisation

from quant_system.optimization.parameter_search import ParameterSearch

search = ParameterSearch()

best_params = search.optimize({
    "ema_period": [10, 20, 30],
    "zigzag_threshold": [0.01, 0.02, 0.03],
    "imbalance_window": [5, 10, 20]
})

print("Meilleurs paramètres :", best_params)

6 Dépendances internes

Le module optimization/ dépend de :

pipeline/ (pour exécuter les runs)

signals/ (pour évaluer les signaux)

features/ (pour mesurer la qualité des features)

Il ne doit jamais dépendre :

de utils/ (sauf hashing si nécessaire)

de attribution/

de orderflow/

👉 Le flux doit rester strictement descendant, car l’optimisation est un module “méta”.

7 Points d’extension (v2 / v3)

v2
optimisation brute multi‑paramètres

optimisation heuristique (random search)

optimisation multi‑objectifs (score + stabilité)

intégration avec le backtesting

v3
optimisation bayésienne

optimisation adaptative

optimisation en ligne

optimisation multi‑actifs

optimisation distribuée
