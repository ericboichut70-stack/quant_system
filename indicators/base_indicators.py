"""
base_indicators.py – Calcul des indicateurs techniques
Contient les fonctions pour EMA, RSI, Énergie, Volume, Ruban 7 EMA.
Utilisé par les modules de stratégie et de backtest.
"""

import pandas as pd
import talib
import numpy as np

class IndicatorModule:
    """
    Module pour calculer les indicateurs techniques de base :
    EMA, RSI, et détection de volume élevé.
    """

    def __init__(self, ema_period=114, rsi_period=14, volume_ratio_thresh=1.5):
        self.ema_period = ema_period
        self.rsi_period = rsi_period
        self.volume_ratio_thresh = volume_ratio_thresh

    def calculate_ema(self, df):
        # Nettoyage et conversion
        if 'close' not in df.columns:
            raise ValueError("❌ La colonne 'close' est absente du DataFrame.")

        close = df['close'].squeeze()
        if not isinstance(close, pd.Series):
            raise TypeError(f"❌ df['close'] n'est pas une Series mais un {type(close)}")

        close = pd.to_numeric(close, errors='coerce').dropna()


        df['EMA'] = np.nan

        if len(close) >= self.ema_period:
            ema_values = talib.EMA(close.values.astype(float), timeperiod=self.ema_period)
            df.loc[close.index, 'EMA'] = ema_values

        return df

    def calculate_rsi(self, df):
        """
        Calcule le RSI sur la colonne 'close'
        """
        df['RSI'] = talib.RSI(df['close'], timeperiod=self.rsi_period)
        return df

    def detect_high_volume(self, df):
        """
        Détecte les volumes élevés par rapport à la moyenne mobile sur 20 périodes
        """
        df['VolumeAvg'] = df['volume'].rolling(window=20).mean()
        df['HighVolume'] = df['volume'] > df['VolumeAvg'] * self.volume_ratio_thresh
        return df

    def compute_indicators(self, df):
        """
        Pipeline complet : applique tous les indicateurs
        """
        df = df.copy()
        df = self.calculate_ema(df)
        df = self.calculate_rsi(df)
        df = self.detect_high_volume(df)
        return df

    def compute_signals(self, df):
        """
        Calcule les signaux d'achat/vente et le score IA
        """
        df = df.copy()

        # Signaux de base
        df['BuySignal'] = (df['close'] > df['EMA']) & (df['close'].shift(1) <= df['EMA'].shift(1))
        df['SellSignal'] = (df['close'] < df['EMA']) & (df['close'].shift(1) >= df['EMA'].shift(1))

        # Pattern chandelier simple : Engulfing haussier/baissier
        df['BullishEngulfing'] = (df['close'].shift(1) < df['open'].shift(1)) & \
                                 (df['close'] > df['open']) & \
                                 (df['close'] > df['open'].shift(1)) & \
                                 (df['open'] < df['close'].shift(1))

        df['BearishEngulfing'] = (df['close'].shift(1) > df['open'].shift(1)) & \
                                 (df['close'] < df['open']) & \
                                 (df['close'] < df['open'].shift(1)) & \
                                 (df['open'] > df['close'].shift(1))

        # Score IA basé sur 5 critères
        df['ScoreIA'] = 0
        df['ScoreIA'] += df['BuySignal'].astype(int) * 20
        df['ScoreIA'] += (df['RSI'] > 50).astype(int) * 20
        df['ScoreIA'] += df['HighVolume'].astype(int) * 20
        df['ScoreIA'] += df['BullishEngulfing'].astype(int) * 20
        df['ScoreIA'] += (df['close'] > df['low'].rolling(window=20).min()).astype(int) * 20  # au-dessus du support

        return df

    def compute_trade_management(self, df, trail_pct=1.0, sl_pct=1.5, tp_pct=3.0):
        """
        Calcule le trailing stop, SL et TP pour les signaux d'achat
        """
        df = df.copy()
        df['TrailStop'] = np.nan
        df['SL'] = np.nan
        df['TP'] = np.nan

        for i in range(1, len(df)):
            if df['BuySignal'].iloc[i]:
                entry_price = df['close'].iloc[i]
                df.at[df.index[i], 'TrailStop'] = entry_price * (1 - trail_pct / 100)
                df.at[df.index[i], 'SL'] = entry_price * (1 - sl_pct / 100)
                df.at[df.index[i], 'TP'] = entry_price * (1 + tp_pct / 100)
            else:
                prev_trail = df['TrailStop'].iloc[i - 1]
                if not np.isnan(prev_trail) and df['close'].iloc[i] > prev_trail:
                    df.at[df.index[i], 'TrailStop'] = df['close'].iloc[i] * (1 - trail_pct / 100)
                else:
                    df.at[df.index[i], 'TrailStop'] = prev_trail

        return df
