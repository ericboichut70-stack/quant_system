import pandas as pd

def route_signals_to_accounts(df_signals: pd.DataFrame, accounts_df: pd.DataFrame) -> pd.DataFrame:
    """
    Associe chaque signal à un compte propfirm selon sa nature.
    Ajoute une colonne 'AssignedAccount' au DataFrame des signaux.
    """

    df = df_signals.copy()
    df["AssignedAccount"] = "Unassigned"

    for i, row in df.iterrows():
        ts = pd.to_datetime(row["timestamp"], errors="coerce")
        hour = ts.hour if pd.notna(ts) else None
        overnight = hour is not None and (hour >= 22 or hour < 6)
        duration = row.get("Duration", 0)

        # Filtrage des comptes compatibles
        candidates = accounts_df.copy()
        candidates = candidates[candidates["news_allowed"]]

        if overnight:
            candidates = candidates[candidates["overnight_allowed"]]
        else:
            # Ici, on n’exclut pas les comptes overnight pour les signaux daytime
            pass

        # Option : filtrer par stratégie si disponible
        if "type" in candidates.columns:
            if duration > 60:
                candidates = candidates[candidates["type"].str.lower() == "swing"]
            else:
                candidates = candidates[candidates["type"].str.lower() == "intraday"]

        # Choix du compte avec le plus grand drawdown
        if not candidates.empty:
            selected = candidates.sort_values("max_drawdown", ascending=False).iloc[0]
            df.at[i, "AssignedAccount"] = selected["name"]

    return df
