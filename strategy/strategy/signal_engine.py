# strategy/signal_engine.py

import pandas as pd

def generate_signals(df: pd.DataFrame, pivots: dict) -> pd.DataFrame:
    """
    Génère des signaux d'achat/vente en fonction des pivots Ballistic et de l'EMA 114.
    
    Args:
        df: DataFrame contenant les colonnes 'close', 'EMA_114', 'timestamp'
        pivots: Dictionnaire des niveaux pivots (S1, R1, etc.)
    
    Returns:
        DataFrame enrichi avec les colonnes 'BuySignal' et 'SellSignal'
    """
    df = df.copy()
    df["BuySignal"] = False
    df["SellSignal"] = False

    for i, row in df.iterrows():
        close_price = row["close"]
        ema_114 = row.get("EMA_114", None)

        if ema_114 is None or pd.isna(ema_114):
            continue

        # Logique simple : entrée sur extrême + position EMA
        if close_price < pivots["S1"] and close_price < ema_114:
            df.at[i, "BuySignal"] = True
        elif close_price > pivots["R1"] and close_price > ema_114:
            df.at[i, "SellSignal"] = True

    return df

def generate_pivot_trades(df: pd.DataFrame, pivots: dict) -> pd.DataFrame:
    """
    Génère des trades pivot-to-pivot en fonction des niveaux Ballistic.
    Entrée sur Sx ou Rx, sortie sur le niveau suivant.
    """
    df = df.copy()
    df["EntryPivot"] = None
    df["ExitPivot"] = None
    df["TradeActive"] = False

    pivot_levels = [k for k in pivots.keys() if k != "P"]
    pivot_levels_sorted = sorted(pivot_levels, key=lambda k: pivots[k])

    for i, row in df.iterrows():
        price = row["close"]

        for idx, level in enumerate(pivot_levels_sorted[:-1]):
            next_level = pivot_levels_sorted[idx + 1]
            if not row["TradeActive"]:
                if abs(price - pivots[level]) < 0.0005:  # seuil de proximité
                    df.at[i, "EntryPivot"] = level
                    df.at[i, "ExitPivot"] = next_level
                    df.at[i, "TradeActive"] = True
            else:
                if abs(price - pivots[next_level]) < 0.0005:
                    df.at[i, "TradeActive"] = False  # sortie atteinte

    return df

def generate_energy_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Génère des signaux d'achat/vente basés sur l'énergie Ballistic et la tendance SMA(38).
    Achat si ENERGY_CALIB > 0 et Close > SMA(38)
    Vente si ENERGY_CALIB < 0 et Close < SMA(38)
    Filtre de volatilité : ATR(14) > médiane
    """
    df = df.copy()
    df["BuyEnergy"] = False
    df["SellEnergy"] = False

    # SMA 38
    df["SMA_38"] = df["CLOSE"].rolling(38).mean()

    # ATR 14
    df["TR"] = df["HIGH"] - df["LOW"]
    df["ATR_14"] = df["TR"].rolling(14).mean()
    atr_median = df["ATR_14"].median()

    for i, row in df.iterrows():
        if pd.isna(row["ENERGY_CALIB"]) or pd.isna(row["SMA_38"]) or pd.isna(row["ATR_14"]):
            continue

        if row["ATR_14"] < atr_median:
            continue  # marché trop calme

        if row["ENERGY_CALIB"] > 0 and row["CLOSE"] > row["SMA_38"]:
            df.at[i, "BuyEnergy"] = True
        elif row["ENERGY_CALIB"] < 0 and row["CLOSE"] < row["SMA_38"]:
            df.at[i, "SellEnergy"] = True

    return df

def generate_combined_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Génère des signaux combinés Pivots + Énergie + ATR.
    Achat si BuySignal ET BuyEnergy ET ATR > médiane
    Vente si SellSignal ET SellEnergy ET ATR > médiane
    """
    df = df.copy()
    df["BuyCombined"] = False
    df["SellCombined"] = False

    if "ATR_14" not in df.columns:
        df["TR"] = df["HIGH"] - df["LOW"]
        df["ATR_14"] = df["TR"].rolling(14).mean()

    atr_median = df["ATR_14"].median()

    for i, row in df.iterrows():
        if pd.isna(row["ATR_14"]) or row["ATR_14"] < atr_median:
            continue

        if row.get("BuySignal") and row.get("BuyEnergy"):
            df.at[i, "BuyCombined"] = True
        elif row.get("SellSignal") and row.get("SellEnergy"):
            df.at[i, "SellCombined"] = True

    return df

def generate_combined_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Génère des signaux combinés Pivots + Énergie + ATR avec logique d'entrée/sortie.
    """
    df = df.copy()
    df["BuyCombined"] = False
    df["SellCombined"] = False
    df["TradeActive"] = False
    df["TradeType"] = None
    df["EntryTime"] = None
    df["ExitTime"] = None
    df["EntryEnergy"] = None
    df["ExitReason"] = None

    if "ATR_14" not in df.columns:
        df["TR"] = df["HIGH"] - df["LOW"]
        df["ATR_14"] = df["TR"].rolling(14).mean()

    atr_median = df["ATR_14"].median()
    active_trade = None

    for i, row in df.iterrows():
        ts = row["timestamp"] if "timestamp" in row else row.name

        if pd.isna(row["ATR_14"]) or row["ATR_14"] < atr_median:
            continue

        buy_cond = row.get("BuySignal") and row.get("BuyEnergy")
        sell_cond = row.get("SellSignal") and row.get("SellEnergy")

        if not row["TradeActive"]:
            if buy_cond:
                df.at[i, "BuyCombined"] = True
                df.at[i, "TradeActive"] = True
                df.at[i, "TradeType"] = "Buy"
                df.at[i, "EntryTime"] = ts
                df.at[i, "EntryEnergy"] = row["ENERGY_CALIB"]
                active_trade = "Buy"
            elif sell_cond:
                df.at[i, "SellCombined"] = True
                df.at[i, "TradeActive"] = True
                df.at[i, "TradeType"] = "Sell"
                df.at[i, "EntryTime"] = ts
                df.at[i, "EntryEnergy"] = row["ENERGY_CALIB"]
                active_trade = "Sell"
        else:
            # Sortie si signal inverse ou perte de convergence
            if active_trade == "Buy" and (sell_cond or not buy_cond):
                df.at[i, "TradeActive"] = False
                df.at[i, "ExitTime"] = ts
                df.at[i, "ExitReason"] = "Signal inverse ou perte convergence"
                active_trade = None
            elif active_trade == "Sell" and (buy_cond or not sell_cond):
                df.at[i, "TradeActive"] = False
                df.at[i, "ExitTime"] = ts
                df.at[i, "ExitReason"] = "Signal inverse ou perte convergence"
                active_trade = None

    return df

def summarize_trades(df: pd.DataFrame) -> pd.DataFrame:
    """
    Résume les trades convergents : ratio de réussite, durée, énergie, etc.
    """
    trades = df[df["EntryTime"].notna() & df["ExitTime"].notna()].copy()
    trades["EntryTime"] = pd.to_datetime(trades["EntryTime"])
    trades["ExitTime"] = pd.to_datetime(trades["ExitTime"])
    trades["Duration"] = (trades["ExitTime"] - trades["EntryTime"]).dt.total_seconds() / 60  # en minutes
    trades["Direction"] = trades["TradeType"]
    trades["EntryPrice"] = trades["close"]
    trades["ExitPrice"] = df.loc[trades["ExitTime"], "close"].values if "close" in df.columns else np.nan
    trades["PnL"] = np.where(
        trades["Direction"] == "Buy",
        trades["ExitPrice"] - trades["EntryPrice"],
        trades["EntryPrice"] - trades["ExitPrice"]
    )
    trades["Win"] = trades["PnL"] > 0

    summary = {
        "Nb Trades": len(trades),
        "Ratio Réussite": trades["Win"].mean(),
        "Durée moyenne (min)": trades["Duration"].mean(),
        "Gain moyen": trades["PnL"].mean(),
        "Énergie moyenne à l’entrée": trades["EntryEnergy"].mean()
    }

    return trades, summary

def tag_session(hour: int) -> str:
    if 0 <= hour < 7:
        return "Asie"
    elif 7 <= hour < 13:
        return "Londres"
    elif 13 <= hour < 22:
        return "New York"
    else:
        return "Off"

def summarize_trades(df: pd.DataFrame, pivots: dict = None, asian_high: float = None, asian_low: float = None) -> pd.DataFrame:
    trades = df[df["EntryTime"].notna() & df["ExitTime"].notna()].copy()
    trades["EntryTime"] = pd.to_datetime(trades["EntryTime"])
    trades["ExitTime"] = pd.to_datetime(trades["ExitTime"])
    trades["Duration"] = (trades["ExitTime"] - trades["EntryTime"]).dt.total_seconds() / 60
    trades["Direction"] = trades["TradeType"]
    trades["EntryPrice"] = trades["close"]
    trades["Hour"] = trades["EntryTime"].dt.hour
    trades["Session"] = trades["Hour"].apply(tag_session)
    trades["Weekday"] = trades["EntryTime"].dt.day_name()

    # Pivot touché
    if pivots:
        for label, level in pivots.items():
            trades[label] = abs(trades["EntryPrice"] - level) < 0.0005

    # Session asiatique
    if asian_high is not None and asian_low is not None:
        trades["AsianHighTouch"] = abs(trades["EntryPrice"] - asian_high) < 0.0005
        trades["AsianLowTouch"] = abs(trades["EntryPrice"] - asian_low) < 0.0005

    # PnL
    trades["ExitPrice"] = df.loc[trades["ExitTime"], "close"].values if "close" in df.columns else np.nan
    trades["PnL"] = np.where(
        trades["Direction"] == "Buy",
        trades["ExitPrice"] - trades["EntryPrice"],
        trades["EntryPrice"] - trades["ExitPrice"]
    )
    trades["Win"] = trades["PnL"] > 0

    # Résumé
    summary = {
        "Nb Trades": len(trades),
        "Ratio Réussite": trades["Win"].mean(),
        "Durée moyenne (min)": trades["Duration"].mean(),
        "Gain moyen": trades["PnL"].mean(),
        "Max Drawdown": trades["PnL"].min(),
        "Constance (écart-type)": trades["PnL"].std(),
        "Sharpe simplifié": trades["PnL"].mean() / (trades["PnL"].std() + 1e-6),
    }

    return trades, summary

# === Croisement avec les signaux convergents ===
def tag_sentiment(df_signals: pd.DataFrame, df_news: pd.DataFrame, window_minutes: int = 30) -> pd.DataFrame:
    """
    Tague chaque signal convergent avec le sentiment des news proches (±window_minutes).
    """
    df = df_signals.copy()
    df["SentimentTag"] = "neutral"

    news = df_news.copy()
    news["timestamp"] = pd.to_datetime(news["timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    for i, row in df.iterrows():
        ts = row["timestamp"]
        nearby = news[
            (news["timestamp"] >= ts - pd.Timedelta(minutes=window_minutes)) &
            (news["timestamp"] <= ts + pd.Timedelta(minutes=window_minutes))
        ]
        if not nearby.empty:
            sentiments = nearby["sentiment"].value_counts()
            if "negative" in sentiments:
                df.at[i, "SentimentTag"] = "negative"
            elif "positive" in sentiments:
                df.at[i, "SentimentTag"] = "positive"

    return df

def filter_signals_by_sentiment(df_signals: pd.DataFrame, df_news: pd.DataFrame, window_minutes: int = 30) -> pd.DataFrame:
    """
    Filtre les signaux convergents selon le ton des news proches.
    - Ignore les signaux longs si news négatives
    - Ignore les signaux shorts si news positives
    """
    df = df_signals.copy()
    df["SentimentFiltered"] = True  # True = signal conservé

    news = df_news.copy()
    news["timestamp"] = pd.to_datetime(news["timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    for i, row in df.iterrows():
        ts = row["timestamp"]
        nearby = news[
            (news["timestamp"] >= ts - pd.Timedelta(minutes=window_minutes)) &
            (news["timestamp"] <= ts + pd.Timedelta(minutes=window_minutes))
        ]
        if not nearby.empty:
            sentiments = nearby["sentiment"].value_counts()
            if row.get("BuyCombined") and "negative" in sentiments:
                df.at[i, "SentimentFiltered"] = False
            elif row.get("SellCombined") and "positive" in sentiments:
                df.at[i, "SentimentFiltered"] = False

    return df

# === Renommage des niveaux de pivots ===
def rename_pivot_levels(pivots: dict) -> dict:
    pivot_map = {
        "S1": "Do",
        "S2": "Ré",
        "S3": "Mi",
        "S4": "Fa",
        "P": "Sol",
        "R1": "La",
        "R2": "Si",
        "R3": "Do#",
        "R4": "Ré#"
    }
    return {pivot_map.get(k, k): v for k, v in pivots.items()}
