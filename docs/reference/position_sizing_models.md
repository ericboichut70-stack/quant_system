# 📏 Position Sizing Models — Modèles de Dimensionnement des Positions

Ce document présente les principaux modèles de **position sizing** utilisés dans les stratégies quantitatives.  
Il sert de référence pour concevoir des stratégies robustes et cohérentes.

---

## 🧭 1. Principes Généraux

- le sizing doit être cohérent avec le risque  
- le sizing doit être stable dans le temps  
- le sizing doit s’adapter à la volatilité  
- le sizing doit éviter les extrêmes  

---

## 🧱 2. Modèles Classiques

## 2.1 Fixed Fractional

\[
\text{Taille} = \text{Capital} \times \text{Risque\%}
\]

Simple, robuste, adapté aux stratégies directionnelles.

---

## 2.2 Fixed Dollar Risk

\[
\text{Taille} = \frac{\text{Risque Fixe}}{\text{Distance Stop}}
\]

Très utilisé en trading institutionnel.

---

## 2.3 Volatility-Based Sizing

\[
\text{Taille} = \frac{K}{ATR}
\]

Permet d’ajuster la taille selon la volatilité.

---

## 🧬 3. Modèles Avancés

## 3.1 Kelly Criterion (version simplifiée)

\[
f^* = p - \frac{q}{r}
\]

Puissant mais instable → utiliser une fraction de Kelly.

---

## 3.2 Risk Parity

\[
\text{Taille} \propto \frac{1}{\sigma}
\]

Utilisé dans les portefeuilles multi‑actifs.

---

## 3.3 Volatility Targeting

\[
\text{Taille} = \frac{\text{Vol Cible}}{\text{Vol Réalisée}}
\]

Très utilisé en gestion systématique.

---

## 🧪 4. Tests de Robustesse

- stress tests  
- variations de volatilité  
- changements de régimes  
- perturbations temporelles  
