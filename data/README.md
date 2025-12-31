# 📘 data/README.md

🧭 Rôle du dossier data/

Le dossier data/ regroupe l’ensemble des composants liés à la gestion des données utilisées par le moteur quantitatif.
Il constitue la première couche du pipeline : tout ce qui suit (indicateurs, stratégie, backtest, modules analytiques) dépend de la qualité, de la cohérence et de la structure des données présentes ici.

Ce dossier est responsable de :

l’ingestion des données brutes

le nettoyage et la normalisation

la validation des formats

la gestion des sources (fichiers, API, flux externes)

la préparation des structures de données utilisées par les modules quantitatifs

Il sert de fondation au moteur quantitatif.

📂 Contenu typique

Selon l’évolution du projet, ce dossier peut contenir :

des scripts d’ingestion (loader, fetcher, reader)

des fonctions de nettoyage (cleaner, sanitizer)

des validateurs de formats (validator)

des structures de données standardisées (ohlc, ticks, features)

des fichiers de données (CSV, JSON, Parquet)

des sous‑dossiers par source ou par marché

Si des fichiers volumineux sont présents, ils doivent être exclus du dépôt Git via .gitignore.

🔧 Intégration dans le moteur quantitatif

Le dossier data/ est utilisé par :

indicators/ pour calculer les signaux

strategy/ pour appliquer les règles d’entrée/sortie

backtest/ pour simuler les performances

modules/quant/ pour les analyses structurelles, orderflow, volatilité, etc.

Il doit garantir :

des formats homogènes

des colonnes standardisées

des index temporels propres

des valeurs cohérentes (pas de trous, pas de doublons)

🧪 Tests et validation

Les tests associés à la gestion des données doivent vérifier :

la conformité des formats

la présence des colonnes obligatoires

la cohérence temporelle

la robustesse face aux données manquantes

la compatibilité avec les modules quantitatifs

📌 Bonnes pratiques

Ne jamais stocker de données sensibles ou propriétaires dans le dépôt.

Utiliser .gitignore pour exclure les fichiers volumineux.

Documenter les formats attendus (colonnes, types, fréquence).

Centraliser les fonctions d’ingestion pour éviter les duplications.

Préférer des formats efficaces (Parquet) pour les gros volumes.

🧭 Navigation

Pour comprendre comment les données sont utilisées dans le moteur :

Lire ce fichier

Explorer indicators/

Explorer strategy/

Explorer backtest/

Explorer modules/quant/
