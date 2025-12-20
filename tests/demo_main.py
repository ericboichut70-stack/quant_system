#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemple d'utilisation complète de l'indicateur de trading IA
Convertit la logique Pine Script en Python avec backtesting complet

Auteur: Cascade AI
Date: 30/08/2025
"""

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

from trading_indicator import TradingIndicator
from backtest_strategy import TradingStrategy
from parameter_optimizer import ParameterOptimizer
import backtrader as bt

def generate_sample_data(symbol: str = "AAPL", period: str = "5y") -> pd.DataFrame:
    """
    Génère des données OHLCV sample via Yahoo Finance
    
    Args:
        symbol: Symbole à télécharger (défaut: AAPL)
        period: Période de données (1y, 2y, 5y, max)
        
    Returns:
        DataFrame avec colonnes OHLCV et index datetime
    """
    print(f"📊 Téléchargement des données {symbol} sur {period}...")
    
    try:
        # Téléchargement via yfinance
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period)
        
        # Nettoyage et formatage
        data.columns = data.columns.str.lower()
        data = data.dropna()
        
        print(f"✅ {len(data)} barres téléchargées du {data.index[0].strftime('%d/%m/%Y')} au {data.index[-1].strftime('%d/%m/%Y')}")
        
        return data
        
    except Exception as e:
        print(f"❌ Erreur lors du téléchargement: {e}")
        print("🔄 Génération de données synthétiques...")
        return generate_synthetic_data()

def generate_synthetic_data(n_days: int = 1000) -> pd.DataFrame:
    """
    Génère des données OHLCV synthétiques pour les tests
    
    Args:
        n_days: Nombre de jours à générer
        
    Returns:
        DataFrame avec données synthétiques
    """
    # Paramètres de simulation
    np.random.seed(42)
    initial_price = 100.0
    volatility = 0.02
    trend = 0.0002
    
    # Génération des rendements avec tendance et volatilité
    returns = np.random.normal(trend, volatility, n_days)
    prices = [initial_price]
    
    for ret in returns:
        prices.append(prices[-1] * (1 + ret))
    
    prices = np.array(prices[1:])  # Supprime le prix initial
    
    # Génération OHLC basée sur les prix de clôture
    data = []
    for i, close in enumerate(prices):
        # Variation intraday aléatoire
        daily_range = close * np.random.uniform(0.005, 0.03)
        
        high = close + np.random.uniform(0, daily_range)
        low = close - np.random.uniform(0, daily_range)
        
        # Open basé sur le close précédent avec gap
        if i == 0:
            open_price = close * np.random.uniform(0.99, 1.01)
        else:
            open_price = prices[i-1] * np.random.uniform(0.995, 1.005)
        
        # Volume aléatoire avec corrélation aux mouvements
        price_change = abs(close - open_price) / open_price
        base_volume = 1000000
        volume = int(base_volume * (1 + price_change * 5) * np.random.uniform(0.5, 2.0))
        
        data.append({
            'open': open_price,
            'high': max(open_price, high, close),
            'low': min(open_price, low, close),
            'close': close,
            'volume': volume
        })
    
    # Création du DataFrame avec index temporel
    df = pd.DataFrame(data)
    df.index = pd.date_range(end=datetime.now(), periods=len(df), freq='D')
    
    print(f"✅ {len(df)} barres synthétiques générées")
    
    return df

def demo_basic_usage():
    """Démonstration de l'utilisation basique de l'indicateur"""
    print("\n" + "="*60)
    print("🚀 DÉMONSTRATION - UTILISATION BASIQUE")
    print("="*60)
    
    # Génération des données
    data = generate_sample_data("AAPL", "2y")
    
    # Initialisation de l'indicateur avec paramètres par défaut
    indicator = TradingIndicator()
    
    # Calcul des indicateurs
    enriched_data = indicator.compute(data)
    
    # Affichage des statistiques
    print(f"\n📈 STATISTIQUES DES SIGNAUX:")
    print(f"• Signaux d'achat basiques: {enriched_data['buy_signal'].sum()}")
    print(f"• Signaux de vente: {enriched_data['sell_signal'].sum()}")
    print(f"• Signaux IA renforcés: {enriched_data['enhanced_buy_signal'].sum()}")
    print(f"• Score IA moyen: {enriched_data['ai_score'].mean():.1f}")
    print(f"• RSI moyen: {enriched_data['rsi'].mean():.1f}")
    
    # Visualisation
    print(f"\n📊 Génération des graphiques...")
    indicator.plot_analysis(enriched_data, start_date='2023-01-01')
    indicator.plot_performance_summary(enriched_data)
    
    # Export des signaux
    indicator.export_signals_to_csv(enriched_data, 'signaux_demo.csv')
    
    return enriched_data

def demo_backtesting():
    """Démonstration du backtesting avec différentes périodes"""
    print("\n" + "="*60)
    print("🎯 DÉMONSTRATION - BACKTESTING MULTI-PÉRIODES")
    print("="*60)
    
    # Test sur différentes périodes et actifs
    test_configs = [
        {"symbol": "AAPL", "period": "2y", "name": "Apple 2 ans"},
        {"symbol": "MSFT", "period": "3y", "name": "Microsoft 3 ans"},
        {"symbol": "GOOGL", "period": "1y", "name": "Google 1 an"},
    ]
    
    results_summary = []
    
    for config in test_configs:
        print(f"\n🔍 Test: {config['name']}")
        print("-" * 40)
        
        # Chargement des données
        data = generate_sample_data(config['symbol'], config['period'])
        
        # Configuration du backtest
        cerebro = bt.Cerebro()
        data_feed = bt.feeds.PandasData(dataname=data)
        cerebro.adddata(data_feed)
        
        # Ajout de la stratégie
        cerebro.addstrategy(TradingStrategy)
        
        # Configuration du broker
        initial_cash = 100000
        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=0.001)
        
        # Ajout des analyseurs
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
        
        # Exécution
        results = cerebro.run()
        strategy = results[0]
        
        # Extraction des métriques
        final_value = cerebro.broker.getvalue()
        total_return = (final_value - initial_cash) / initial_cash * 100
        
        sharpe = strategy.analyzers.sharpe.get_analysis().get('sharperatio', 0)
        if sharpe is None:
            sharpe = 0
            
        drawdown = strategy.analyzers.drawdown.get_analysis().get('max', {}).get('drawdown', 0)
        
        trades_info = strategy.analyzers.trades.get_analysis()
        total_trades = trades_info.get('total', {}).get('total', 0)
        won_trades = trades_info.get('won', {}).get('total', 0)
        win_rate = (won_trades / total_trades * 100) if total_trades > 0 else 0
        
        # Affichage des résultats
        print(f"💰 Capital final: {final_value:,.2f}€")
        print(f"📈 Rendement total: {total_return:.2f}%")
        print(f"📊 Ratio de Sharpe: {sharpe:.2f}")
        print(f"📉 Drawdown max: {drawdown:.2f}%")
        print(f"🎯 Trades gagnants: {won_trades}/{total_trades} ({win_rate:.1f}%)")
        
        # Sauvegarde pour comparaison
        results_summary.append({
            'config': config['name'],
            'symbol': config['symbol'],
            'final_value': final_value,
            'total_return_pct': total_return,
            'sharpe_ratio': sharpe,
            'max_drawdown_pct': drawdown,
            'win_rate_pct': win_rate,
            'total_trades': total_trades
        })
    
    # Comparaison des résultats
    print(f"\n📊 COMPARAISON DES PERFORMANCES:")
    print("-" * 60)
    comparison_df = pd.DataFrame(results_summary)
    print(comparison_df.to_string(index=False, float_format='%.2f'))
    
    return comparison_df

def demo_optimization():
    """Démonstration de l'optimisation des paramètres"""
    print("\n" + "="*60)
    print("🔧 DÉMONSTRATION - OPTIMISATION DES PARAMÈTRES")
    print("="*60)
    
    # Chargement des données pour optimisation
    data = generate_sample_data("AAPL", "3y")
    
    # Initialisation de l'optimiseur
    optimizer = ParameterOptimizer(data, initial_cash=100000)
    
    # Lancement de l'optimisation (limitée pour la démo)
    print("⚡ Optimisation rapide avec 100 combinaisons...")
    results = optimizer.optimize_parameters(max_combinations=100)
    
    if not results.empty:
        # Affichage des meilleures configurations
        print(f"\n🏆 TOP 5 - RATIO DE SHARPE:")
        best_sharpe = optimizer.get_best_parameters('sharpe_ratio', 5)
        for i, (_, row) in enumerate(best_sharpe.iterrows(), 1):
            params = row['params']
            print(f"{i}. Sharpe: {row['sharpe_ratio']:.3f} | "
                  f"EMA: {params['ema_length']} | "
                  f"RSI: {params['rsi_length']} | "
                  f"Score min: {params['min_score_threshold']}")
        
        print(f"\n🎯 TOP 5 - TAUX DE RÉUSSITE:")
        best_winrate = optimizer.get_best_parameters('win_rate_pct', 5)
        for i, (_, row) in enumerate(best_winrate.iterrows(), 1):
            params = row['params']
            print(f"{i}. Win rate: {row['win_rate_pct']:.1f}% | "
                  f"Trades: {row['total_trades']} | "
                  f"Rendement: {row['total_return_pct']:.2f}%")
        
        # Visualisation des résultats
        optimizer.plot_optimization_results()
        
        # Export des résultats
        optimizer.export_results('optimization_demo.csv')
        
        # Suggestions d'amélioration
        suggestions = optimizer.suggest_improvements()
        print(f"\n💡 SUGGESTIONS D'AMÉLIORATION:")
        for key, suggestion in suggestions.items():
            print(f"• {key.upper()}: {suggestion}")
    
    return results

def demo_money_management():
    """Démonstration de la gestion des risques et money management"""
    print("\n" + "="*60)
    print("💰 DÉMONSTRATION - MONEY MANAGEMENT")
    print("="*60)
    
    # Test avec différents niveaux de risque
    risk_levels = [0.005, 0.01, 0.02, 0.03]  # 0.5%, 1%, 2%, 3%
    data = generate_sample_data("AAPL", "2y")
    
    risk_results = []
    
    for risk in risk_levels:
        print(f"\n🎲 Test avec risque {risk*100:.1f}% par trade:")
        
        # Configuration du backtest
        cerebro = bt.Cerebro()
        data_feed = bt.feeds.PandasData(dataname=data)
        cerebro.adddata(data_feed)
        
        # Stratégie avec niveau de risque spécifique
        cerebro.addstrategy(TradingStrategy, risk_per_trade=risk)
        
        cerebro.broker.setcash(100000)
        cerebro.broker.setcommission(commission=0.001)
        
        # Analyseurs
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
        
        # Exécution
        results = cerebro.run()
        strategy = results[0]
        
        final_value = cerebro.broker.getvalue()
        total_return = (final_value - 100000) / 100000 * 100
        max_drawdown = strategy.analyzers.drawdown.get_analysis().get('max', {}).get('drawdown', 0)
        
        print(f"  💰 Rendement: {total_return:.2f}%")
        print(f"  📉 Drawdown max: {max_drawdown:.2f}%")
        print(f"  📊 Ratio rendement/risque: {total_return/max_drawdown:.2f}" if max_drawdown > 0 else "  📊 Ratio: ∞")
        
        risk_results.append({
            'risk_pct': risk * 100,
            'return_pct': total_return,
            'drawdown_pct': max_drawdown,
            'risk_adjusted_return': total_return / max_drawdown if max_drawdown > 0 else float('inf')
        })
    
    # Analyse comparative
    risk_df = pd.DataFrame(risk_results)
    print(f"\n📊 ANALYSE COMPARATIVE DU RISQUE:")
    print(risk_df.to_string(index=False, float_format='%.2f'))
    
    return risk_df

def main():
    """Fonction principale - Exécute toutes les démonstrations"""
    print("🎯 INDICATEUR DE TRADING IA - DÉMONSTRATION COMPLÈTE")
    print("Conversion Pine Script → Python avec backtesting avancé")
    print("=" * 80)
    
    try:
        # 1. Utilisation basique
        basic_data = demo_basic_usage()
        
        # 2. Backtesting multi-périodes
        backtest_results = demo_backtesting()
        
        # 3. Optimisation des paramètres
        optimization_results = demo_optimization()
        
        # 4. Money management
        risk_results = demo_money_management()
        
        print("\n" + "="*80)
        print("✅ DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
        print("="*80)
        
        print("\n📁 FICHIERS GÉNÉRÉS:")
        print("• signaux_demo.csv - Signaux de la démo basique")
        print("• optimization_demo.csv - Résultats d'optimisation")
        
        print("\n🎯 PROCHAINES ÉTAPES SUGGÉRÉES:")
        print("• Tester sur vos propres données de marché")
        print("• Ajuster les paramètres selon vos préférences de risque")
        print("• Intégrer des indicateurs supplémentaires (MACD, ATR)")
        print("• Implémenter des filtres de tendance long terme")
        print("• Tester sur différentes unités de temps (4H, 1D, 1W)")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
