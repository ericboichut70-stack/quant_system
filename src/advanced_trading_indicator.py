#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Indicateur de Trading IA Avancé - Version Complète
Intègre MACD, ATR, Bollinger Bands, EMA 200, ADX, ML scoring, walk-forward et optimisation bayésienne

Auteur: Cascade AI
Date: 31/08/2025
"""

import pandas as pd
import numpy as np
import talib as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from typing import Dict, Tuple, Optional, List, Any
import warnings
warnings.filterwarnings('ignore')

# Machine Learning et optimisation
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score, precision_score, recall_score
from skopt import gp_minimize
from skopt.space import Real, Integer
from skopt.utils import use_named_args

# Backtesting
import backtrader as bt
from itertools import product
import yfinance as yf
from datetime import datetime, timedelta

class AdvancedTradingIndicator:
    """
    Indicateur de trading IA avancé avec tous les indicateurs techniques modernes
    et système de machine learning pour scoring optimisé
    """
    
    def __init__(self, 
                 # Paramètres techniques de base
                 ema_length: int = 114,
                 rsi_length: int = 14,
                 volume_ratio_threshold: float = 1.5,
                 
                 # Nouveaux indicateurs avancés
                 macd_fast: int = 12,
                 macd_slow: int = 26,
                 macd_signal: int = 9,
                 atr_length: int = 14,
                 bb_length: int = 20,
                 bb_std: float = 2.0,
                 ema_long: int = 200,
                 adx_length: int = 14,
                 
                 # Paramètres de gestion des risques
                 base_stop_loss_pct: float = 1.5,
                 base_take_profit_pct: float = 3.0,
                 atr_multiplier: float = 2.0,
                 
                 # Paramètres ML
                 use_ml_scoring: bool = True,
                 ml_lookback: int = 50,
                 
                 # Paramètres de trading
                 support_resistance_length: int = 20,
                 min_score_threshold: int = 70):
        """
        Initialise l'indicateur avancé avec tous les paramètres
        """
        # Paramètres techniques de base
        self.ema_length = ema_length
        self.rsi_length = rsi_length
        self.volume_ratio_threshold = volume_ratio_threshold
        
        # Nouveaux indicateurs
        self.macd_fast = macd_fast
        self.macd_slow = macd_slow
        self.macd_signal = macd_signal
        self.atr_length = atr_length
        self.bb_length = bb_length
        self.bb_std = bb_std
        self.ema_long = ema_long
        self.adx_length = adx_length
        
        # Gestion des risques avancée
        self.base_stop_loss_pct = base_stop_loss_pct
        self.base_take_profit_pct = base_take_profit_pct
        self.atr_multiplier = atr_multiplier
        
        # Machine Learning
        self.use_ml_scoring = use_ml_scoring
        self.ml_lookback = ml_lookback
        self.ml_model = None
        self.scaler = StandardScaler()
        
        # Autres paramètres
        self.sr_length = support_resistance_length
        self.min_score_threshold = min_score_threshold
        
    def calculate_base_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcule les indicateurs techniques de base et avancés"""
        # Indicateurs de base existants
        df['ema_main'] = ta.EMA(df['close'].values, timeperiod=self.ema_length)
        df['rsi'] = ta.RSI(df['close'].values, timeperiod=self.rsi_length)
        df['volume_avg'] = ta.SMA(df['volume'].values, timeperiod=20)
        
        # === NOUVEAUX INDICATEURS AVANCÉS ===
        
        # EMA 200 pour filtre de tendance long terme
        df['ema_long'] = ta.EMA(df['close'].values, timeperiod=self.ema_long)
        
        # MACD pour confirmation de tendance
        macd, macd_signal, macd_hist = ta.MACD(df['close'].values, 
                                              fastperiod=self.macd_fast,
                                              slowperiod=self.macd_slow, 
                                              signalperiod=self.macd_signal)
        df['macd'] = macd
        df['macd_signal'] = macd_signal
        df['macd_histogram'] = macd_hist
        
        # ATR pour volatilité et stops dynamiques
        df['atr'] = ta.ATR(df['high'].values, df['low'].values, df['close'].values, 
                          timeperiod=self.atr_length)
        
        # Bollinger Bands pour sur-achat/survente
        bb_upper, bb_middle, bb_lower = ta.BBANDS(df['close'].values, 
                                                 timeperiod=self.bb_length,
                                                 nbdevup=self.bb_std, 
                                                 nbdevdn=self.bb_std)
        df['bb_upper'] = bb_upper
        df['bb_middle'] = bb_middle
        df['bb_lower'] = bb_lower
        df['bb_width'] = (bb_upper - bb_lower) / bb_middle * 100
        
        # ADX pour force de tendance
        df['adx'] = ta.ADX(df['high'].values, df['low'].values, df['close'].values,
                          timeperiod=self.adx_length)
        df['plus_di'] = ta.PLUS_DI(df['high'].values, df['low'].values, df['close'].values,
                                  timeperiod=self.adx_length)
        df['minus_di'] = ta.MINUS_DI(df['high'].values, df['low'].values, df['close'].values,
                                    timeperiod=self.adx_length)
        
        return df
    
    def detect_advanced_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        """Détecte les signaux avec les nouveaux filtres avancés"""
        # Signaux de base
        df['buy_signal_basic'] = (df['close'] > df['ema_main']) & (df['close'].shift(1) <= df['ema_main'].shift(1))
        df['sell_signal_basic'] = (df['close'] < df['ema_main']) & (df['close'].shift(1) >= df['ema_main'].shift(1))
        
        # === FILTRES AVANCÉS ===
        
        # Filtre tendance long terme (EMA 200)
        df['long_trend_bullish'] = df['close'] > df['ema_long']
        
        # Filtre MACD (confirmation de tendance)
        df['macd_bullish'] = (df['macd'] > df['macd_signal']) & (df['macd_histogram'] > 0)
        
        # Filtre ADX (force de tendance)
        df['strong_trend'] = df['adx'] > 25
        df['di_bullish'] = df['plus_di'] > df['minus_di']
        
        # Filtre Bollinger Bands
        df['bb_oversold'] = df['close'] < df['bb_lower']
        df['bb_overbought'] = df['close'] > df['bb_upper']
        df['bb_squeeze'] = df['bb_width'] < df['bb_width'].rolling(20).quantile(0.2)
        
        # Signaux filtrés avancés
        df['buy_signal'] = (df['buy_signal_basic'] & 
                           df['long_trend_bullish'] & 
                           df['macd_bullish'] & 
                           df['strong_trend'] & 
                           df['di_bullish'])
        
        df['sell_signal'] = (df['sell_signal_basic'] | 
                            df['bb_overbought'] |
                            (~df['macd_bullish'] & df['strong_trend']))
        
        return df
    
    def calculate_dynamic_stops(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcule les stops dynamiques basés sur l'ATR"""
        # Stop loss dynamique basé sur ATR
        df['dynamic_stop_loss_pct'] = np.maximum(
            self.base_stop_loss_pct,
            (df['atr'] / df['close'] * 100 * self.atr_multiplier)
        )
        
        # Take profit adaptatif
        df['dynamic_take_profit_pct'] = df['dynamic_stop_loss_pct'] * 2
        
        # Trailing stop ATR
        df['atr_trailing_stop'] = df['close'] - (df['atr'] * self.atr_multiplier)
        
        return df
    
    def prepare_ml_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Prépare les features pour le machine learning"""
        # Features techniques
        df['rsi_normalized'] = (df['rsi'] - 50) / 50
        df['macd_normalized'] = df['macd'] / df['close']
        df['bb_position'] = (df['close'] - df['bb_lower']) / (df['bb_upper'] - df['bb_lower'])
        df['volume_ratio'] = df['volume'] / df['volume_avg']
        df['price_vs_ema'] = (df['close'] - df['ema_main']) / df['ema_main']
        df['price_vs_ema_long'] = (df['close'] - df['ema_long']) / df['ema_long']
        df['atr_normalized'] = df['atr'] / df['close']
        
        # Features de momentum
        df['price_change_1'] = df['close'].pct_change(1)
        df['price_change_5'] = df['close'].pct_change(5)
        df['price_change_10'] = df['close'].pct_change(10)
        
        # Features de volatilité
        df['volatility_5'] = df['close'].rolling(5).std() / df['close']
        df['volatility_20'] = df['close'].rolling(20).std() / df['close']
        
        return df
    
    def train_ml_model(self, df: pd.DataFrame) -> None:
        """Entraîne le modèle ML pour prédire les signaux rentables"""
        if len(df) < self.ml_lookback * 2:
            return
        
        # Préparation des features
        feature_columns = [
            'rsi_normalized', 'macd_normalized', 'bb_position', 'volume_ratio',
            'price_vs_ema', 'price_vs_ema_long', 'atr_normalized',
            'price_change_1', 'price_change_5', 'price_change_10',
            'volatility_5', 'volatility_20', 'adx'
        ]
        
        # Création du target (signal rentable dans les N prochaines barres)
        df['future_return'] = df['close'].shift(-5) / df['close'] - 1
        df['profitable_signal'] = (df['future_return'] > 0.02).astype(int)  # 2% de gain minimum
        
        # Filtrage des données complètes
        valid_data = df[feature_columns + ['profitable_signal']].dropna()
        
        if len(valid_data) < 100:
            return
        
        X = valid_data[feature_columns].values
        y = valid_data['profitable_signal'].values
        
        # Normalisation
        X_scaled = self.scaler.fit_transform(X)
        
        # Entraînement avec validation temporelle
        tscv = TimeSeriesSplit(n_splits=3)
        
        # Modèle ensemble
        self.ml_model = GradientBoostingClassifier(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            random_state=42
        )
        
        self.ml_model.fit(X_scaled, y)
        
    def calculate_ml_score(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcule le score ML si le modèle est entraîné"""
        if not self.use_ml_scoring or self.ml_model is None:
            return df
        
        feature_columns = [
            'rsi_normalized', 'macd_normalized', 'bb_position', 'volume_ratio',
            'price_vs_ema', 'price_vs_ema_long', 'atr_normalized',
            'price_change_1', 'price_change_5', 'price_change_10',
            'volatility_5', 'volatility_20', 'adx'
        ]
        
        # Prédiction des probabilités
        valid_data = df[feature_columns].dropna()
        
        if len(valid_data) > 0:
            X_scaled = self.scaler.transform(valid_data.values)
            probabilities = self.ml_model.predict_proba(X_scaled)[:, 1]
            
            # Ajout des scores ML au DataFrame
            df.loc[valid_data.index, 'ml_probability'] = probabilities
            df['ml_score'] = df['ml_probability'] * 100
        else:
            df['ml_score'] = 50  # Score neutre par défaut
        
        return df
    
    def calculate_enhanced_ai_score(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcule le score IA amélioré avec tous les nouveaux indicateurs"""
        df['ai_score'] = 0
        
        # Critères de base (15 points chacun)
        df.loc[df['buy_signal_basic'], 'ai_score'] += 15
        df.loc[df['rsi'] > 50, 'ai_score'] += 15
        df.loc[df['volume'] > df['volume_avg'] * self.volume_ratio_threshold, 'ai_score'] += 15
        
        # Nouveaux critères avancés (10 points chacun)
        df.loc[df['long_trend_bullish'], 'ai_score'] += 10
        df.loc[df['macd_bullish'], 'ai_score'] += 10
        df.loc[df['strong_trend'] & df['di_bullish'], 'ai_score'] += 10
        df.loc[df['bb_oversold'], 'ai_score'] += 10
        df.loc[df['bb_squeeze'], 'ai_score'] += 5  # Compression = potentiel breakout
        
        # Intégration du score ML (15 points max)
        if 'ml_score' in df.columns:
            df['ai_score'] += (df['ml_score'] / 100 * 15)
        
        # Signal renforcé avec seuil adaptatif
        df['enhanced_buy_signal'] = (df['ai_score'] >= self.min_score_threshold) & df['buy_signal']
        
        return df
    
    def compute(self, df: pd.DataFrame) -> pd.DataFrame:
        """Pipeline complet de calcul avec tous les indicateurs avancés"""
        result_df = df.copy()
        
        # Pipeline modulaire
        result_df = self.calculate_base_indicators(result_df)
        result_df = self.detect_advanced_signals(result_df)
        result_df = self.calculate_dynamic_stops(result_df)
        result_df = self.prepare_ml_features(result_df)
        
        # Entraînement ML si activé
        if self.use_ml_scoring:
            self.train_ml_model(result_df)
            result_df = self.calculate_ml_score(result_df)
        
        result_df = self.calculate_enhanced_ai_score(result_df)
        
        return result_df
