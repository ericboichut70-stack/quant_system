# 🔊 Audio Tools — Interfaces Audio (`interface_pilotage/`)

Ce document décrit les **interfaces audio** du projet, situées dans `interface_pilotage/`.  
Elles permettent d’interagir avec le système via des éléments sonores, narratifs ou vocaux.

---

## 🧭 1. Rôle des Interfaces Audio

Les interfaces audio permettent :

- de générer des narrations  
- de lire des résumés  
- d’accompagner les dashboards  
- de guider l’utilisateur dans des scénarios  
- de renforcer l’aspect pédagogique  

Elles sont utilisées dans :

- `streamlit_manifest_audio.py`  
- modules narratifs  
- interfaces mentorales  

---

## 📂 2. Composants Principaux

## 2.1 `streamlit_manifest_audio.py`

- lecture audio de manifestes  
- narration de scénarios  
- intégration dans Streamlit  

## 2.2 Modules Narratifs

- génération de textes  
- transformation en audio  
- lecture séquentielle  

## 2.3 Outils Internes

- gestion des fichiers audio  
- conversion texte → audio  
- intégration dans les interfaces  

---

## 🔧 3. Architecture Fonctionnelle

Les interfaces audio s’appuient sur :

- `exports/` (fichiers audio générés)  
- `documentation_md/` (contenus narratifs)  
- `utils/` (helpers audio)  

Elles ne modifient jamais la logique métier.

---

## 🎨 4. Cas d’Usage

- narration d’un rapport  
- lecture d’un manifeste  
- accompagnement d’un dashboard  
- guidage dans une quête  
- validation mentorale  

---

## 🧪 5. Tests

Les tests doivent vérifier :

- la génération correcte des fichiers audio  
- la lecture dans Streamlit  
- la compatibilité avec les exports  
- la stabilité des modules narratifs  
