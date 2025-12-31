# 📊 Documentation — Couche Données (`data/`)

Ce document décrit en détail la couche **données** du moteur quantitatif.  
Il complète le README du dossier `data/` en offrant une vue plus technique et plus approfondie.

---

## 🧭 1. Rôle de la Couche Données

La couche `data/` constitue la **fondation** du moteur quantitatif.  
Elle garantit que toutes les couches supérieures reçoivent des données :

- propres  
- cohérentes  
- normalisées  
- complètes  
- sans trous temporels  
- sans duplications  

---

## 🧱 2. Pipeline de Données

Le pipeline suit les étapes suivantes :

1. **Ingestion**
   - CSV, API, flux externes
   - formats OHLCV standardisés

2. **Nettoyage**
   - suppression des valeurs aberrantes  
   - correction des timestamps  
   - gestion des NaN  

3. **Normalisation**
   - colonnes standardisées (`open`, `high`, `low`, `close`, `volume`)  
   - index temporel propre  
   - fréquence homogène  

4. **Validation**
   - cohérence temporelle  
   - absence de trous  
   - absence de doublons  
   - vérification des types  

5. **Préparation**
   - enrichissement éventuel  
   - alignement multi‑timeframes  
   - formats prêts pour les indicateurs  

---

## 📂 3. Structure du Dossier

Le dossier peut contenir :

- `loader.py`  
- `cleaner.py`  
- `validator.py`  
- `normalizer.py`  
- `data_sources/`  
- `sample_data/`  

Les fichiers volumineux doivent être exclus via `.gitignore`.

---

## 🔧 4. Formats Supportés

## Formats d’entrée

- CSV  
- JSON  
- Parquet  
- API (yfinance, brokers, flux temps réel)

## Formats internes

- DataFrame Pandas  
- Index temporel  
- colonnes normalisées  

## Formats de sortie

- DataFrame enrichies  
- données prêtes pour les indicateurs  

---

## 🧪 5. Tests et Validation

Les tests doivent vérifier :

- la cohérence des colonnes  
- la validité des timestamps  
- la gestion des NaN  
- la compatibilité avec les indicateurs  
- la reproductibilité  

---

## 🧭 6. Intégration avec les autres couches

data/ → indicators/ → modules/quant/ → strategy/ → backtest/

La couche données est **strictement en amont**.
