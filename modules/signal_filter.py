## Module autonome d'activation, désactivation, ou ajustage dynamique des signaux
def filter_signals(df, market=None, context=None, min_score=5):
    """
    Filtre les signaux selon le marché, le contexte et le score minimal.
    """
    filtered = df.copy()

    if market:
        filtered = filtered[filtered["Market"] == market]
    if context:
        filtered = filtered[filtered["Context"] == context]
    filtered = filtered[filtered["ConfidenceScore"] >= min_score]

    return filtered
