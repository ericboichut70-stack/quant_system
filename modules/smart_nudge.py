# 🧠 Module de relance intelligente
def generate_nudge(feedback_df, user_name, memory_dict):
    """
    Génère une relance intelligente selon l’activité pédagogique.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    recent = user_df[user_df["timestamp"] >= pd.Timestamp.now() - pd.Timedelta("7D")]

    if len(recent) == 0:
        return "👋 Tu n’as rien soumis cette semaine. Une pause ? Ou envie de reprendre doucement ?"

    weak_scenarios = [s for s in memory_dict if memory_dict[s] < 0]
    if weak_scenarios:
        return f"🔍 Tu pourrais revoir les scénarios suivants : {', '.join(weak_scenarios[:3])}"

    return "✅ Tu progresses bien. Pourquoi ne pas tester un scénario plus avancé cette semaine ?"
