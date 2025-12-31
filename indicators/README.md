# 📘 indicators/README.md

🧭 Rôle du dossier indicators/

Le dossier indicators/ regroupe l’ensemble des indicateurs techniques utilisés par le moteur quantitatif.
Il constitue la seconde couche du pipeline, juste après les données (data/) et avant la stratégie (strategy/) et le backtest (backtest/).

Les indicateurs sont responsables de :

transformer les données brutes en features exploitables

détecter des structures, patterns ou signaux

fournir des mesures quantitatives cohérentes et standardisées

alimenter les modules de stratégie, de filtrage, d’optimisation et de simulation

Ils jouent un rôle central dans la génération de signaux.

📂 Contenu typique

Le dossier contient généralement :

indicateurs de base  
(ex. moyennes mobiles, volatilité, dérivées simples)

indicateurs avancés  
(ex. énergie, pivots, signaux composites)

fonctions utilitaires  
(normalisation, smoothing, dérivées, transformations)

structures de sortie standardisées  
(DataFrame enrichies, colonnes normalisées, signaux booléens)

Dans ton projet, on retrouve notamment :

base_indicators.py

phoebus_energy.py

ut_pivots.py

index.md (documentation locale)

🔧 Intégration dans le moteur quantitatif

Les indicateurs sont utilisés par :

strategy/ pour définir les règles d’entrée/sortie

backtest/ pour simuler les performances

modules/quant/ pour les analyses structurelles, orderflow, volatilité, etc.

utils/ pour les transformations transverses

Ils doivent garantir :

des formats homogènes

des noms de colonnes cohérents

des valeurs calculées sans trous ni décalages temporels

une compatibilité totale avec les données produites par data/

🧪 Tests et validation

Les tests associés aux indicateurs doivent vérifier :

la cohérence des valeurs calculées

l’absence de décalage temporel (lookahead bias)

la robustesse face aux données manquantes

la stabilité numérique

la compatibilité avec les modules de stratégie et de backtest

📌 Bonnes pratiques

Toujours documenter les paramètres d’un indicateur.

Éviter les calculs redondants : mutualiser dans base_indicators.py.

Préférer des structures de sortie standardisées (DataFrame enrichies).

Vérifier systématiquement l’absence de lookahead.

Grouper les indicateurs par familles si le dossier s’agrandit.

🧭 Navigation

Pour comprendre comment les indicateurs s’intègrent dans le moteur :

Lire ce fichier

Explorer base_indicators.py

Explorer les indicateurs avancés (phoebus_energy.py, ut_pivots.py)

Explorer strategy/ pour voir comment ils sont utilisés

Explorer backtest/ pour comprendre leur impact sur les simulations
