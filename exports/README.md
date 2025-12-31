# 📘 exports/README.md

🧭 Rôle du dossier exports/

Le dossier exports/ contient l’ensemble des fichiers générés par le moteur quantitatif, les interfaces et les modules internes.

Il sert de zone de sortie pour :

les rapports

les audits

les badges

les timelines

les résumés

les exports CSV/JSON

les visuels

les attestations

les logs consolidés

C’est un espace de résultats, pas de code.

📂 Contenu typique

Dans ton projet, on trouve :

bot_report.md

audit_final.md

core_analysis_export.csv

memory_local_export.json

visuals/

bot_registry_*

mentor_validations.*

scoring_table.md

signal_challenges.md

community_roles.md

etc.

🔧 Intégration dans le projet

Les exports sont produits par :

modules/quant/

backtest/

interface/

interface_pilotage/

les scripts d’automatisation (documentation_md/scripts_automation/)

Ils servent à :

analyser les performances

suivre l’évolution du système

générer des rapports

documenter les résultats

alimenter les interfaces

📌 Bonnes pratiques

Ne jamais versionner les fichiers volumineux.

Organiser les exports par type (CSV, JSON, MD, visuels).

Documenter les formats dans ce README.

Nettoyer régulièrement les fichiers obsolètes.
