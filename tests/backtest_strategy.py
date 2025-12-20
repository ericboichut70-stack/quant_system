import backtrader as bt
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from trading_indicator import TradingIndicator

class TradingStrategy(bt.Strategy):
    """
    Stratégie de trading basée sur l'indicateur IA avec gestion des risques
    
    Intègre le money management avec risque de 1% par trade et position sizing
    """
    
    # Paramètres configurables de la stratégie
    params = (
        ('ema_length', 114),           # Période EMA principale
        ('rsi_length', 14),            # Période RSI
        ('volume_ratio_threshold', 1.5), # Seuil volume élevé
        ('trailing_stop_pct', 1.0),    # Trailing stop %
        ('stop_loss_pct', 1.5),        # Stop loss %
        ('take_profit_pct', 3.0),      # Take profit %
        ('sr_length', 20),             # Lookback zones S/R
        ('min_score_threshold', 70),   # Score IA minimum
        ('risk_per_trade', 0.01),      # Risque par trade (1%)
        ('max_positions', 3),          # Nombre max de positions simultanées
    )
    
    def __init__(self):
        """Initialise la stratégie et l'indicateur IA"""
        # Initialisation de l'indicateur avec les paramètres
        self.indicator = TradingIndicator(
            ema_length=self.params.ema_length,
            rsi_length=self.params.rsi_length,
            volume_ratio_threshold=self.params.volume_ratio_threshold,
            trailing_stop_pct=self.params.trailing_stop_pct,
            stop_loss_pct=self.params.stop_loss_pct,
            take_profit_pct=self.params.take_profit_pct,
            support_resistance_length=self.params.sr_length,
            min_score_threshold=self.params.min_score_threshold
        )
        
        # Variables de suivi des positions
        self.positions_count = 0
        self.entry_prices = []
        self.stop_losses = []
        self.take_profits = []
        self.trailing_stops = []
        
        # Statistiques de performance
        self.trades_log = []
        self.signals_log = []
        
    def next(self):
        """
        Logique principale exécutée à chaque barre
        Équivalent à la logique Pine Script avec alertes
        """
        # Conversion des données actuelles en DataFrame pour l'indicateur
        current_data = self._get_current_dataframe()
        
        # Calcul des indicateurs via notre classe
        enriched_data = self.indicator.compute(current_data)
        
        # Récupération des signaux de la dernière barre
        latest_signals = enriched_data.iloc[-1]
        
        # === GESTION DES SIGNAUX D'ACHAT ===
        if latest_signals['enhanced_buy_signal'] and self.positions_count < self.params.max_positions:
            self._execute_buy_signal(latest_signals)
        
        elif latest_signals['buy_signal'] and not latest_signals['enhanced_buy_signal']:
            # Signal d'achat basique (sans IA) - position plus petite
            self._execute_basic_buy_signal(latest_signals)
        
        # === GESTION DES SIGNAUX DE VENTE ===
        if latest_signals['sell_signal'] and self.position:
            self._execute_sell_signal(latest_signals)
        
        # === GESTION DU TRAILING STOP ===
        if self.position and not np.isnan(latest_signals['trailing_stop']):
            self._update_trailing_stop(latest_signals['trailing_stop'])
        
        # === GESTION STOP LOSS / TAKE PROFIT ===
        if self.position:
            self._check_stop_loss_take_profit(latest_signals)
    
    def _get_current_dataframe(self, lookback: int = 200) -> pd.DataFrame:
        """
        Convertit les données Backtrader en DataFrame pandas pour l'indicateur
        
        Args:
            lookback: Nombre de barres à inclure
            
        Returns:
            DataFrame avec colonnes OHLCV
        """
        # Récupération des données avec lookback suffisant
        size = min(len(self.data), lookback)
        
        data_dict = {
            'open': [self.data.open[-i] for i in range(size-1, -1, -1)],
            'high': [self.data.high[-i] for i in range(size-1, -1, -1)],
            'low': [self.data.low[-i] for i in range(size-1, -1, -1)],
            'close': [self.data.close[-i] for i in range(size-1, -1, -1)],
            'volume': [self.data.volume[-i] for i in range(size-1, -1, -1)]
        }
        
        # Création du DataFrame avec index temporel
        df = pd.DataFrame(data_dict)
        df.index = pd.date_range(end=pd.Timestamp.now(), periods=len(df), freq='D')
        
        return df
    
    def _calculate_position_size(self, entry_price: float, stop_loss_price: float) -> int:
        """
        Calcule la taille de position basée sur le risque de 1% par trade
        
        Args:
            entry_price: Prix d'entrée prévu
            stop_loss_price: Prix de stop loss
            
        Returns:
            Nombre d'actions à acheter
        """
        # Capital disponible
        available_cash = self.broker.get_cash()
        
        # Risque maximum par trade (1% du capital)
        max_risk_amount = available_cash * self.params.risk_per_trade
        
        # Risque par action (différence entre entrée et stop loss)
        risk_per_share = abs(entry_price - stop_loss_price)
        
        # Éviter division par zéro
        if risk_per_share == 0:
            return 0
        
        # Calcul de la taille de position
        position_size = int(max_risk_amount / risk_per_share)
        
        # Vérification que nous avons assez de capital
        total_cost = position_size * entry_price
        if total_cost > available_cash * 0.95:  # Garde 5% de marge
            position_size = int((available_cash * 0.95) / entry_price)
        
        return max(0, position_size)
    
    def _execute_buy_signal(self, signals: pd.Series) -> None:
        """
        Exécute un signal d'achat renforcé par l'IA
        
        Args:
            signals: Série avec tous les indicateurs calculés
        """
        current_price = self.data.close[0]
        stop_loss_price = current_price * (1 - self.params.stop_loss_pct / 100)
        
        # Calcul de la taille de position avec money management
        size = self._calculate_position_size(current_price, stop_loss_price)
        
        if size > 0:
            # Exécution de l'ordre d'achat
            order = self.buy(size=size)
            
            # Enregistrement des niveaux de sortie
            self.entry_prices.append(current_price)
            self.stop_losses.append(stop_loss_price)
            self.take_profits.append(current_price * (1 + self.params.take_profit_pct / 100))
            self.trailing_stops.append(signals['trailing_stop'])
            
            self.positions_count += 1
            
            # Log du signal (équivalent alertcondition Pine Script)
            self.signals_log.append({
                'date': self.data.datetime.date(0),
                'type': 'BUY_IA_ENHANCED',
                'price': current_price,
                'size': size,
                'ai_score': signals['ai_score'],
                'rsi': signals['rsi']
            })
    
    def _execute_basic_buy_signal(self, signals: pd.Series) -> None:
        """
        Exécute un signal d'achat basique (sans IA)
        
        Args:
            signals: Série avec tous les indicateurs calculés
        """
        current_price = self.data.close[0]
        stop_loss_price = current_price * (1 - self.params.stop_loss_pct / 100)
        
        # Position plus petite pour signal non confirmé par IA
        size = self._calculate_position_size(current_price, stop_loss_price) // 2
        
        if size > 0:
            order = self.buy(size=size)
            
            self.entry_prices.append(current_price)
            self.stop_losses.append(stop_loss_price)
            self.take_profits.append(current_price * (1 + self.params.take_profit_pct / 100))
            self.trailing_stops.append(signals['trailing_stop'])
            
            self.positions_count += 1
            
            self.signals_log.append({
                'date': self.data.datetime.date(0),
                'type': 'BUY_BASIC',
                'price': current_price,
                'size': size,
                'ai_score': signals['ai_score'],
                'rsi': signals['rsi']
            })
    
    def _execute_sell_signal(self, signals: pd.Series) -> None:
        """
        Exécute un signal de vente
        
        Args:
            signals: Série avec tous les indicateurs calculés
        """
        if self.position.size > 0:
            order = self.sell(size=self.position.size)
            
            self.signals_log.append({
                'date': self.data.datetime.date(0),
                'type': 'SELL',
                'price': self.data.close[0],
                'size': self.position.size,
                'ai_score': signals['ai_score'],
                'rsi': signals['rsi']
            })
    
    def _update_trailing_stop(self, new_trailing_stop: float) -> None:
        """
        Met à jour le trailing stop dynamique
        
        Args:
            new_trailing_stop: Nouvelle valeur du trailing stop
        """
        if self.position.size > 0 and len(self.trailing_stops) > 0:
            current_trailing = self.trailing_stops[-1]
            
            # Mise à jour si le nouveau trailing stop est plus élevé
            if not np.isnan(new_trailing_stop) and new_trailing_stop > current_trailing:
                self.trailing_stops[-1] = new_trailing_stop
    
    def _check_stop_loss_take_profit(self, signals: pd.Series) -> None:
        """
        Vérifie les conditions de stop loss et take profit
        
        Args:
            signals: Série avec tous les indicateurs calculés
        """
        if not self.position or len(self.stop_losses) == 0:
            return
        
        current_price = self.data.close[0]
        stop_loss = self.stop_losses[-1]
        take_profit = self.take_profits[-1]
        trailing_stop = self.trailing_stops[-1]
        
        # Vérification stop loss
        if current_price <= stop_loss:
            self.sell(size=self.position.size)
            self._log_trade_exit('STOP_LOSS', current_price)
        
        # Vérification take profit
        elif current_price >= take_profit:
            self.sell(size=self.position.size)
            self._log_trade_exit('TAKE_PROFIT', current_price)
        
        # Vérification trailing stop
        elif not np.isnan(trailing_stop) and current_price <= trailing_stop:
            self.sell(size=self.position.size)
            self._log_trade_exit('TRAILING_STOP', current_price)
    
    def _log_trade_exit(self, exit_type: str, exit_price: float) -> None:
        """
        Enregistre la sortie d'un trade
        
        Args:
            exit_type: Type de sortie (STOP_LOSS, TAKE_PROFIT, TRAILING_STOP)
            exit_price: Prix de sortie
        """
        if len(self.entry_prices) > 0:
            entry_price = self.entry_prices.pop()
            self.stop_losses.pop()
            self.take_profits.pop()
            self.trailing_stops.pop()
            
            pnl = (exit_price - entry_price) / entry_price * 100
            
            self.trades_log.append({
                'date': self.data.datetime.date(0),
                'entry_price': entry_price,
                'exit_price': exit_price,
                'exit_type': exit_type,
                'pnl_pct': pnl,
                'size': self.position.size
            })
            
            self.positions_count -= 1
    
    def notify_order(self, order):
        """Notification des ordres exécutés"""
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'ACHAT EXÉCUTÉ - Prix: {order.executed.price:.2f}, '
                        f'Taille: {order.executed.size}, Coût: {order.executed.value:.2f}')
            else:
                self.log(f'VENTE EXÉCUTÉE - Prix: {order.executed.price:.2f}, '
                        f'Taille: {order.executed.size}, Valeur: {order.executed.value:.2f}')
    
    def notify_trade(self, trade):
        """Notification des trades fermés"""
        if trade.isclosed:
            self.log(f'TRADE FERMÉ - PnL Brut: {trade.pnl:.2f}, '
                    f'PnL Net: {trade.pnlcomm:.2f}')
    
    def log(self, txt, dt=None):
        """Fonction de logging avec format français"""
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.strftime("%d/%m/%Y")}: {txt}')
    
    def get_performance_stats(self) -> Dict:
        """
        Retourne les statistiques de performance de la stratégie
        
        Returns:
            Dictionnaire avec métriques de performance
        """
        if not self.trades_log:
            return {}
        
        trades_df = pd.DataFrame(self.trades_log)
        
        # Calcul des métriques
        total_trades = len(trades_df)
        winning_trades = len(trades_df[trades_df['pnl_pct'] > 0])
        losing_trades = len(trades_df[trades_df['pnl_pct'] < 0])
        
        win_rate = (winning_trades / total_trades * 100) if total_trades > 0 else 0
        
        avg_win = trades_df[trades_df['pnl_pct'] > 0]['pnl_pct'].mean() if winning_trades > 0 else 0
        avg_loss = trades_df[trades_df['pnl_pct'] < 0]['pnl_pct'].mean() if losing_trades > 0 else 0
        
        profit_factor = abs(avg_win * winning_trades / (avg_loss * losing_trades)) if losing_trades > 0 else float('inf')
        
        return {
            'total_trades': total_trades,
            'winning_trades': winning_trades,
            'losing_trades': losing_trades,
            'win_rate': win_rate,
            'avg_win_pct': avg_win,
            'avg_loss_pct': avg_loss,
            'profit_factor': profit_factor,
            'total_pnl_pct': trades_df['pnl_pct'].sum(),
            'signals_generated': len(self.signals_log)
        }
