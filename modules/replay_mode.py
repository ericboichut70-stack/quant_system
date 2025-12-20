# modules/replay_mode.py

import time
import pandas as pd

def replay_trades(df: pd.DataFrame, speed: float = 1.0) -> None:
    """
    Rejoue les trades en mode simulation temporelle.
    
    Paramètres :
    - df : DataFrame contenant ['timestamp','Direction','Entry','Exit','Size','PnL','Outcome']
    - speed : vitesse de simulation (en secondes entre chaque trade)
    
    Retour :
    - None (affiche les trades en séquence)
    """
    if df.empty:
        print("🎬 Aucun trade à rejouer.")
        return

    print("🎬 Début du replay des trades...")
    for _, row in df.iterrows():
        print(f"[{row['timestamp']}] {row['Direction']} {row['Size']} @ {row['Entry']} → {row['Exit']} | "
              f"PnL={row['PnL']} | Outcome={row['Outcome']}")
        time.sleep(speed)
    print("✅ Replay terminé.")


def summarize_replay(df: pd.DataFrame) -> str:
    """
    Génère un résumé du replay.
    
    Paramètres :
    - df : DataFrame des trades
    
    Retour :
    - Chaîne descriptive avec nombre de trades et PnL total
    """
    if df.empty:
        return "📊 Replay : aucun trade disponible."

    total_trades = len(df)
    pnl_total = df["PnL"].sum()

    return f"📊 Replay : {total_trades} trades rejoués, PnL total={pnl_total:.2f}"
