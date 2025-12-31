# 📘 strategy/README.md

🧭 Rôle du dossier strategy/

Le dossier strategy/ contient la logique décisionnelle du moteur quantitatif.
Il constitue la troisième couche du pipeline, entre :

indicators/ (features & signaux)

backtest/ (simulation & performance)

La stratégie est responsable de :

définir les conditions d’entrée en position

définir les conditions de sortie

gérer le risque (stop, target, sizing)

orchestrer les signaux issus des indicateurs

produire des ordres exploitables par le backtest ou l’exécution réelle

C’est le cœur logique du système.

📂 Contenu typique

Selon l’évolution du projet, ce dossier peut contenir :

des règles d’entrée/sortie

des filtres de marché

des modules de gestion du risque

des stratégies paramétrables

des classes ou fonctions de décision

des configurations de stratégie

des wrappers pour orchestrer plusieurs signaux

Dans ton projet, ce dossier est destiné à accueillir la logique stratégique propre, séparée :

des indicateurs (indicators/)

du moteur de backtest (backtest/)

des modules analytiques (modules/quant/)

🔧 Intégration dans le moteur quantitatif

La stratégie dépend de :

data/ pour les données propres

indicators/ pour les signaux

modules/quant/ pour les analyses avancées (structure, volatilité, orderflow, etc.)

utils/ pour les transformations transverses

Elle fournit en retour :

des signaux d’entrée/sortie

des ordres structurés

des paramètres de gestion du risque

des événements exploitables par le backtest

🧪 Tests et validation

Les tests associés à la stratégie doivent vérifier :

la cohérence des signaux

l’absence de lookahead bias

la stabilité des règles d’entrée/sortie

la compatibilité avec différents jeux de données

la robustesse face aux données manquantes

la reproductibilité des décisions

📌 Bonnes pratiques

Séparer clairement logique de signal et logique de décision.

Documenter les paramètres de la stratégie.

Éviter les dépendances circulaires avec les indicateurs.

Tester systématiquement les règles sur plusieurs horizons temporels.

Prévoir une structure paramétrable pour faciliter l’optimisation.

🧭 Navigation

Pour comprendre comment la stratégie s’intègre dans le moteur :

Lire ce fichier

Explorer indicators/ pour comprendre les signaux utilisés

Explorer modules/quant/ pour les analyses avancées

Explorer backtest/ pour voir comment les décisions sont simulées

Explorer utils/ pour les helpers transverses
