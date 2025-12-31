# 📈 Documentation — Couche Backtest (`backtest/`)

Ce document décrit en profondeur la couche **backtest**, responsable de la simulation historique des stratégies.  
Il complète le README du dossier `backtest/` en offrant une vue technique, détaillée et structurée.

---

## 🧭 1. Rôle du Backtest

Le backtest permet de :

- simuler l’exécution d’une stratégie sur des données historiques  
- mesurer la performance réelle d’un ensemble de règles  
- analyser la robustesse, la stabilité et la cohérence des signaux  
- comparer différentes variantes de stratégie  
- identifier les faiblesses structurelles  

Il constitue la **validation empirique** du moteur quantitatif.

---

## 🧱 2. Pipeline du Backtest

Le pipeline suit les étapes suivantes :

1. **Préparation**
   - chargement des données  
   - alignement des signaux  
   - initialisation du capital  

2. **Simulation**
   - exécution des ordres  
   - gestion du risque  
   - gestion des positions  
   - prise en compte des frais, slippage, spread  

3. **Analyse**
   - calcul des métriques  
   - génération des journaux  
   - analyse des trades  

4. **Export**
   - rapports  
   - CSV / JSON  
   - visualisations  

---

## 📂 3. Structure du Dossier

Le dossier peut contenir :

- `backtest_engine.py`  
- `order_simulator.py`  
- `metrics.py`  
- `trade_log.py`  
- `config.py`  

---

## 📊 4. Métriques de Performance

Les métriques typiques incluent :

- rendement total  
- drawdown maximum  
- ratio de Sharpe  
- profit factor  
- taux de réussite  
- expectancy  
- nombre de trades  
- distribution des gains/pertes  

---

## 🔧 5. Intégration avec les autres couches

data/ → indicators/ → modules/quant/ → strategy/ → backtest/ → exports/

Le backtest dépend de :

- la stratégie  
- les signaux  
- les modules quantitatifs  
- les données propres  

Il fournit en retour :

- des métriques  
- des journaux  
- des exports  
- des diagnostics  

---

## 🧪 6. Tests et Validation

Les tests doivent vérifier :

- absence de lookahead  
- cohérence temporelle  
- exécution correcte des ordres  
- stabilité des métriques  
- reproductibilité des résultats  
