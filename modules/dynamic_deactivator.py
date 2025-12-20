# ✅ Module de désactivation dynamique
def evaluate_scenario_deactivation(memory_dict, evolving_score_df, coherence_df, thresholds=None):
    """
    Évalue quels scénarios doivent être désactivés dynamiquement.
    """
    if thresholds is None:
        thresholds = {
            "memory": -3,
            "score": 10,
            "coherence": 40
        }

    to_deactivate = []

    for scenario in memory_dict:
        mem_score = memory_dict.get(scenario, 0)
        evol_score = evolving_score_df.set_index("ScenarioType").get("Score collectif évolutif", {}).get(scenario, 0)
        coherence = coherence_df.get("Cohérence (%)", {}).get(scenario, 100)

        if mem_score < thresholds["memory"] or evol_score < thresholds["score"] or coherence < thresholds["coherence"]:
            to_deactivate.append(scenario)

    return to_deactivate
