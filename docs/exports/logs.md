# 🧾 Logs — Documentation des Journaux (`exports/`)

Ce document décrit la structure, le rôle et les bonnes pratiques liées aux **journaux (logs)** générés par le moteur quantitatif, les modules avancés et les interfaces.

Les logs constituent une source essentielle pour :

- le débogage  
- l’audit  
- la traçabilité  
- la compréhension des comportements internes  
- l’analyse post‑exécution  

---

## 🧭 1. Types de Logs

## 1.1 Logs de Backtest

Contiennent :

- ordres exécutés  
- prix d’entrée / sortie  
- taille des positions  
- PnL par trade  
- erreurs éventuelles  
- métriques intermédiaires  

Exemple :
2025-01-03 10:00: BUY 100 AAPL @ 182.50
2025-01-03 11:15: SELL 100 AAPL @ 184.20  PnL: +1.70

## 1.2 Logs de Stratégie

Contiennent :

- signaux reçus  
- filtres appliqués  
- décisions prises  
- raisons des rejets  

Exemple :
Signal BUY rejeté : score IA insuffisant (68 < 70)

Code

## 1.3 Logs des Modules Quantitatifs

Contiennent :

- structure détectée  
- swings  
- volatilité  
- orderflow  
- signaux avancés  

## 1.4 Logs des Interfaces

Contiennent :

- actions utilisateur  
- erreurs Streamlit  
- interactions CLI  
- chargements de fichiers  

---

## 📂 2. Organisation Recommandée

exports/
logs/
backtest/
strategy/
quant_modules/
interfaces/

Code

---

## 🧱 3. Formats Supportés

- `.log` (texte brut)  
- `.json` (structuré)  
- `.md` (rapports lisibles)  

---

## 🔧 4. Bonnes Pratiques

- timestamp obligatoire  
- messages courts et explicites  
- niveaux de log (`INFO`, `WARNING`, `ERROR`)  
- pas de données sensibles  
- rotation des logs si volumineux  
