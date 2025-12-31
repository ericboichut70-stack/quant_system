# 📘 interface/README.md

🧭 Rôle du dossier interface/

Le dossier interface/ regroupe les dashboards principaux du projet.
Ces interfaces permettent d’explorer les données, visualiser les signaux, analyser les performances et interagir avec le moteur quantitatif de manière intuitive.

Elles constituent la couche utilisateur du système.

📂 Contenu typique

Dans ton projet, ce dossier contient notamment :

predictability_dashboard.py

propfirm_dashboard.py

index.md (documentation locale)

Ces dashboards sont conçus pour :

visualiser les signaux

analyser la prédictibilité

explorer les performances

tester des scénarios

naviguer dans les données

▶️ Lancement

Les dashboards sont généralement exécutés via Streamlit :

bash
streamlit run interface/<nom_du_dashboard>.py
Exemples :

bash
streamlit run interface/predictability_dashboard.py
streamlit run interface/propfirm_dashboard.py

🔧 Intégration dans le projet

Les interfaces utilisent :

les données (data/)

les indicateurs (indicators/)

les modules quantitatifs (modules/quant/)

les exports (exports/)

Elles servent de visualisation et d’outil d’analyse.
