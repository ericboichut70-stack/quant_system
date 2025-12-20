# modules/signal_attribution.py

import pandas as pd

def attribute_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Attribue une origine aux signaux de trading.
    
    Paramètres :
    - df : DataFrame contenant ['timestamp','Signal','Trend','Volume','Sentiment']
    
    Retour :
    - DataFrame enrichi avec colonne 'Attribution' :
      * 'Trend' si le signal est aligné avec la tendance
      * 'Volume' si le volume est élevé
      * 'Sentiment' si le sentiment est positif/négatif fort
      * 'Mixed' si plusieurs conditions sont réunies
      * 'Unclear' sinon
    """
    df = df.copy()
    df["Attribution"] = "Unclear"

    for i, row in df.iterrows():
        reasons = []
        if row.get("Trend") == row.get("Signal"):
            reasons.append("Trend")
        if row.get("Volume", 0) > 1000:
            reasons.append("Volume")
        if row.get("Sentiment") in ["Positive","Negative"]:
            reasons.append("Sentiment")

        if len(reasons) == 1:
            df.at[i, "Attribution"] = reasons[0]
        elif len(reasons) > 1:
            df.at[i, "Attribution"] = "Mixed"

    return df


def summarize_attribution(df: pd.DataFrame) -> str:
    """
    Génère un résumé des attributions de signaux.
    
    Paramètres :
    - df : DataFrame enrichi par attribute_signals
    
    Retour :
    - Chaîne descriptive avec nombre de signaux attribués par type
    """
    if df.empty:
        return "📊 Aucun signal attribué."

    trend_count = (df["Attribution"] == "Trend").sum()
    volume_count = (df["Attribution"] == "Volume").sum()
    sentiment_count = (df["Attribution"] == "Sentiment").sum()
    mixed_count = (df["Attribution"] == "Mixed").sum()
    unclear_count = (df["Attribution"] == "Unclear").sum()

    return (f"📊 Attribution des signaux : Trend={trend_count}, Volume={volume_count}, "
            f"Sentiment={sentiment_count}, Mixed={mixed_count}, Unclear={unclear_count}")
