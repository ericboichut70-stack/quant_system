# outcome = 1 si le signal a été gagnant, 0 sinon
def compute_hourly_predictability(df, signal_column="signal", result_column="outcome"):
    hourly_stats = {}
    for hour in range(24):
        subset = df[df["timestamp"].dt.hour == hour]
        if len(subset) > 0:
            win_rate = subset[result_column].mean()
            hourly_stats[hour] = round(win_rate, 3)
    return hourly_stats

def assign_session(timestamp_utc):
    hour = timestamp_utc.hour
    if 0 <= hour < 7:
        return "Asia"
    elif 7 <= hour < 13:
        return "London"
    elif 13 <= hour < 22:
        return "New York"
    else:
        return "Post-market"

def export_predictability_scores(symbol, scores, mode="hourly"):
    path = f"data/predictability_scores/{symbol}_{mode}_predictability.csv"
    pd.DataFrame(list(scores.items()), columns=[mode, "score"]).to_csv(path, index=False)
