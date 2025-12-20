# modules/structure_tracker.py

import pandas as pd

def detect_market_structure(df: pd.DataFrame) -> pd.DataFrame:
    """
    Détecte une structure de marché simple (HH, HL, LH, LL) à partir des points hauts et bas.

    Paramètres :
    - df : DataFrame contenant au minimum ['timestamp','high','low']

    Retour :
    - DataFrame enrichi avec colonnes :
      * 'SwingHigh' : True/False (détection locale d'un plus haut)
      * 'SwingLow'  : True/False (détection locale d'un plus bas)
      * 'Structure' : 'HH','HL','LH','LL' ou '' (vide si non défini)
    """
    df = df.copy()
    df["SwingHigh"] = False
    df["SwingLow"] = False
    df["Structure"] = ""

    # Détection basique de swings (point extrême local)
    for i in range(1, len(df) - 1):
        prev_high, curr_high, next_high = df.loc[i - 1, "high"], df.loc[i, "high"], df.loc[i + 1, "high"]
        prev_low, curr_low, next_low = df.loc[i - 1, "low"], df.loc[i, "low"], df.loc[i + 1, "low"]

        if curr_high > prev_high and curr_high > next_high:
            df.at[i, "SwingHigh"] = True
        if curr_low < prev_low and curr_low < next_low:
            df.at[i, "SwingLow"] = True

    # Extraction des swings pour comparer la structure
    swings = df[(df["SwingHigh"]) | (df["SwingLow"])].copy()
    last_swing_price = None
    last_swing_type = None  # "H" ou "L"

    for idx in swings.index:
        is_high = df.at[idx, "SwingHigh"]
        price = df.at[idx, "high"] if is_high else df.at[idx, "low"]
        swing_type = "H" if is_high else "L"

        if last_swing_price is not None and last_swing_type == swing_type:
            # Comparaison avec le précédent swing du même type
            if swing_type == "H":
                # Higher High / Lower High
                df.at[idx, "Structure"] = "HH" if price > last_swing_price else "LH"
            else:
                # Higher Low / Lower Low
                df.at[idx, "Structure"] = "HL" if price > last_swing_price else "LL"

        last_swing_price = price
        last_swing_type = swing_type

    return df


def summarize_structure(df: pd.DataFrame) -> str:
    """
    Génère un résumé de la structure de marché détectée.

    Paramètres :
    - df : DataFrame enrichi par detect_market_structure

    Retour :
    - Chaîne descriptive indiquant le nombre de HH, HL, LH, LL
    """
    if df.empty:
        return "📊 Structure : aucun point détecté."

    hh = (df["Structure"] == "HH").sum()
    hl = (df["Structure"] == "HL").sum()
    lh = (df["Structure"] == "LH").sum()
    ll = (df["Structure"] == "LL").sum()

    return f"📊 Structure : HH={hh}, HL={hl}, LH={lh}, LL={ll}"
