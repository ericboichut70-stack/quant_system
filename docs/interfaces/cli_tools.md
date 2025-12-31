# ⚙️ Documentation — Outils CLI (`interface_pilotage/`)

Ce document décrit les **outils en ligne de commande (CLI)** du projet, situés dans le dossier `interface_pilotage/`.  
Il complète le README du dossier en offrant une vue technique, fonctionnelle et structurée.

---

## 🧭 1. Rôle des Outils CLI

Les outils CLI permettent :

- d’interagir avec le moteur quantitatif sans interface graphique  
- d’automatiser certaines tâches  
- de piloter des modules internes  
- d’exécuter des scénarios rapides  
- de lancer des analyses ou exports  
- de gérer des rôles, badges, certifications, historiques  

Ils constituent la **couche de pilotage textuelle** du système.

---

## 📂 2. CLI Principaux

## 2.1 `cli_launcher.py`

- point d’entrée général  
- menu interactif  
- accès aux modules internes  
- exécution rapide de commandes  

## 2.2 `quest_cli.py`

- gestion des quêtes  
- progression utilisateur  
- scoring  
- validation de tâches  

## 2.3 `vote_cli.py`

- système de vote interne  
- gestion des décisions communautaires  
- enregistrement des résultats  

## 2.4 `mentor_interface.py` (mode CLI)

- interactions mentorales  
- validation des étapes  
- suivi des progrès  

---

## ▶️ 3. Lancement des CLI

Les outils CLI s’exécutent via Python :

```bash
python interface_pilotage/cli_launcher.py
python interface_pilotage/quest_cli.py
python interface_pilotage/vote_cli.py

🧱 4. Architecture d’un CLI

Un outil CLI typique contient :

un parser d’arguments

un menu interactif

un module d’exécution

un module d’export

un module de logs

🔧 5. Intégration avec les autres couches

Les CLI utilisent :

exports/ pour lire/écrire des fichiers

modules/ pour exécuter des actions internes

utils/ pour les helpers

documentation_md/ pour les rituels internes

Ils ne modifient jamais la logique métier.

🧪 6. Tests

Les tests doivent vérifier :

la stabilité des menus

la gestion des erreurs

la compatibilité avec les exports

la cohérence des actions
