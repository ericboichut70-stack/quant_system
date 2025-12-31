# 📘 `docs/reference/faq.md`

```markdown
# ❓ FAQ — Questions Fréquentes

Cette FAQ regroupe les questions les plus fréquentes concernant le moteur quantitatif, les modules, les interfaces et la documentation.

---

# 🧭 1. Général

## ❓ Comment est structuré le projet ?
Le projet est organisé en couches :
data → indicators → modules/quant → strategy → backtest → exports → interfaces

Chaque couche a une responsabilité unique.

## ❓ Où se trouve la documentation principale ?
Dans `docs/`, avec un index dans `docs/README.md`.

---

# 📊 2. Données & Indicateurs

## ❓ Quels formats de données sont supportés ?
CSV, JSON, Parquet, API externes.

## ❓ Comment éviter le lookahead ?
- alignement strict  
- décalage des indicateurs  
- validation temporelle  

---

# 🧠 3. Modules Quantitatifs

## ❓ Quels modules sont disponibles ?
- structure  
- volatilité  
- orderflow  
- signaux avancés  
- optimisation  

## ❓ Peut-on ajouter un module ?
Oui, chaque module est indépendant et extensible.

---

# 🎯 4. Stratégie

## ❓ Comment sont générés les signaux ?
À partir :
- des indicateurs  
- des modules quantitatifs  
- des filtres internes  

## ❓ Comment fonctionne la gestion du risque ?
Via :
- stop loss  
- take profit  
- sizing dynamique  

---

# 📈 5. Backtest

## ❓ Le backtest est-il réaliste ?
Oui : slippage, spread, frais, exécution simulée.

## ❓ Peut-on backtester plusieurs actifs ?
Oui, via le pipeline multi‑actifs.

---

# 🖥️ 6. Interfaces

## ❓ Comment lancer un dashboard ?
streamlit run interface/<dashboard>.py

## ❓ Les interfaces modifient-elles les données ?
Non, elles sont en lecture seule.

---

# 📤 7. Exports

## ❓ Quels formats sont disponibles ?
CSV, JSON, Markdown, PNG.

## ❓ Où sont stockés les logs ?
Dans `exports/logs/`.
