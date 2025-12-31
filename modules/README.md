# 📘 modules/README.md

🧭 Rôle du dossier modules/

Le dossier modules/ est l’un des plus vastes du projet.
Il regroupe un ensemble très large de composants couvrant :

des modules quantitatifs (analyse structurelle, signaux, volatilité, orderflow, optimisation…)

des modules pédagogiques

des modules communautaires

des modules de progression

des modules de scoring

des modules de narration

des dashboards internes

des simulateurs sociaux

des outils de certification

des tests unitaires

Ce dossier représente l’écosystème élargi du projet.

Pour clarifier la structure, une distinction nette est faite entre :

les modules quantitatifs (moteur d’analyse de marché)

les modules non quantitatifs (pédagogie, communauté, progression, etc.)

📂 Structure interne

Le dossier contient :

des fichiers Python (modules fonctionnels)

des sous‑dossiers (utils/, __pycache__/, tests)

des modules de scoring, progression, narration, etc.

des modules analytiques avancés (quantitatifs)

des modules d’interface interne

Pour faciliter la navigation, il est recommandé d’isoler les modules quantitatifs dans un sous‑dossier dédié :

modules/
    quant/
        (modules quantitatifs)

🔧 Modules quantitatifs (à isoler)

Les modules quantitatifs identifiés sont :

zigzag_mapper.py

structure_tracker.py

fvg_detector.py

order_blocks.py

trend_detector.py

multi_timeframe_convergence.py

multi_tf_contextualizer.py

volatility_clustering.py

orderflow_reader.py

signal_filter.py

signal_predictor.py

signal_attribution.py

optimizer.py

order_optimizer.py

backtest_engine.py

pre_trade_simulator.py

pre_trade_validator.py

market_radar.py

scanner_intraday.py

poi_mapper.py (à confirmer)

Ces modules doivent être documentés dans un README séparé (modules/quant/README.md).

🔧 Modules non quantitatifs

Ils couvrent :

progression

scoring

narration

communauté

badges

rôles

saisonnalité

mentorat

certification

dashboards internes

simulateurs sociaux

outils pédagogiques

Ces modules ne font pas partie du moteur quantitatif, mais de l’écosystème global.

🧪 Tests

Le dossier contient également de nombreux tests unitaires :

Code
test_*.py
Ils doivent être conservés mais clairement séparés de la logique métier.

📌 Bonnes pratiques

Isoler les modules quantitatifs dans modules/quant/.

Documenter séparément les deux familles (quantitatif / non quantitatif).

Éviter les dépendances croisées entre les deux mondes.

Garder les modules cohérents et autonomes.

Utiliser utils/ pour les fonctions transverses.

🧭 Navigation

Pour comprendre ce dossier :

Lire ce fichier

Explorer modules/quant/ pour le moteur quantitatif

Explorer les autres modules selon leur famille fonctionnelle

Explorer tests/ pour les validations

Explorer interface_pilotage/ pour les dashboards internes
