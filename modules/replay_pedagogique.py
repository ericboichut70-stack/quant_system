# modules/replay_pedagogique.py

import time
import pandas as pd

def replay_with_explanations(df: pd.DataFrame, speed: float = 1.0) -> None:
    """
    Rejoue les trades en mode pédagogique, avec explications étape par étape.
    
    Paramètres :
    - df : DataFrame contenant ['timestamp','Direction','Entry','Exit','Size','PnL','Outcome']
    - speed : vitesse de simulation (en secondes entre chaque trade)
    
    Retour :
    - None (affiche les trades avec explications)
    """
    if df.empty:
        print("🎓 Aucun trade à rejouer en mode pédagogique.")
        return

    print("🎓 Début du replay pédagogique des trades...")
    for _, row in df.iterrows():
        print(f"\n⏱️ {row['timestamp']} → Nouvelle bougie analysée")
        print(f"➡️ Signal : {row['Direction']} {row['Size']} unités")
        print(f"🎯 Entrée à {row['Entry']} → Sortie à {row['Exit']}")
        print(f"💰 Résultat : PnL={row['PnL']} | Issue={row['Outcome']}")
        if row["Outcome"] == "TP":
            print("✅ Explication : le trade a atteint son objectif (Take Profit).")
        elif row["Outcome"] == "SL":
            print("❌ Explication : le trade a touché son Stop Loss.")
        else:
            print("ℹ️ Explication : issue neutre ou non définie.")
        time.sleep(speed)
    print("\n🎓 Replay pédagogique terminé.")


def summarize_pedagogique(df: pd.DataFrame) -> str:
    """
    Génère un résumé du replay pédagogique.
    
    Paramètres :
    - df : DataFrame des trades
    
    Retour :
    - Chaîne descriptive avec nombre de trades et PnL total
    """
    if df.empty:
        return "📊 Replay pédagogique : aucun trade disponible."

    total_trades = len(df)
    pnl_total = df["PnL"].sum()

    return f"📊 Replay pédagogique : {total_trades} trades rejoués, PnL total={pnl_total:.2f}"
