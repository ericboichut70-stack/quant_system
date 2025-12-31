# 📘 modules/quant/README.md

🧭 Rôle du dossier modules/quant/

Le dossier modules/quant/ regroupe l’ensemble des modules analytiques du moteur quantitatif.
Il constitue la couche avancée du pipeline, au‑dessus de :

data/ (ingestion & nettoyage)

indicators/ (features & signaux)

strategy/ (règles d’entrée/sortie)

backtest/ (simulation)

Ces modules fournissent des analyses structurelles, contextuelles et dynamiques du marché.
Ils enrichissent la stratégie et le backtest avec des signaux de haut niveau.

📂 Contenu du dossier

Les modules quantitatifs identifiés sont :

Structure de marché
zigzag_mapper.py

structure_tracker.py

order_blocks.py

fvg_detector.py

Tendance & momentum
trend_detector.py

multi_timeframe_convergence.py

multi_tf_contextualizer.py

Volatilité
volatility_clustering.py

Orderflow
orderflow_reader.py

Signalisation
signal_filter.py

signal_predictor.py

signal_attribution.py

Optimisation
optimizer.py

order_optimizer.py

Pré‑trade & simulation
pre_trade_simulator.py

pre_trade_validator.py

Radar & scanning
market_radar.py

scanner_intraday.py

Divers (à confirmer)
poi_mapper.py

🔧 Intégration dans le moteur quantitatif

Ces modules sont utilisés par :

strategy/ pour enrichir les règles

backtest/ pour simuler des comportements complexes

indicators/ pour générer des features avancées

utils/ pour les transformations transverses

Ils doivent respecter :

des formats standardisés

une cohérence temporelle stricte

l’absence de lookahead bias

une compatibilité totale avec les données de data/

🧪 Tests et validation

Les tests doivent vérifier :

la cohérence des signaux

la stabilité numérique

la robustesse face aux données manquantes

la reproductibilité des résultats

la compatibilité avec les stratégies et le backtest

📌 Bonnes pratiques

Garder chaque module autonome et bien délimité.

Documenter les paramètres et les sorties.

Éviter les dépendances croisées inutiles.

Mutualiser les helpers dans utils/.

Tester systématiquement les modules sensibles (structure, orderflow, volatilité)
