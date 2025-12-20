import pandas as pd
from advanced_trading_indicator import AdvancedTradingIndicator
import matplotlib.pyplot as plt

# Chargement des données
data = pd.read_csv('C:/Users/user/OneDrive/Documents/CODES_IA/CODES_CASCADE/TRADING_INDICATOR_PYTHON_09_2025/VERSION_1/200_DATA_CLONE_B_ENERGIE.csv')

# Indicateur avec ML activé
indicator = AdvancedTradingIndicator(use_ml_scoring=True)
enriched_data = indicator.compute(data)

# Visualisation (pas de plot_advanced_analysis, on utilise un plot basique)
plt.figure(figsize=(12, 6))
plt.plot(enriched_data.index, enriched_data['close'], label='Prix', color='blue')
plt.plot(enriched_data.index, enriched_data['ema_main'], label='EMA 114', color='orange')
plt.plot(enriched_data.index, enriched_data['ema_long'], label='EMA 200', color='purple')
plt.scatter(enriched_data.index[enriched_data['buy_signal']], enriched_data['close'][enriched_data['buy_signal']], color='green', label='Achat', marker='^')
plt.scatter(enriched_data.index[enriched_data['sell_signal']], enriched_data['close'][enriched_data['sell_signal']], color='red', label='Vente', marker='v')
plt.legend()
plt.title('Signaux de Trading Avancés')
plt.show(block=True)

# Export des signaux
enriched_data.to_csv('signaux_final.csv')