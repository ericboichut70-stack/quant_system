# strategy/signal_filter.py
import pandas as pd
from strategy.news_turbulence_filter import load_news_calendar, is_near_news, compute_turbulence_index

def filter_signals(df, news_path, impact_level="high", window_minutes=30, turbulence_threshold=0.02):
    news_df = load_news_calendar(news_path, impact_filter=impact_level)
    df = compute_turbulence_index(df)

    filtered_rows = []
    for i, row in df.iterrows():
        signal_time = row["timestamp"]
        turbulence = row.get("turbulence", 0)

        if is_near_news(signal_time, news_df, window_minutes):
            row["reason"] = "🛑 News à fort impact détectée"
        elif turbulence > turbulence_threshold:
            row["reason"] = "🌪️ Turbulence trop élevée"
        else:
            row["reason"] = ""

        filtered_rows.append(row)

    return pd.DataFrame(filtered_rows)

# 🔧 Désactivation automatique
def auto_deactivate_signals(df, feedback_df, threshold=3):
    """
    Désactive automatiquement les signaux trop critiqués ou invalidés.
    """
    to_deactivate = []

    for signal_id in df["timestamp"]:
        feedbacks = feedback_df[feedback_df["timestamp"] == signal_id]
        if len(feedbacks) >= 3 and feedbacks["decision"].value_counts().get("Rejeter", 0) >= threshold:
            to_deactivate.append(signal_id)

    df["is_active"] = ~df["timestamp"].isin(to_deactivate)
    return df
