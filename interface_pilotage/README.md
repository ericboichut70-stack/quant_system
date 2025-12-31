# 📘 interface_pilotage/README.md

🧭 Rôle du dossier interface_pilotage/

Le dossier interface_pilotage/ regroupe les interfaces avancées, destinées au pilotage, à la certification, à la narration et à l’orchestration du système.

Il contient :

des dashboards Streamlit avancés

des interfaces audio

des outils de certification

des CLI de pilotage

des outils de suivi, d’historique, de progression

des visualisations internes

C’est un espace riche, dense, et hautement modulaire.

📂 Contenu typique

On y trouve notamment :

bot_dashboard.py

mentor_interface.py

streamlit_dashboard.py

streamlit_history.py

streamlit_manifest_audio.py

cli_launcher.py

quest_cli.py

vote_cli.py

et de nombreux autres modules spécialisés

▶️ Lancement

Les dashboards se lancent via Streamlit :
streamlit run interface_pilotage/< dashboard >.py

Les CLI se lancent via Python :
python interface_pilotage/< outil >.py

🔧 Intégration dans le projet

Ces interfaces sont utilisées pour :

piloter le système

gérer les rôles, badges, certifications

suivre les timelines

analyser les engagements

visualiser les signatures

orchestrer les modules internes

Elles ne font pas partie du moteur quantitatif, mais de l’écosystème de pilotage.
