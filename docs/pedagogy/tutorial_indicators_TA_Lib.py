import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import pandas as pd
import numpy as np
from indicators.base_indicators import IndicatorModule


# Simuler des données OHLCV
def generate_sample_data(n=100):
    np.random.seed(42)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n, freq='15min')
    close = np.cumsum(np.random.randn(n)) + 100
    open = close + np.random.randn(n)
    high = np.maximum(open, close) + np.random.rand(n)
    low = np.minimum(open, close) - np.random.rand(n)
    volume = np.random.randint(100, 1000, size=n)

    df = pd.DataFrame({
        'datetime': dates,
        'open': open,
        'high': high,
        'low': low,
        'close': close,
        'volume': volume
    })
    df.set_index('datetime', inplace=True)
    return df

# Initialiser le module
indicator = IndicatorModule(ema_period=20, rsi_period=14, volume_ratio_thresh=1.5)

# Générer les données et calculer les indicateurs
df = generate_sample_data()
df_indicators = indicator.compute_indicators(df)

# Afficher les premières lignes
print(df_indicators[['close', 'EMA', 'RSI', 'HighVolume']].head(10))
