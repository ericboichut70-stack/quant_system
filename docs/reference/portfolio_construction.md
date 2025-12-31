# 🧺 Portfolio Construction — Construction de Portefeuille

Ce document présente les principes et méthodes pour construire un portefeuille quantitatif robuste, diversifié et cohérent avec les signaux du moteur.

---

## 🧭 1. Principes Généraux

- diversification intelligente  
- allocation cohérente avec le risque  
- corrélations maîtrisées  
- stabilité dans le temps  
- adaptation aux régimes de marché  

---

## 🧱 2. Méthodes d’Allocation

## 2.1 Allocation Égale (Equal Weight)

Simple, robuste, mais peu optimisée.

## 2.2 Allocation par Volatilité (Volatility Weighting)

\[
w_i = \frac{1/\sigma_i}{\sum_j 1/\sigma_j}
\]

## 2.3 Risk Parity

Chaque actif contribue de manière égale au risque global.

## 2.4 Mean‑Variance Optimization (Markowitz)

\[
\min_w w^T \Sigma w - \lambda \mu^T w
\]

## 2.5 Maximum Diversification

\[
\max_w \frac{w^T \sigma}{\sqrt{w^T \Sigma w}}
\]

---

## 🧬 3. Contraintes

- limites par actif  
- limites par secteur  
- limites par volatilité  
- limites de corrélation  

---

## 🧪 4. Tests de Robustesse

- stress tests  
- variations de corrélations  
- changements de régimes  
- perturbations de volatilité  
