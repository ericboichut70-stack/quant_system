# 📘 README.md final — structure commentée
# 🧠 Private Assistant — README

## 📦 Structure du projet

TRADING_BOT/
├── modules/ # Modules métier 
├── tests/ # Scénarios de test 
├── utils/ # Scripts de maintenance 
├── config/ # Fichiers de configuration 
├── exports/ # Fichiers générés 
├── replays/ # Relectures pédagogiques 
├── interface_pilotage/ # Interfaces CLI et Streamlit 
├── run_test.py # Script principal de test

## 🚀 Activation

- Lancer `activation_protocol.py` pour activer les modules verrouillés
- Utiliser `cli_launcher.py` pour lancer avec options

## 📋 Registre

- `module_registry.yaml` : statut, score, replay, export
- `bot_manifest.yaml` : modules actifs et fonctionnalités

## 🧪 Tests

- Chaque module possède un test dédié
- Replays et exports générés automatiquement

## 🎯 Objectif

Un assistant pédagogique, modulaire, traçable, et activable en production.
