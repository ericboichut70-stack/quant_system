# 📘 tests/README.md

🧭 Rôle du dossier tests/

Le dossier tests/ regroupe l’ensemble des tests unitaires et fonctionnels du projet.
Il constitue la couche de validation technique, garantissant la stabilité, la cohérence et la non‑régression du moteur quantitatif et de l’écosystème élargi.

Les tests permettent de :

vérifier la cohérence des modules

détecter les régressions

valider les comportements attendus

sécuriser les évolutions futures

garantir la compatibilité entre les différentes couches du système

📂 Contenu typique

Le dossier contient généralement :

des fichiers test_*.py

des tests unitaires pour les modules quantitatifs

des tests fonctionnels pour les interfaces ou pipelines

des tests de cohérence pour les exports

des tests de validation pour les transformations de données

Dans ton projet, les tests couvrent notamment :

structure de marché

orderflow

volatilité

signaux

optimisation

modules pédagogiques et communautaires

simulateurs internes

🔧 Intégration dans le projet

Les tests doivent être exécutables via :
pytest

ou, selon la configuration :
python -m pytest

Ils doivent couvrir :

data/

indicators/

strategy/

backtest/

modules/quant/

les modules critiques de l’écosystème

Un test = un comportement précis

Pas de dépendances externes non contrôlées

Utiliser des données de test minimales et reproductibles

Tester les cas limites (NaN, trous temporels, volatilité extrême)

Documenter les tests complexes

Garder les tests rapides

🧭 Navigation

Pour comprendre la structure des tests :

Lire ce fichier

Explorer les fichiers test_*.py

Identifier les modules associés

Exécuter les tests pour valider le moteur
