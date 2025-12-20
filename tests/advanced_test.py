# Utilisation basique
from advanced_trading_indicator import AdvancedTradingIndicator, generate_sample_data

# Chargement des données
data = generate_sample_data('C:\Users\user\OneDrive\Documents\CODES IA\CODES CASCADE\1.0 BOT INDICATOR IA TV PYTHON\200 DATA CLONE B ENERGIE.csv')

# Indicateur avec ML activé
indicator = AdvancedTradingIndicator(use_ml_scoring=True)
enriched_data = indicator.compute(data)


# Visualisation avancée (12 graphiques)
indicator.plot_advanced_analysis(enriched_data)

# Démonstration complète
main_demo(data = pd.read_csv('C:/Users/user/OneDrive/Documents/CODES IA/CODES CASCADE/1.0 BOT INDICATOR IA TV PYTHON/mes_donnees.csv'))