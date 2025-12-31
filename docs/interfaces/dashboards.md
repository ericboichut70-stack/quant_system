# 🖥️ Documentation — Dashboards (`interface/`)

Ce document décrit les **dashboards principaux** du projet, situés dans le dossier `interface/`.  
Il complète le README du dossier `interface/` en offrant une vue technique et fonctionnelle.

---

## 🧭 1. Rôle des Dashboards

Les dashboards permettent :

- d’explorer les données  
- de visualiser les signaux  
- d’analyser les performances  
- d’interagir avec le moteur quantitatif  
- de tester des scénarios  
- de naviguer dans les exports  

Ils constituent la **couche utilisateur** du système.

---

## 📂 2. Dashboards Principaux

## 2.1 `predictability_dashboard.py`

- analyse de prédictibilité  
- visualisation des signaux  
- heatmaps, courbes, zones  
- statistiques de performance  

## 2.2 `propfirm_dashboard.py`

- analyse orientée prop‑firm  
- gestion du risque  
- suivi des règles  
- visualisation des drawdowns  

---

## ▶️ 3. Lancement des Dashboards

Les dashboards sont exécutés via Streamlit :

```bash
streamlit run interface/predictability_dashboard.py
streamlit run interface/propfirm_dashboard.py

🧱 4. Architecture d’un Dashboard

Un dashboard typique contient :

un loader de données

un module de visualisation

un module d’analyse

un module d’interaction utilisateur

un module d’export

🎨 5. Visualisations

Les dashboards peuvent inclure :

graphiques multi‑panneaux

heatmaps

signaux visuels (flèches, zones, couleurs)

courbes d’équité

tableaux de performance

🔧 6. Intégration avec les autres couches

Les dashboards utilisent :

data/ pour les données

indicators/ pour les signaux

modules/quant/ pour les analyses avancées

exports/ pour les rapports

utils/ pour les transformations

Ils ne modifient jamais les données : ils sont en lecture seule.

🧪 7. Tests

Les tests doivent vérifier :

le chargement correct des données

la stabilité des visualisations

la compatibilité avec les exports

l’absence d’erreurs Streamlit

🧭 8. Commandes PowerShell — version institutionnelle

🟦 Commandes PowerShell — à la racine du projet

📌 Se placer à la racine du projet

powershell
cd C:\Users\user\OneDrive\Documents\CODES_CASCADE\quant_system

Destination :  
Permet de s’assurer que toutes les commandes suivantes s’exécutent dans le bon contexte.

📌 Lancer un dashboard spécifique

Dashboard de prédictibilité
powershell
streamlit run interface/predictability_dashboard.py

Dashboard PropFirm
powershell
streamlit run interface/propfirm_dashboard.py

Destination :  
Lance directement un dashboard Streamlit sans passer par le menu principal.
