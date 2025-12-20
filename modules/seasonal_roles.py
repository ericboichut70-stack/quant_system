#🧑‍🏫 Logique de rôle mentoré par saison
# 🎯 Objectif : Attribuer à chaque élève un rôle pédagogique évolutif selon sa saison :
# Initié, Explorateur, Stratège, Mentoré; Chaque rôle débloque des scénarios, badges, ou responsabilités,
# Peut être affiché dans les dashboards ou classements
def assign_seasonal_role(feedback_df, user_name):
    """
    Attribue un rôle pédagogique selon la saison de l’élève.
    """
    valides = (feedback_df[(feedback_df["user"] == user_name)]["decision"] == "Valider").sum()

    if valides < 10:
        return "🧑‍🎓 Initié"
    elif valides < 30:
        return "🧭 Explorateur"
    elif valides < 60:
        return "🧠 Stratège"
    else:
        return "🧑‍🏫 Mentoré"
    if valides >= 60:
        unlocked = ["volatility trap", "liquidity sweep", "mentor_validation"]
        return "🧑‍🏫 Mentoré", unlocked
    else:
        return role, []
