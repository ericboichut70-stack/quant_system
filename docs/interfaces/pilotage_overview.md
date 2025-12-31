# 🧭 Pilotage Overview — Interfaces Avancées (`interface_pilotage/`)

Ce document présente une vue d’ensemble des **interfaces de pilotage**, situées dans le dossier `interface_pilotage/`.  
Elles constituent la couche d’orchestration, de suivi et de gestion interne du système.

---

## 🧱 1. Rôle des Interfaces de Pilotage

Les interfaces de pilotage permettent :

- de gérer les rôles, badges, certifications  
- de suivre les timelines et historiques  
- d’interagir avec les modules internes  
- de valider des étapes  
- de piloter des scénarios  
- d’utiliser des outils avancés (audio, CLI, dashboards internes)  

Elles sont destinées à un usage **interne**, **expert**, ou **pédagogique**.

---

## 📂 2. Composants Principaux

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

## 2.4 Modules Narratifs & Communautaires

- scoring  
- progression  
- rôles  
- badges  
- timelines  

---

## 🧬 3. Architecture Fonctionnelle

Les interfaces de pilotage s’appuient sur :

- `modules/` (analyses, scoring, progression)  
- `exports/` (rapports, historiques)  
- `documentation_md/` (rituels, scripts internes)  
- `utils/` (helpers transverses)  

Elles ne modifient jamais la logique métier.

---

## 🎨 4. Visualisations

Les dashboards internes peuvent inclure :

- timelines  
- historiques  
- badges  
- rôles  
- signatures  
- heatmaps internes  
- graphiques narratifs  

---

## 🔧 5. Lancement

Dashboards :

```bash
streamlit run interface_pilotage/bot_dashboard.py

CLI :

python interface_pilotage/cli_launcher.py

🧪 6. Tests

Les tests doivent vérifier :

la stabilité des interfaces

la cohérence des données affichées

la compatibilité avec les exports

la robustesse des interactions
