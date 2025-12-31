# 🖥️ Interfaces — Index Global

Ce document sert d’**index centralisé** pour toutes les interfaces du projet :  

- dashboards principaux (`interface/`)  
- interfaces de pilotage (`interface_pilotage/`)  
- outils CLI  
- interfaces mentorales  
- modules narratifs  

Il facilite la navigation et l’orientation.

---

## 🧭 1. Dashboards Principaux (`interface/`)

## 1.1 `predictability_dashboard.py`

- analyse de prédictibilité  
- visualisation des signaux  
- heatmaps, courbes, zones  

## 1.2 `propfirm_dashboard.py`

- analyse orientée prop‑firm  
- gestion du risque  
- suivi des règles  

---

## 🧭 2. Interfaces de Pilotage (`interface_pilotage/`)

## 2.1 Dashboards Avancés

- `bot_dashboard.py`  
- `streamlit_dashboard.py`  
- `streamlit_history.py`  
- `streamlit_manifest_audio.py`  

## 2.2 Outils CLI

- `cli_launcher.py`  
- `quest_cli.py`  
- `vote_cli.py`  

## 2.3 Interfaces Mentorales

- `mentor_interface.py`  
- `mentor_validations/`  

---

## 🧭 3. Modules Narratifs & Communautaires

- scoring  
- progression  
- rôles  
- badges  
- timelines  
- narration interne  

---

## 🧭 4. Intégration avec les autres couches

Les interfaces utilisent :

- `exports/`  
- `modules/`  
- `utils/`  
- `documentation_md/`  

Elles ne modifient jamais la logique métier.
