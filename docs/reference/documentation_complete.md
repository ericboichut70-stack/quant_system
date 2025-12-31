# 🎯 Indicateur de Trading IA - GPT Pro EMA 114

Conversion complète du script Pine Script en Python avec architecture modulaire, backtesting avancé et optimisation des paramètres.

## 📋 Table des Matières

- [🚀 Installation](#-installation)
- [🏗️ Architecture](#️-architecture)
- [📊 Fonctionnalités](#-fonctionnalités)
- [💡 Utilisation Rapide](#-utilisation-rapide)
- [🔧 Configuration](#-configuration)
- [📈 Backtesting](#-backtesting)
- [⚡ Optimisation](#-optimisation)
- [📁 Structure du Projet](#-structure-du-projet)
- [🎯 Exemples](#-exemples)
- [🔍 Métriques de Performance](#-métriques-de-performance)
- [💰 Money Management](#-money-management)
- [🛠️ Améliorations Suggérées](#️-améliorations-suggérées)

## 🚀 Installation

### Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Installation de TA-Lib (Windows)

```bash
# Option 1: Via pip (recommandé)
pip install talib-binary

# Option 2: Si problème, installer depuis les wheels
# Télécharger le fichier .whl approprié depuis https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
pip install TA_Lib-0.4.24-cp39-cp39-win_amd64.whl
```

## 🏗️ Architecture

Le projet suit une architecture modulaire pour faciliter la maintenance et l'évolutivité :

```bash
├── trading_indicator.py     # Classe principale des indicateurs
├── backtest_strategy.py     # Stratégie Backtrader avec money management
├── parameter_optimizer.py   # Optimisation via grid search
├── main_example.py         # Exemples d'utilisation complète
├── requirements.txt        # Dépendances
└── README.md              # Documentation
```

### Composants Principaux

1. **TradingIndicator** : Calculs des indicateurs techniques et signaux
2. **TradingStrategy** : Stratégie de trading avec gestion des risques
3. **ParameterOptimizer** : Optimisation des paramètres via grid search

## 📊 Fonctionnalités

### ✅ Indicateurs Techniques

- **EMA 114** : Moyenne mobile exponentielle principale
- **RSI 14** : Relative Strength Index
- **Zones Support/Résistance** : Détection automatique
- **Volume Analysis** : Détection des volumes élevés
- **Patterns Chandeliers** : Bullish/Bearish Engulfing

### ✅ Système de Scoring IA

Score basé sur 5 critères (20 points chacun) :

- Signal d'achat EMA
- RSI > 50 (momentum haussier)
- Volume élevé (> 1.5x moyenne)
- Pattern bullish engulfing
- Prix au-dessus du support

### ✅ Gestion des Risques

- **Trailing Stop** : Dynamique et configurable
- **Stop Loss** : Pourcentage fixe
- **Take Profit** : Objectif de gain
- **Position Sizing** : Basé sur le risque (1% par trade)
- **Money Management** : Limitation du nombre de positions

### ✅ Visualisation

- Graphiques multi-panneaux avec zones colorées
- Signaux visuels (flèches, étoiles)
- Statistiques de performance
- Export CSV des signaux

## 💡 Utilisation Rapide

### Exemple Basique

```python
from trading_indicator import TradingIndicator
import pandas as pd

# Chargement des données (format OHLCV)
data = pd.read_csv('votre_fichier.csv', index_col=0, parse_dates=True)

# Initialisation de l'indicateur
indicator = TradingIndicator()

# Calcul des signaux
enriched_data = indicator.compute(data)

# Visualisation
indicator.plot_analysis(enriched_data)

# Export des signaux
indicator.export_signals_to_csv(enriched_data, 'signaux.csv')
```

### Démonstration Complète

```bash
python main_example.py
```

## 🔧 Configuration

### Paramètres de l'Indicateur

```python
indicator = TradingIndicator(
    ema_length=114,                    # Période EMA principale
    rsi_length=14,                     # Période RSI
    volume_ratio_threshold=1.5,        # Seuil volume élevé (x moyenne)
    trailing_stop_pct=1.0,             # Trailing stop (%)
    stop_loss_pct=1.5,                 # Stop loss (%)
    take_profit_pct=3.0,               # Take profit (%)
    support_resistance_length=20,      # Lookback zones S/R
    min_score_threshold=70             # Score IA minimum
)
```

### Paramètres de Money Management

```python
strategy_params = {
    'risk_per_trade': 0.01,           # Risque par trade (1%)
    'max_positions': 3,               # Positions simultanées max
}
```

## 📈 Backtesting

### Backtest Simple

```python
import backtrader as bt
from backtest_strategy import TradingStrategy

# Configuration
cerebro = bt.Cerebro()
cerebro.adddata(bt.feeds.PandasData(dataname=data))
cerebro.addstrategy(TradingStrategy)
cerebro.broker.setcash(100000)
cerebro.broker.setcommission(commission=0.001)

# Exécution
results = cerebro.run()
```

### Backtest Multi-Périodes

Le fichier `main_example.py` inclut des exemples de backtesting sur :

- Différents actifs (AAPL, MSFT, GOOGL)
- Différentes périodes (1 an, 2 ans, 3 ans)
- Différents niveaux de risque

## ⚡ Optimisation

### Grid Search Automatique

```python
from parameter_optimizer import ParameterOptimizer

# Initialisation
optimizer = ParameterOptimizer(data, initial_cash=100000)

# Optimisation (500 combinaisons max)
results = optimizer.optimize_parameters(max_combinations=500)

# Meilleures configurations
best_configs = optimizer.get_best_parameters('sharpe_ratio', top_n=5)

# Visualisation des résultats
optimizer.plot_optimization_results()

# Export
optimizer.export_results('optimization_results.csv')
```

### Grille de Paramètres

L'optimiseur teste automatiquement :

- **EMA Length** : [50, 89, 114, 144, 200]
- **RSI Length** : [10, 14, 18, 21]
- **Volume Threshold** : [1.2, 1.5, 2.0, 2.5]
- **Trailing Stop** : [0.5%, 1.0%, 1.5%, 2.0%]
- **Stop Loss** : [1.0%, 1.5%, 2.0%, 2.5%]
- **Take Profit** : [2.0%, 3.0%, 4.0%, 5.0%]
- **Score IA Min** : [60, 70, 80, 90]
- **Risque/Trade** : [0.5%, 1.0%, 1.5%, 2.0%]

## 📁 Structure du Projet

```bash
trading-indicator-ia/
│
├── trading_indicator.py      # 🎯 Classe principale
│   ├── calculate_base_indicators()
│   ├── detect_basic_signals()
│   ├── calculate_support_resistance_zones()
│   ├── detect_volume_patterns()
│   ├── detect_candlestick_patterns()
│   ├── calculate_ai_score()
│   ├── calculate_trailing_stop()
│   ├── calculate_stop_loss_take_profit()
│   ├── compute()                    # Pipeline complet
│   ├── plot_analysis()              # Visualisation
│   └── export_signals_to_csv()      # Export
│
├── backtest_strategy.py       # 📊 Stratégie Backtrader
│   ├── __init__()                   # Configuration
│   ├── next()                       # Logique principale
│   ├── _calculate_position_size()   # Money management
│   ├── _execute_buy_signal()        # Exécution achats
│   ├── _execute_sell_signal()       # Exécution ventes
│   └── get_performance_stats()      # Statistiques
│
├── parameter_optimizer.py     # ⚡ Optimisation
│   ├── define_parameter_grid()      # Grille de paramètres
│   ├── run_single_backtest()        # Backtest unitaire
│   ├── optimize_parameters()        # Grid search
│   ├── get_best_parameters()        # Meilleures configs
│   ├── plot_optimization_results()  # Visualisation
│   └── suggest_improvements()       # Suggestions IA
│
├── main_example.py           # 🚀 Démonstrations
│   ├── generate_sample_data()       # Données sample
│   ├── demo_basic_usage()           # Usage basique
│   ├── demo_backtesting()           # Backtests multi-périodes
│   ├── demo_optimization()          # Optimisation
│   └── demo_money_management()      # Gestion risques
│
├── requirements.txt          # 📦 Dépendances
└── README.md                # 📚 Documentation
```

## 🎯 Exemples

### 1. Analyse Technique Simple

```python
# Chargement et analyse
data = generate_sample_data("AAPL", "2y")
indicator = TradingIndicator()
results = indicator.compute(data)

# Statistiques
print(f"Signaux d'achat: {results['buy_signal'].sum()}")
print(f"Signaux IA: {results['enhanced_buy_signal'].sum()}")
print(f"Score IA moyen: {results['ai_score'].mean():.1f}")
```

### 2. Backtest avec Métriques

```python
# Configuration avancée
cerebro = bt.Cerebro()
cerebro.addstrategy(TradingStrategy, 
                   ema_length=89,
                   min_score_threshold=80,
                   risk_per_trade=0.015)

# Analyseurs de performance
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')

results = cerebro.run()
```

### 3. Optimisation Ciblée

```python
# Optimisation sur métrique spécifique
optimizer = ParameterOptimizer(data)
results = optimizer.optimize_parameters(max_combinations=200)

# Tri par drawdown minimum
best_low_risk = optimizer.get_best_parameters('max_drawdown_pct', 5)
```

## 🔍 Métriques de Performance

### Métriques Calculées

- **Ratio de Sharpe** : Rendement ajusté du risque
- **Drawdown Maximum** : Perte maximale depuis un pic
- **Taux de Réussite** : % de trades gagnants
- **Profit Factor** : Gains totaux / Pertes totales
- **Rendement Total** : Performance globale
- **Nombre de Trades** : Activité de la stratégie

### Interprétation

- **Sharpe > 1.0** : Bonne performance ajustée du risque
- **Drawdown < 15%** : Risque acceptable
- **Win Rate > 50%** : Stratégie précise
- **Profit Factor > 1.5** : Gains supérieurs aux pertes

## 💰 Money Management

### Principe du 1% de Risque

```python
# Calcul automatique de la taille de position
def _calculate_position_size(self, entry_price, stop_loss_price):
    available_cash = self.broker.get_cash()
    max_risk = available_cash * 0.01  # 1% du capital
    risk_per_share = abs(entry_price - stop_loss_price)
    position_size = int(max_risk / risk_per_share)
    return position_size
```

### Avantages

- **Protection du Capital** : Limite les pertes par trade
- **Consistance** : Risque uniforme sur tous les trades
- **Évolutivité** : S'adapte à la croissance du capital
- **Psychologie** : Réduit le stress émotionnel

## 🛠️ Améliorations Suggérées

### Indicateurs Supplémentaires

```python
# Exemples d'extensions possibles
def add_macd_filter(self, df):
    """Ajouter MACD pour confirmation de tendance"""
    macd, signal, hist = ta.MACD(df['close'])
    return macd > signal  # Signal haussier

def add_atr_volatility(self, df):
    """Ajouter ATR pour ajuster les stops"""
    atr = ta.ATR(df['high'], df['low'], df['close'])
    return atr  # Pour stops dynamiques

def add_bollinger_bands(self, df):
    """Ajouter Bollinger Bands pour sur-achat/vente"""
    upper, middle, lower = ta.BBANDS(df['close'])
    return df['close'] < lower  # Signal de survente
```

### Filtres de Tendance

- **EMA 200** : Filtre de tendance long terme
- **ADX** : Force de la tendance
- **Ichimoku** : Analyse multi-temporelle

### Timeframes Multiples

- **Analyse 4H** : Tendance intermédiaire
- **Analyse 1D** : Tendance principale
- **Analyse 1W** : Tendance long terme

## 📞 Support et Contribution

### Problèmes Courants

1. **Erreur TA-Lib** : Installer `talib-binary` au lieu de `TA-Lib`
2. **Données manquantes** : Vérifier la connexion internet pour yfinance
3. **Performance lente** : Réduire `max_combinations` dans l'optimiseur

### Améliorations Futures

- [ ] Interface graphique (GUI)
- [ ] Trading en temps réel
- [ ] Intégration API brokers
- [ ] Machine Learning avancé
- [ ] Alertes automatiques

---

**Développé par Cascade AI** - Conversion Pine Script → Python  
**Version** : 1.0.0  
**Date** : 30/08/2025  

🎯 **Objectif** : Fournir un indicateur de trading professionnel, modulaire et évolutif pour l'analyse technique automatisée.
