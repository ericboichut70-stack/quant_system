# 📐 Indicator Math — Formules Détaillées des Indicateurs

Ce document regroupe les **formules mathématiques** des indicateurs utilisés dans le moteur quantitatif.  
Il sert de référence pour les développeurs, chercheurs et auditeurs.

---

## 🧭 1. Moyennes Mobiles

## 1.1 SMA — Simple Moving Average

\[
SMA_t = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}
\]

## 1.2 EMA — Exponential Moving Average

\[
EMA_t = \alpha P_t + (1 - \alpha) EMA_{t-1}
\]

où  

\[
\alpha = \frac{2}{n+1}
\]

---

## 🧭 2. Volatilité

## 2.1 ATR — Average True Range

\[
TR_t = \max
\begin{cases}
H_t - L_t \\
|H_t - C_{t-1}| \\
|L_t - C_{t-1}|
\end{cases}
\]

\[
ATR_t = EMA(TR_t)
\]

---

## 🧭 3. Oscillateurs

## 3.1 RSI — Relative Strength Index

\[
RSI = 100 - \frac{100}{1 + RS}
\]

où  

\[
RS = \frac{\text{Moyenne des gains}}{\text{Moyenne des pertes}}
\]

---

## 🧭 4. Momentum

## 4.1 ROC — Rate of Change

\[
ROC_t = \frac{P_t - P_{t-n}}{P_{t-n}} \times 100
\]

---

## 🧭 5. Normalisations

## 5.1 Z‑Score

\[
Z_t = \frac{X_t - \mu}{\sigma}
\]

## 5.2 Min‑Max Scaling

\[
X' = \frac{X - X_{min}}{X_{max} - X_{min}}
\]

---

## 🧭 6. Indicateurs Avancés

## 6.1 Phoebus Energy (exemple générique)

\[
Energy_t = \frac{|P_t - EMA_t|}{ATR_t}
\]

## 6.2 Pivots UT

\[
Pivot = \frac{H + L + C}{3}
\]
