# 🌐 Market Regimes — Régimes de Marché

Ce document décrit les **régimes de marché** utilisés pour contextualiser les signaux, les modules quantitatifs et les stratégies.

Les régimes permettent d’adapter :

- les signaux  
- les filtres  
- la gestion du risque  
- les décisions  

---

## 🧭 1. Définition d’un Régime de Marché

Un régime de marché est un **état global** du marché, défini par :

- volatilité  
- direction  
- structure  
- momentum  
- liquidité  

---

## 🧱 2. Types de Régimes

## 2.1 Tendance Haussière (Bull Trend)

- sommets et creux ascendants  
- volatilité modérée  
- momentum positif  

## 2.2 Tendance Baissière (Bear Trend)

- sommets et creux descendants  
- volatilité modérée  
- momentum négatif  

## 2.3 Range / Consolidation

- absence de direction  
- faible momentum  
- structure horizontale  

## 2.4 Volatilité Élevée

- mouvements rapides  
- swings larges  
- risques accrus  

## 2.5 Volatilité Faible

- compression  
- signaux faibles  
- faible liquidité  

---

## 🧬 3. Détection des Régimes

- structure (modules quantitatifs)  
- volatilité (ATR, variance)  
- momentum (ROC, RSI)  
- clustering (optionnel ML)  

---

## 🎯 4. Utilisation dans la Stratégie

- filtrage des signaux  
- ajustement du sizing  
- modification des stops  
- activation/désactivation de modules  
