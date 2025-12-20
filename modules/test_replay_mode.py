import pandas as pd
from replay_mode import replay_trades, summarize_replay

# --- Création d’un DataFrame fictif ---
df_trades = pd.DataFrame([
    {"timestamp":"2025-12-16 10:00:00","Direction":"Buy","Entry":100,"Exit":110,"Size":10,"PnL":100,"Outcome":"TP"},
    {"timestamp":"2025-12-16 11:00:00","Direction":"Sell","Entry":200,"Exit":190,"Size":5,"PnL":50,"Outcome":"TP"},
    {"timestamp":"2025-12-16 12:00:00","Direction":"Buy","Entry":150,"Exit":140,"Size":8,"PnL":-80,"Outcome":"SL"},
])

# --- Replay ---
print(summarize_replay(df_trades))
replay_trades(df_trades, speed=0.5)
