# modules/sentiment_analyzer.py

import pandas as pd

def analyze_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyse le sentiment du marché à partir des variations de prix.
    
    Paramètres :
    - df : DataFrame contenant ['timestamp','close']
    
    Retour :
    - DataFrame enrichi avec colonne 'Sentiment' :
      * 'Positive' si variation > 0
      * 'Negative' si variation < 0
      * 'Neutral' si variation = 0
    """
    df = df.copy()
    df["Variation"] = df["close"].diff()
    df["Sentiment"] = df["Variation"].apply(
        lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
    )
    return df


def summarize_sentiment(df: pd.DataFrame) -> str:
    """
    Génère un résumé du sentiment global.
    
    Paramètres :
    - df : DataFrame enrichi par analyze_sentiment
    
    Retour :
    - Chaîne descriptive avec proportion de sentiments positifs, négatifs et neutres
    """
    if df.empty:
        return "📊 Aucun sentiment détecté."

    pos = (df["Sentiment"] == "Positive").mean() * 100
    neg = (df["Sentiment"] == "Negative").mean() * 100
    neu = (df["Sentiment"] == "Neutral").mean() * 100

    summary = "📊 Sentiment global :\n"
    summary += f"- Positif : {pos:.2f}%\n"
    summary += f"- Négatif : {neg:.2f}%\n"
    summary += f"- Neutre : {neu:.2f}%\n"
    return summary
