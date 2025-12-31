# 📤 Usage Guidelines — Bonnes Pratiques d’Export

Ce document décrit les **bonnes pratiques** pour utiliser, organiser et maintenir les exports générés par le moteur quantitatif, les modules avancés et les interfaces.

---

## 🧭 1. Principes Généraux

- ne jamais versionner les fichiers volumineux  
- organiser les exports par type  
- documenter les formats  
- nettoyer régulièrement les fichiers obsolètes  
- utiliser des noms explicites  

---

## 📂 2. Organisation Recommandée

exports/
visuals/
reports/
signals/
optimization/
logs/

---

## 🧱 3. Bonnes Pratiques par Type d’Export

## 3.1 CSV

- utiliser des noms explicites  
- inclure l’actif et la période  
- vérifier les colonnes obligatoires  

Exemple :
signals_BTCUSD_1h.csv

Code

## 3.2 JSON

- structurer les données  
- éviter les fichiers trop volumineux  
- utiliser pour les configurations et résumés  

## 3.3 Markdown

- idéal pour les rapports  
- compatible GitHub  
- facile à versionner  

## 3.4 Images

- stocker dans `visuals/`  
- utiliser des noms explicites  
- éviter les images trop lourdes  

---

## 🔧 4. Conventions de Nommage

- `YYYY-MM-DD_report.md`  
- `signals_<asset>_<period>.csv`  
- `optimization_results.csv`  
- `equity_curve.png`  

---

## 🧪 5. Tests

Les tests doivent vérifier :

- la validité des formats  
- la cohérence des données exportées  
- la compatibilité avec les dashboards  
- l’absence de corruption  
