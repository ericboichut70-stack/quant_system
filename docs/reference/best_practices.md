# 🌟 Best Practices — Bonnes Pratiques Globales

Ce document regroupe les **meilleures pratiques** pour travailler efficacement avec le moteur quantitatif, les modules avancés, les interfaces et la documentation.

Il sert de guide transversal pour maintenir un projet propre, stable et évolutif.

---

## 🧭 1. Architecture & Organisation

- respecter la structure en couches  
- éviter les dépendances circulaires  
- isoler chaque responsabilité dans son dossier  
- documenter chaque module ajouté  
- maintenir une architecture modulaire  

---

## 🧱 2. Code & Développement

- respecter les conventions (`coding_standards.md`)  
- privilégier la lisibilité à l’optimisation prématurée  
- éviter les effets de bord  
- écrire des fonctions courtes et explicites  
- utiliser des noms clairs et cohérents  

---

## 🧪 3. Tests

- écrire des tests pour chaque module  
- utiliser des données minimales et reproductibles  
- tester les comportements, pas les implémentations  
- vérifier l’absence de lookahead  
- exécuter les tests avant chaque merge  

---

## 📊 4. Données & Indicateurs

- normaliser systématiquement les données  
- vérifier la cohérence temporelle  
- éviter les trous temporels  
- documenter les transformations  
- valider les indicateurs avancés  

---

## 🧠 5. Modules Quantitatifs

- séparer structure / volatilité / orderflow  
- éviter les modules monolithiques  
- documenter les signaux générés  
- tester la stabilité numérique  
- vérifier la reproductibilité  

---

## 🎯 6. Stratégie

- séparer filtrage / décision / gestion du risque  
- éviter les règles implicites  
- documenter les conditions d’entrée et de sortie  
- tester les scénarios extrêmes  

---

## 📈 7. Backtest

- simuler slippage, spread et frais  
- vérifier la cohérence des ordres  
- analyser les métriques clés  
- conserver les journaux  

---

## 📤 8. Exports

- utiliser des noms explicites  
- organiser les exports par type  
- éviter les fichiers volumineux dans Git  
- documenter les formats  

---

## 🖥️ 9. Interfaces

- séparer logique métier et interface  
- ne jamais modifier les données depuis l’interface  
- tester les dashboards  
- documenter les outils CLI  
