# ✅ Logique de parcours scénarisé
def build_scenario_pathway(feedback_df, user_name, memory_dict, difficulty="Intermédiaire"):
    """
    Génère un parcours scénarisé pour un élève selon son niveau et sa mémoire.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    validated = user_df[user_df["decision"] == "Valider"]["ScenarioType"].value_counts()

    # Définition des scénarios par niveau
    scenario_levels = {
        "Débutant": ["range", "breakout"],
        "Intermédiaire": ["reversal", "news_spike"],
        "Avancé": ["multi-leg", "volatility trap", "liquidity sweep"]
    }

    pathway = []
    for scenario in scenario_levels.get(difficulty, []):
        score = memory_dict.get(scenario, 0)
        count = validated.get(scenario, 0)
        pathway.append({"Scenario": scenario, "Validations": count, "Score mémoire": score})

    return sorted(pathway, key=lambda x: (-x["Validations"], -x["Score mémoire"]))
