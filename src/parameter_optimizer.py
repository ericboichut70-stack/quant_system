"""
parameter_optimizer.py – Optimisation des paramètres
Utilise Optuna ou d’autres algorithmes pour trouver les meilleurs paramètres EMA, RSI, etc.
"""

import backtrader as bt
import pandas as pd
import numpy as np
from itertools import product
from typing import Dict, List, Tuple, Any
import matplotlib.pyplot as plt
from backtest_strategy import TradingStrategy
import warnings
warnings.filterwarnings('ignore')

class ParameterOptimizer:
    """
    Optimiseur de paramètres via grid search pour la stratégie de trading IA
    
    Permet de tester différentes combinaisons de paramètres et d'identifier
    les configurations optimales selon diverses métriques de performance.
    """
    
    def __init__(self, data: pd.DataFrame, initial_cash: float = 100000):
        """
        Initialise l'optimiseur avec les données de marché
        
        Args:
            data: DataFrame avec colonnes OHLCV et index datetime
            initial_cash: Capital initial pour les backtests (défaut: 100k€)
        """
        self.data = data
        self.initial_cash = initial_cash
        self.optimization_results = []
        
    def define_parameter_grid(self) -> Dict[str, List]:
        """
        Définit la grille de paramètres à optimiser
        
        Returns:
            Dictionnaire avec les paramètres et leurs valeurs à tester
        """
        parameter_grid = {
            'ema_length': [50, 89, 114, 144, 200],  # Périodes EMA variées
            'rsi_length': [10, 14, 18, 21],         # Périodes RSI
            'volume_ratio_threshold': [1.2, 1.5, 2.0, 2.5],  # Seuils volume
            'trailing_stop_pct': [0.5, 1.0, 1.5, 2.0],       # Trailing stop %
            'stop_loss_pct': [1.0, 1.5, 2.0, 2.5],           # Stop loss %
            'take_profit_pct': [2.0, 3.0, 4.0, 5.0],         # Take profit %
            'min_score_threshold': [60, 70, 80, 90],          # Score IA minimum
            'risk_per_trade': [0.005, 0.01, 0.015, 0.02]     # Risque par trade
        }
        
        return parameter_grid
    
    def run_single_backtest(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Exécute un backtest avec un jeu de paramètres spécifique
        
        Args:
            params: Dictionnaire des paramètres à tester
            
        Returns:
            Dictionnaire avec les résultats de performance
        """
        # Configuration du moteur Backtrader
        cerebro = bt.Cerebro()
        
        # Ajout des données
        data_feed = bt.feeds.PandasData(dataname=self.data)
        cerebro.adddata(data_feed)
        
        # Configuration de la stratégie avec les paramètres
        cerebro.addstrategy(TradingStrategy, **params)
        
        # Configuration du broker
        cerebro.broker.setcash(self.initial_cash)
        cerebro.broker.setcommission(commission=0.001)  # 0.1% de commission
        
        # Ajout des analyseurs de performance
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
        
        # Exécution du backtest
        try:
            results = cerebro.run()
            strategy = results[0]
            
            # Extraction des métriques
            sharpe_ratio = strategy.analyzers.sharpe.get_analysis().get('sharperatio', 0)
            if sharpe_ratio is None:
                sharpe_ratio = 0
                
            drawdown_info = strategy.analyzers.drawdown.get_analysis()
            max_drawdown = drawdown_info.get('max', {}).get('drawdown', 0)
            
            returns_info = strategy.analyzers.returns.get_analysis()
            total_return = returns_info.get('rtot', 0) * 100  # En pourcentage
            
            trades_info = strategy.analyzers.trades.get_analysis()
            total_trades = trades_info.get('total', {}).get('total', 0)
            won_trades = trades_info.get('won', {}).get('total', 0)
            win_rate = (won_trades / total_trades * 100) if total_trades > 0 else 0
            
            # Valeur finale du portefeuille
            final_value = cerebro.broker.getvalue()
            
            return {
                'params': params.copy(),
                'final_value': final_value,
                'total_return_pct': total_return,
                'sharpe_ratio': sharpe_ratio,
                'max_drawdown_pct': max_drawdown,
                'total_trades': total_trades,
                'win_rate_pct': win_rate,
                'profit_factor': self._calculate_profit_factor(strategy),
                'success': True
            }
            
        except Exception as e:
            return {
                'params': params.copy(),
                'error': str(e),
                'success': False
            }
    
    def _calculate_profit_factor(self, strategy) -> float:
        """
        Calcule le profit factor à partir des statistiques de la stratégie
        
        Args:
            strategy: Instance de la stratégie exécutée
            
        Returns:
            Profit factor (gains totaux / pertes totales)
        """
        try:
            trades_info = strategy.analyzers.trades.get_analysis()
            won_info = trades_info.get('won', {})
            lost_info = trades_info.get('lost', {})
            
            total_won = won_info.get('pnl', {}).get('total', 0)
            total_lost = abs(lost_info.get('pnl', {}).get('total', 0))
            
            if total_lost > 0:
                return total_won / total_lost
            else:
                return float('inf') if total_won > 0 else 0
                
        except:
            return 0
    
    def optimize_parameters(self, max_combinations: int = 500) -> pd.DataFrame:
        """
        Lance l'optimisation complète via grid search
        
        Args:
            max_combinations: Nombre maximum de combinaisons à tester
            
        Returns:
            DataFrame avec tous les résultats triés par performance
        """
        print("🚀 Démarrage de l'optimisation des paramètres...")
        
        # Génération de la grille de paramètres
        param_grid = self.define_parameter_grid()
        
        # Génération de toutes les combinaisons possibles
        param_names = list(param_grid.keys())
        param_values = list(param_grid.values())
        all_combinations = list(product(*param_values))
        
        # Limitation du nombre de combinaisons si nécessaire
        if len(all_combinations) > max_combinations:
            print(f"⚠️ Limitation à {max_combinations} combinaisons sur {len(all_combinations)} possibles")
            # Échantillonnage aléatoire pour diversité
            np.random.seed(42)
            selected_indices = np.random.choice(len(all_combinations), max_combinations, replace=False)
            all_combinations = [all_combinations[i] for i in selected_indices]
        
        print(f"📊 Test de {len(all_combinations)} combinaisons de paramètres...")
        
        # Exécution des backtests
        results = []
        for i, combination in enumerate(all_combinations):
            # Création du dictionnaire de paramètres
            params = dict(zip(param_names, combination))
            
            # Exécution du backtest
            result = self.run_single_backtest(params)
            results.append(result)
            
            # Affichage du progrès
            if (i + 1) % 50 == 0 or i == len(all_combinations) - 1:
                success_rate = sum(1 for r in results if r['success']) / len(results) * 100
                print(f"Progrès: {i+1}/{len(all_combinations)} ({success_rate:.1f}% réussis)")
        
        # Filtrage des résultats réussis
        successful_results = [r for r in results if r['success']]
        
        if not successful_results:
            print("❌ Aucun backtest réussi!")
            return pd.DataFrame()
        
        # Conversion en DataFrame
        results_df = pd.DataFrame(successful_results)
        
        # Tri par ratio de Sharpe décroissant
        results_df = results_df.sort_values('sharpe_ratio', ascending=False)
        
        # Sauvegarde des résultats
        self.optimization_results = results_df
        
        print(f"✅ Optimisation terminée! {len(successful_results)} configurations testées avec succès")
        
        return results_df
    
    def get_best_parameters(self, metric: str = 'sharpe_ratio', top_n: int = 5) -> pd.DataFrame:
        """
        Retourne les meilleures configurations selon une métrique
        
        Args:
            metric: Métrique de sélection ('sharpe_ratio', 'total_return_pct', 'win_rate_pct')
            top_n: Nombre de meilleures configurations à retourner
            
        Returns:
            DataFrame avec les meilleures configurations
        """
        if self.optimization_results.empty:
            print("⚠️ Aucun résultat d'optimisation disponible")
            return pd.DataFrame()
        
        # Tri selon la métrique choisie
        ascending = metric in ['max_drawdown_pct']  # Drawdown : plus petit = mieux
        sorted_results = self.optimization_results.sort_values(metric, ascending=ascending)
        
        return sorted_results.head(top_n)
    
    def plot_optimization_results(self) -> None:
        """
        Affiche les graphiques d'analyse des résultats d'optimisation
        """
        if self.optimization_results.empty:
            print("⚠️ Aucun résultat d'optimisation à afficher")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Analyse des Résultats d\'Optimisation', fontsize=16, fontweight='bold')
        
        # === DISTRIBUTION DU RATIO DE SHARPE ===
        ax1.hist(self.optimization_results['sharpe_ratio'], bins=30, alpha=0.7, 
                color='steelblue', edgecolor='black')
        ax1.axvline(x=self.optimization_results['sharpe_ratio'].mean(), 
                   color='red', linestyle='--', label='Moyenne')
        ax1.set_xlabel('Ratio de Sharpe')
        ax1.set_ylabel('Fréquence')
        ax1.set_title('Distribution du Ratio de Sharpe')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # === CORRÉLATION RENDEMENT VS DRAWDOWN ===
        ax2.scatter(self.optimization_results['max_drawdown_pct'], 
                   self.optimization_results['total_return_pct'], 
                   alpha=0.6, color='green', s=20)
        ax2.set_xlabel('Drawdown Maximum (%)')
        ax2.set_ylabel('Rendement Total (%)')
        ax2.set_title('Rendement vs Risque')
        ax2.grid(True, alpha=0.3)
        
        # === IMPACT DE L'EMA SUR LA PERFORMANCE ===
        ema_performance = self.optimization_results.groupby(
            self.optimization_results['params'].apply(lambda x: x['ema_length'])
        )['sharpe_ratio'].mean()
        
        ema_performance.plot(kind='bar', ax=ax3, color='orange', alpha=0.7)
        ax3.set_xlabel('Période EMA')
        ax3.set_ylabel('Ratio de Sharpe Moyen')
        ax3.set_title('Impact de la Période EMA')
        ax3.tick_params(axis='x', rotation=45)
        ax3.grid(True, alpha=0.3)
        
        # === TAUX DE RÉUSSITE VS NOMBRE DE TRADES ===
        ax4.scatter(self.optimization_results['total_trades'], 
                   self.optimization_results['win_rate_pct'], 
                   alpha=0.6, color='purple', s=20)
        ax4.set_xlabel('Nombre Total de Trades')
        ax4.set_ylabel('Taux de Réussite (%)')
        ax4.set_title('Activité vs Précision')
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def export_results(self, filename: str = 'optimization_results.csv') -> None:
        """
        Exporte les résultats d'optimisation vers un fichier CSV
        
        Args:
            filename: Nom du fichier de sortie
        """
        if self.optimization_results.empty:
            print("⚠️ Aucun résultat à exporter")
            return
        
        # Préparation des données pour l'export
        export_data = []
        for _, row in self.optimization_results.iterrows():
            export_row = row['params'].copy()
            export_row.update({
                'final_value': row['final_value'],
                'total_return_pct': row['total_return_pct'],
                'sharpe_ratio': row['sharpe_ratio'],
                'max_drawdown_pct': row['max_drawdown_pct'],
                'total_trades': row['total_trades'],
                'win_rate_pct': row['win_rate_pct'],
                'profit_factor': row['profit_factor']
            })
            export_data.append(export_row)
        
        export_df = pd.DataFrame(export_data)
        export_df.to_csv(filename, sep=';', decimal=',', index=False)
        
        print(f"✅ Résultats exportés vers {filename}")
        print(f"📊 {len(export_df)} configurations exportées")
    
    def suggest_improvements(self) -> Dict[str, str]:
        """
        Analyse les résultats et suggère des améliorations
        
        Returns:
            Dictionnaire avec suggestions d'amélioration
        """
        if self.optimization_results.empty:
            return {"erreur": "Aucun résultat d'optimisation disponible"}
        
        suggestions = {}
        
        # Analyse du meilleur ratio de Sharpe
        best_sharpe = self.optimization_results.iloc[0]
        if best_sharpe['sharpe_ratio'] < 1.0:
            suggestions['sharpe'] = "Ratio de Sharpe faible. Considérer l'ajout de MACD ou ATR pour filtrer les signaux."
        
        # Analyse du drawdown
        avg_drawdown = self.optimization_results['max_drawdown_pct'].mean()
        if avg_drawdown > 15:
            suggestions['drawdown'] = "Drawdown élevé. Réduire la taille des positions ou resserrer les stops."
        
        # Analyse du nombre de trades
        avg_trades = self.optimization_results['total_trades'].mean()
        if avg_trades < 10:
            suggestions['activite'] = "Peu de signaux générés. Assouplir les critères du score IA ou réduire la période EMA."
        elif avg_trades > 100:
            suggestions['overtrading'] = "Trop de signaux. Renforcer les filtres ou augmenter le score IA minimum."
        
        # Analyse du taux de réussite
        avg_win_rate = self.optimization_results['win_rate_pct'].mean()
        if avg_win_rate < 40:
            suggestions['precision'] = "Taux de réussite faible. Ajouter des filtres de tendance ou améliorer le timing d'entrée."
        
        # Suggestions d'indicateurs supplémentaires
        suggestions['indicateurs'] = "Considérer l'ajout de MACD, ATR, ou Bollinger Bands pour améliorer la précision."
        suggestions['timeframes'] = "Tester sur différentes unités de temps (4H, 1D, 1W) pour validation."
        
        return suggestions
