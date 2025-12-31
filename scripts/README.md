# 📘 scripts/README.md

🧭 Rôle du dossier scripts/

Le dossier scripts/ regroupe les scripts utilitaires utilisés pour automatiser certaines tâches du projet.
Il ne contient pas de logique métier, mais des outils facilitant :

l’exécution de pipelines

la génération de fichiers

la manipulation de données

la maintenance du projet

les opérations ponctuelles

C’est un espace de support opérationnel.

📂 Contenu typique

Ce dossier peut contenir :

des scripts de nettoyage

des scripts de génération

des scripts de conversion

des scripts de diagnostic

des scripts d’import/export

des scripts de maintenance

Selon ton projet, il peut inclure :

des scripts de préparation de données

des scripts de lancement de modules

des scripts d’analyse ponctuelle

des scripts de support pour les interfaces

🔧 Intégration dans le projet

Les scripts doivent :

être autonomes

être documentés

ne pas dépendre de chemins absolus

utiliser les modules internes plutôt que du code dupliqué

être compatibles avec l’environnement du projet

Ils peuvent être exécutés via :

bash
python scripts/<nom_du_script>.py

🧪 Bonnes pratiques

Documenter chaque script en en‑tête

Éviter les dépendances inutiles

Ne pas stocker de données volumineuses dans ce dossier

Préférer des noms explicites

Garder les scripts courts et ciblés

🧭 Navigation

Pour utiliser ce dossier :

Lire ce fichier

Explorer les scripts disponibles

Vérifier les dépendances

Exécuter les scripts selon les besoins
