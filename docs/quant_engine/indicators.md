# 📊 Documentation — Couche Indicateurs (`indicators/`)

Ce document décrit en profondeur la couche **indicateurs** du moteur quantitatif.  
Il complète le README du dossier `indicators/` en offrant une vue technique, détaillée et structurée.

---

## 🧭 1. Rôle de la Couche Indicateurs

La couche `indicators/` transforme les données brutes en **features exploitables** par :

- les modules quantitatifs (`modules/quant/`)
- la stratégie (`strategy/`)
- le backtest (`backtest/`)

Elle constitue la **seconde couche** du pipeline, juste après `data/`.

---

## 🧱 2. Types d’Indicateurs

## 2.1 Indicateurs de Base

- EMA, SMA  

- RSI  
- ATR  
- Volumes  
- Variations, dérivées  
- Normalisations  

## 2.2 Indicateurs Avancés

- énergie (phoebus_energy)  

- pivots UT  
- signaux composites  
- volatilité dérivée  
- signaux multi‑timeframes  

## 2.3 Indicateurs Structurels

Utilisés par les modules quantitatifs :

- swings  
- zones clés  
- impulsions  
- compressions  

---

## 🔧 3. Pipeline des Indicateurs

Le pipeline suit les étapes suivantes :

1. **Préparation**
   - alignement temporel  
   - gestion des NaN  
   - normalisation  

2. **Calcul**
   - application des formules  
   - calcul vectorisé  
   - gestion des décalages  

3. **Enrichissement**
   - signaux booléens  
   - signaux multi‑niveaux  
   - signaux composites  

4. **Validation**
   - absence de lookahead  
   - cohérence temporelle  
   - compatibilité avec les modules  

---

## 📂 4. Structure du Dossier

Le dossier peut contenir :

- `base_indicators.py`  
- `phoebus_energy.py`  
- `ut_pivots.py`  
- `normalization.py`  
- `signal_utils.py`  
- `index.md` (documentation locale)

---

## 🧪 5. Tests et Validation

Les tests doivent vérifier :

- la cohérence des valeurs  
- l’absence de lookahead bias  
- la stabilité numérique  
- la compatibilité avec les modules quantitatifs  
- la reproductibilité  

---

## 🧭 6. Intégration avec les autres couches

data/ → indicators/ → modules/quant/ → strategy/ → backtest/

Les indicateurs sont **strictement en amont** des modules quantitatifs.
