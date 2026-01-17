def get_module_docs() -> dict:
    """
    Retourne une documentation pédagogique structurée par module.
    """
    docs = {
        "Indicateurs": [
            "Partition dynamique des niveaux (1 pivot central + 4 supports/résistances)",
            "Énergie calibrée avec filtre SMA et ATR",
            "Détection de tendance via slope EMA et ADX"
        ],
        "Signaux": [
            "Signal Pivots : extrême + position EMA",
            "Signal Énergie : convergence énergie + tendance",
            "Signal combiné : Pivots + Énergie + ATR"
        ],
        "Journal de trading": [
            "Tags : session, jour, heure, pivot touché, niveaux asiatiques",
            "Critères propfirm : drawdown, constance, Sharpe",
            "Export CSV pour analyse"
        ],
        "Prédiction": [
            "Modèle RandomForest",
            "Features : heure, énergie, durée, session, sentiment, tendance",
            "Score de probabilité de réussite"
        ],
        "Exécution / Backtest": [
            "Paramètres dynamiques : taille, SL, TP",
            "Simulation de TP/SL selon tendance",
            "Journal des trades exécutés"
        ],
        "API de trading": [
            "Envoi simulé d’ordres Buy/Sell",
            "Traçabilité des ordres",
            "Préparation pour connexion à broker réel"
        ]
    }
    return docs
