Quant System v3 — Moteur Quantitatif Modulaire
Quant System v3 est un moteur quantitatif modulaire conçu pour l’analyse de marché, la génération de signaux, la construction de stratégies, le backtesting et l’intégration future de modèles ML.

Cette version introduit un pipeline entièrement structuré, une documentation professionnelle et une architecture prête pour l’extension.

🚀 Fonctionnalités principales
Pipeline v3 composé de 12 stages indépendants

Backtest event‑driven

Multi‑UT intégré

Indicateurs techniques avancés

Génération de signaux quantitatifs

Construction de signaux composites

Gestion du risque

Export structuré des résultats

Support ML (features + modèles)

Documentation MkDocs Material

📦 Installation
Code
pip install -r requirements.txt
▶️ Exécution du pipeline
Code
python main_pipeline_v3.py
📤 Exports générés
Les résultats sont disponibles dans :

Code
exports/pipeline_v3_example/
Contenu :

trades.csv

equity_curve.csv

metrics.json

📘 Documentation
La documentation complète est disponible dans :

Code
docs/
Elle inclut :

Architecture

Pipeline

Indicateurs

Stratégie

Backtest

ML

Guides techniques

Une version en ligne sera bientôt disponible via GitHub Pages.

🧱 Structure du projet
Code
quant_system/
│
├── pipeline/          # Pipeline v3 (12 stages)
├── config/            # Configuration YAML
├── data/              # Données brutes et nettoyées
├── indicators/        # Indicateurs techniques
├── strategy/          # Stratégies de trading
├── utils/             # Fonctions utilitaires
├── tests/             # Tests unitaires
├── exports/           # Résultats du pipeline
├── docs/              # Documentation MkDocs
├── notebooks/         # Analyses Jupyter
├── archive_legacy/    # Historique du projet
└── main_pipeline_v3.py
🏁 Statut
Version stable, prête pour utilisation, documentation et extension ML.

🟦 3) Préparation de la documentation pour GitHub Pages
Tu as déjà :

mkdocs.yml

docs/

un site local fonctionnel

Il reste une seule étape :
👉 activer GitHub Pages sur la branche gh-pages générée par MkDocs.

Voici la procédure exacte :

🔧 Étape 1 — Ajouter la configuration de déploiement MkDocs
Dans mkdocs.yml, ajouter :

yaml
site_url: https://ericboichut70-stack.github.io/quant_system/
(Tu l’as déjà.)

🔧 Étape 2 — Installer le plugin de déploiement (si tu veux automatiser)
Code
pip install mkdocs ghp-import
🔧 Étape 3 — Générer et pousser la documentation
Depuis la racine :

Code
mkdocs build
ghp-import -n -p site
Cela :

génère le site dans site/

crée la branche gh-pages

pousse automatiquement sur GitHub

🔧 Étape 4 — Activer GitHub Pages
Sur GitHub :

Settings

Pages

Source → gh-pages

Folder → root

Save

Ton site sera disponible à :

Code
https://ericboichut70-stack.github.io/quant_system/
