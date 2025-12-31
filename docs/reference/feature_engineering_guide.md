# 🧬 Feature Engineering Guide — Guide de Construction de Features

Ce document décrit les bonnes pratiques pour créer des **features** robustes, informatives et adaptées au moteur quantitatif ou aux modèles ML.

---

## 🧭 1. Principes Généraux

- chaque feature doit avoir une justification  
- éviter les features redondantes  
- éviter les fuites de données  
- normaliser systématiquement  
- tester la stabilité  

---

## 🧱 2. Types de Features

## 2.1 Features Basées sur les Prix

- variations  
- retours log  
- dérivées  
- volatilité  

## 2.2 Features Basées sur les Indicateurs

- EMA / SMA  
- RSI / ATR  
- signaux techniques  

## 2.3 Features Structurelles

- swings  
- pivots  
- structure UT  
- zones  

## 2.4 Features Orderflow

- pression acheteurs/vendeurs  
- déséquilibres  
- volumes anormaux  

## 2.5 Features Multi‑Timeframes

- signaux synchronisés  
- volatilité multi‑niveaux  
- structure multi‑UT  

---

## 🧪 3. Normalisation

- z‑score  
- min‑max  
- robust scaling  
- normalisation par volatilité  

---

## 🧬 4. Tests de Qualité

- corrélations  
- importance des features  
- stabilité temporelle  
- robustesse aux trous  

---

## 🧠 5. Anti‑Patterns

- sur‑ingénierie  
- duplication de signaux  
- fuites temporelles  
- dépendances circulaires  
