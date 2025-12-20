# ✅ Logique de validation pré-trade
# 🎯 Objectif : filtre de sécurité pédagogique, avant toute exécution ou simulation.
def validate_pre_trade(signal_row, memory_dict, account_size, user_profile, pause_status):
    """
    Valide qu’un signal peut être activé selon les garde-fous pédagogiques.
    """
    scenario = signal_row["ScenarioType"]
    score = signal_row["ConfidenceScore"]
    mem_score = memory_dict.get(scenario, 0)

    if pause_status:
        return False, "⏸️ Pause pédagogique active."

    if score < 3:
        return False, f"⚠️ Score trop faible ({score}) pour '{scenario}'"

    if mem_score < 0:
        return False, f"🔻 Scénario '{scenario}' désactivé."

    if account_size not in user_profile.get("allowed_sizes", []):
        return False, "❌ Taille de compte non autorisée."

    return True, "✅ Signal validé pour activation."
