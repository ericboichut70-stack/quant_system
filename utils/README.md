# 📘 utils/README.md

🧭 Rôle du dossier utils/

Le dossier utils/ regroupe les fonctions utilitaires transverses utilisées par l’ensemble du moteur quantitatif.
Il constitue une couche de support : il ne contient pas de logique métier, mais des outils indispensables pour éviter la duplication de code.

Les utilitaires servent à :

manipuler les données

gérer les dates, intervalles, fréquences

effectuer des transformations génériques

standardiser des opérations répétitives

fournir des helpers pour les modules, la stratégie et le backtest

C’est un espace de facteurs communs, conçu pour maintenir la cohérence du code.

📂 Contenu typique

Ce dossier peut contenir :

des fonctions de manipulation de DataFrame

des outils de logging

des helpers mathématiques

des fonctions de normalisation

des outils de parsing

des wrappers génériques

des fonctions de validation

Les utilitaires doivent rester simples, génériques et réutilisables.

🔧 Intégration dans le moteur quantitatif

utils/ est utilisé par :

data/ pour les transformations basiques

indicators/ pour les opérations mathématiques

strategy/ pour les règles paramétrables

backtest/ pour les calculs de performance

modules/quant/ pour les analyses avancées

Les utilitaires doivent être :

stables

testés

documentés

indépendants de toute logique métier

🧪 Tests et validation

Les tests doivent vérifier :

la robustesse des fonctions

la cohérence des résultats

la compatibilité avec les structures de données utilisées dans le moteur

l’absence d’effets de bord

📌 Bonnes pratiques

Garder les utilitaires petits et atomiques.

Éviter toute dépendance circulaire.

Ne jamais intégrer de logique métier dans utils/.

Documenter chaque fonction.

Mutualiser les opérations répétitives.

🧭 Navigation

Pour comprendre comment utils/ s’intègre :

Lire ce fichier

Explorer les fonctions utilitaires

Voir comment elles sont utilisées dans data/, indicators/, strategy/ et backtest/

Explorer modules/quant/ pour les usages avancés
