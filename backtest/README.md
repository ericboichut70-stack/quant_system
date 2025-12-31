# 📘 backtest/README.md

🧭 Rôle du dossier backtest/

Le dossier backtest/ contient le moteur de backtesting du système.
Il constitue la quatrième couche du pipeline quantitatif, après :

data/ (ingestion & nettoyage)

indicators/ (features & signaux)

strategy/ (règles d’entrée/sortie)

Le backtest permet de :

simuler l’exécution d’une stratégie sur des données historiques

mesurer la performance, la robustesse et la stabilité

analyser les métriques clés (drawdown, winrate, expectancy, Sharpe, etc.)

valider les signaux et les règles de stratégie

comparer différentes variantes ou paramètres

C’est un composant essentiel pour évaluer la qualité du moteur quantitatif.

📂 Contenu typique

Selon l’évolution du projet, ce dossier peut contenir :

un moteur d’exécution historique

des simulateurs d’ordres (market, limit, stop, partial fills)

des modules de gestion du risque

des calculateurs de métriques de performance

des outils de visualisation ou d’export

des classes de configuration ou de scénarios

Dans ton projet, le fichier principal est :

backtest_engine.py (dans modules/)

mais ce dossier backtest/ est destiné à accueillir la logique dédiée, séparée du reste.

🔧 Intégration dans le moteur quantitatif

Le backtest dépend de :

data/ pour les données propres

indicators/ pour les features

strategy/ pour les règles

utils/ pour les helpers

modules/quant/ pour les analyses structurelles, signaux, volatilité, etc.

Il fournit en retour :

des métriques de performance

des journaux d’exécution

des courbes d’équité

des exports (CSV, JSON, graphiques)

des diagnostics pour optimiser la stratégie

🧪 Tests et validation

Les tests associés au backtest doivent vérifier :

l’absence de lookahead bias

la cohérence temporelle des signaux

la bonne exécution des ordres

la stabilité des métriques

la reproductibilité des résultats

la compatibilité avec différentes stratégies

📌 Bonnes pratiques

Toujours séparer la logique d’exécution de la logique de stratégie.

Documenter les paramètres du moteur (slippage, spread, fees, etc.).

Vérifier systématiquement les décalages temporels.

Utiliser des structures de données immuables pour éviter les effets de bord.

Exporter les résultats dans un format standardisé.

🧭 Navigation

Pour comprendre comment le backtest s’intègre dans le moteur :

Lire ce fichier

Explorer strategy/ pour voir les règles utilisées

Explorer indicators/ pour comprendre les signaux

Explorer modules/quant/ pour les analyses avancées

Explorer exports/ pour voir les résultats générés
