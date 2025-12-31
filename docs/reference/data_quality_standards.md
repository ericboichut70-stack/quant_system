# 📊 Data Quality Standards — Normes de Qualité des Données

Ce document définit les **standards de qualité** que doivent respecter toutes les données utilisées dans le moteur quantitatif.

Il garantit la fiabilité, la cohérence et la robustesse du pipeline.

---

## 🧭 1. Principes Généraux

- données propres  
- données cohérentes  
- données complètes  
- données normalisées  
- données vérifiées  

---

## 🧱 2. Normes de Qualité

## 2.1 Cohérence Temporelle

- timestamps strictement ordonnés  
- aucune valeur future utilisée  
- pas de duplications  

## 2.2 Complétude

- absence de trous temporels  
- gestion explicite des NaN  
- vérification des colonnes obligatoires  

## 2.3 Normalisation

- colonnes standardisées :  
  `open`, `high`, `low`, `close`, `volume`  
- index temporel propre  
- fréquence homogène  

## 2.4 Validation

- types corrects  
- valeurs plausibles  
- absence d’anomalies extrêmes  
- vérification des formats  

---

## 🧪 3. Tests de Qualité

- tests unitaires sur les loaders  
- tests d’intégration sur le pipeline  
- tests de cohérence multi‑timeframes  
- tests de reproductibilité  

---

## 🧬 4. Bonnes Pratiques

- documenter les sources  
- éviter les conversions inutiles  
- nettoyer avant enrichissement  
- valider avant utilisation  
