# modules/scenario_builder.py

import pandas as pd

def build_scenarios(df: pd.DataFrame) -> pd.DataFrame:
    """
    Construit des scénarios de trading à partir des signaux.
    
    Paramètres :
    - df : DataFrame contenant ['timestamp','Trend','Signal','RiskReward']
    
    Retour :
    - DataFrame enrichi avec colonne 'Scenario' :
      * 'LongSetup' si Trend=Bullish et Signal=Buy
      * 'ShortSetup' si Trend=Bearish et Signal=Sell
      * 'Neutral' sinon
    """
    df = df.copy()
    df["Scenario"] = "Neutral"

    for i, row in df.iterrows():
        if row["Trend"] == "Bullish" and row["Signal"] == "Buy":
            df.at[i, "Scenario"] = "LongSetup"
        elif row["Trend"] == "Bearish" and row["Signal"] == "Sell":
            df.at[i, "Scenario"] = "ShortSetup"

    return df


def summarize_scenarios(df: pd.DataFrame) -> str:
    """
    Génère un résumé des scénarios construits.
    
    Paramètres :
    - df : DataFrame enrichi par build_scenarios
    
    Retour :
    - Chaîne descriptive avec nombre de setups longs et courts
    """
    if df.empty:
        return "📊 Aucun scénario construit."

    long_count = (df["Scenario"] == "LongSetup").sum()
    short_count = (df["Scenario"] == "ShortSetup").sum()

    return f"📊 Scénarios : Long={long_count}, Short={short_count}"
