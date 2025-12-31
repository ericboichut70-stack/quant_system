# 🧑‍💻 Coding Standards — Normes de Développement

Ce document définit les **standards de code** utilisés dans le projet.  
Il garantit la cohérence, la lisibilité et la maintenabilité du code.

---

## 🧭 1. Style Général

- respecter PEP8  
- indentation : 4 espaces  
- lignes ≤ 88 caractères  
- noms explicites  
- pas de logique complexe dans une seule ligne  
- éviter les effets de bord  

---

## 🧱 2. Nommage

## 2.1 Fichiers

- `snake_case.py`  
- noms courts mais explicites  

## 2.2 Fonctions

- `compute_signal()`  
- `calculate_volatility()`  

## 2.3 Classes

- `CamelCase`  
- `BacktestEngine`, `TrendDetector`  

## 2.4 Variables

- `snake_case`  
- éviter les abréviations obscures  

---

## 🔧 3. Documentation

## 3.1 Docstrings

Format recommandé : Google Style

```python
def compute_signal(df):
    """
    Compute trading signal based on EMA and RSI.

    Args:
        df (DataFrame): Input OHLCV data.

    Returns:
        DataFrame: Enriched data with signal columns.
    """
3.2 Commentaires

expliquer le pourquoi, pas le comment

éviter les commentaires inutiles

🧪 4. Tests

un test par comportement

pas de dépendances externes non contrôlées

données minimales et reproductibles

tests rapides

🧬 5. Organisation du Code

5.1 Modules

un module = une responsabilité

éviter les modules fourre‑tout

5.2 Imports

imports standard

imports externes

imports internes

jamais d’imports circulaires

🧭 6. Gestion des Exceptions

lever des exceptions explicites

ne jamais masquer une erreur

logs clairs

✔️ Statut d’intégration
Ce fichier doit être placé dans :

Code
docs/dev_guides/coding_standards.md
Code

---

# 📘 `docs/quant_engine/pipeline_overview.md`

```markdown
# 🔄 Pipeline Overview — Moteur Quantitatif

Ce document présente une vue d’ensemble du **pipeline complet** du moteur quantitatif, depuis les données brutes jusqu’aux exports.

---

# 🧭 1. Vue Globale du Pipeline

data/ → indicators/ → modules/quant/ → strategy/ → backtest/ → exports/

Code

Chaque couche enrichit la précédente.

---

# 🧱 2. Étapes du Pipeline

## 2.1 Données (`data/`)

- ingestion  
- nettoyage  
- normalisation  
- validation  

## 2.2 Indicateurs (`indicators/`)

- EMA, RSI, ATR  
- signaux techniques  
- features enrichies  

## 2.3 Modules Quantitatifs (`modules/quant/`)

- structure de marché  
- volatilité  
- orderflow  
- signaux avancés  
- optimisation  

## 2.4 Stratégie (`strategy/`)

- règles d’entrée  
- règles de sortie  
- gestion du risque  
- génération d’ordres  

## 2.5 Backtest (`backtest/`)

- simulation historique  
- métriques  
- journaux  
- analyse des trades  

## 2.6 Exports (`exports/`)

- rapports  
- CSV / JSON  
- visuels  
- audits  

---

# 🧬 3. Flux d’Information (Mermaid)

```mermaid
flowchart LR

    A[Data] --> B[Indicators]
    B --> C[Quant Modules]
    C --> D[Strategy]
    D --> E[Backtest]
    E --> F[Exports]

🧪 4. Tests du Pipeline

Les tests doivent vérifier :

cohérence temporelle

absence de lookahead

compatibilité entre couches

reproductibilité
