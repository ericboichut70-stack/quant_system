# 🧪 Testing Guidelines — Bonnes Pratiques de Tests

Ce document définit les **principes, méthodes et bonnes pratiques** pour tester le moteur quantitatif, les modules avancés, les interfaces et les exports.

Il complète le dossier `tests/` et garantit une approche cohérente et professionnelle.

---

## 🧭 1. Objectifs des Tests

Les tests doivent permettre de :

- détecter les régressions  
- garantir la stabilité du moteur  
- valider les comportements attendus  
- sécuriser les évolutions futures  
- assurer la reproductibilité  
- vérifier la cohérence temporelle (pas de lookahead)  

---

## 🧱 2. Types de Tests

## 2.1 Tests Unitaires

Portent sur :

- fonctions isolées  
- modules simples  
- transformations de données  
- indicateurs  

Objectif : **valider un comportement précis**.

## 2.2 Tests Fonctionnels

Portent sur :

- modules quantitatifs  
- stratégie  
- backtest  
- exports  

Objectif : **valider un flux complet**.

## 2.3 Tests d’Intégration

Portent sur :

- pipeline complet  
- interactions entre couches  
- cohérence des signaux  

Objectif : **valider l’ensemble du moteur**.

---

## 🔧 3. Données de Test

- utiliser des datasets minimaux  
- reproductibles  
- sans dépendance externe  
- éviter les appels API dans les tests  
- privilégier des données synthétiques  

---

## 🧬 4. Tests du Pipeline Quantitatif

Les tests doivent vérifier :

- cohérence temporelle  
- absence de lookahead  
- alignement des signaux  
- compatibilité entre couches  
- stabilité des métriques  

---

## 📊 5. Tests des Modules Quantitatifs

Vérifier :

- cohérence des signaux  
- stabilité numérique  
- gestion des NaN  
- robustesse aux trous temporels  
- reproductibilité  

---

## 🖥️ 6. Tests des Interfaces

Pour les dashboards :

- chargement correct  
- absence d’erreurs Streamlit  
- compatibilité avec les exports  

Pour les CLI :

- menus stables  
- gestion des erreurs  
- cohérence des actions  

---

## 🧪 7. Organisation des Tests

tests/
test_data.py
test_indicators.py
test_quant_modules.py
test_strategy.py
test_backtest.py
test_exports.py
test_interfaces.py
