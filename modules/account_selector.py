import pandas as pd

def select_best_account(
    accounts_df: pd.DataFrame,
    strategy: str = "intraday",
    allow_overnight: bool = True,
    require_constance: bool = False
) -> pd.DataFrame:
    """
    Sélectionne le compte propfirm le plus adapté à la stratégie.
    
    Paramètres :
    - accounts_df : DataFrame contenant au minimum les colonnes
      ['name', 'max_drawdown', 'overnight_allowed', 'news_allowed', 'constance_required', 'type']
    - strategy : "intraday", "swing" ou "overnight"
    - allow_overnight : True si la stratégie autorise l’overnight, False sinon
    - require_constance : True si la stratégie exige constance, False sinon
    
    Retour :
    - DataFrame avec le compte le plus adapté (1 ligne)
    """

    df = accounts_df.copy()

    # Filtrage par type de stratégie si disponible
    if "type" in df.columns and strategy in ["intraday", "swing"]:
        df = df[df["type"].str.lower() == strategy.lower()]

    # Filtrage overnight
    if strategy == "overnight":
        df = df[df["overnight_allowed"] == True]
    elif strategy == "intraday" and not allow_overnight:
        df = df[df["overnight_allowed"] == False]

    # Filtrage news
    df = df[df["news_allowed"] == True]

    # Filtrage constance
    if require_constance:
        df = df[df["constance_required"] == True]

    # Choix du compte avec le plus grand drawdown
    df = df.sort_values("max_drawdown", ascending=False)

    return df.head(1)
