# modules/packaging_module.py

import pandas as pd

def package_signals(df: pd.DataFrame) -> dict:
    """
    Prépare un paquetage des signaux pour transmission ou affichage.
    
    Paramètres :
    - df : DataFrame contenant au minimum ['timestamp','Direction','Entry','Exit','Size','PnL','Outcome']
    
    Retour :
    - Dictionnaire structuré avec :
      * 'summary' : résumé global
      * 'signals' : liste des signaux formatés
    """
    if df.empty:
        return {"summary": "📦 Aucun signal disponible.", "signals": []}

    total = len(df)
    tp_count = (df["Outcome"] == "TP").sum()
    sl_count = (df["Outcome"] == "SL").sum()
    pnl_total = df["PnL"].sum()

    summary = f"📦 Paquetage : {total} signaux, TP={tp_count}, SL={sl_count}, PnL total={pnl_total:.2f}"

    signals = []
    for _, row in df.iterrows():
        signals.append({
            "timestamp": row["timestamp"],
            "direction": row["Direction"],
            "entry": row["Entry"],
            "exit": row["Exit"],
            "size": row["Size"],
            "pnl": row["PnL"],
            "outcome": row["Outcome"]
        })

    return {"summary": summary, "signals": signals}


def export_to_dataframe(package: dict) -> pd.DataFrame:
    """
    Convertit un paquetage de signaux en DataFrame.
    
    Paramètres :
    - package : dictionnaire produit par package_signals
    
    Retour :
    - DataFrame des signaux
    """
    return pd.DataFrame(package.get("signals", []))
