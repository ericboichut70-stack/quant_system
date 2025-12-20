# ✅ Interface de réinitialisation saisonnière
# 🎯 Objectif : Permettre à un élève ou à un mentor de :
# Réinitialiser la saison pédagogique en cours, Repartir à zéro ou conserver les acquis,
# Choisir une nouvelle saison ou laisser le bot réassigner
def reset_season(user_name, feedback_df, memory_dict, mode="soft", path="utils/season_log.txt"):
    """
    Réinitialise la saison pédagogique d’un élève.
    - mode = "soft" : conserve les validations, réinitialise la narration
    - mode = "hard" : purge les validations, recommence depuis la saison 1
    """
    from datetime import datetime
    import pandas as pd
    from modules.pedagogical_quests import get_available_quests
    from modules.narrative_progression import generate_narrative
    from modules.seasonal_roles import assign_seasonal_role
    from modules.seasonal_progression import assign_season

    current_season = assign_season(feedback_df, user_name)
    new_season = "🌱 Saison 1 — Initiation" if mode == "hard" else current_season

    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user_name} | RESET ({mode}) → {new_season}\n")

    # Relance narrative
    narrative = generate_narrative(feedback_df, [], user_name)

    # Quêtes proposées
    new_quests = get_available_quests(user_name, feedback_df, memory_dict)

    # Rôle et permissions
    role, unlocked = assign_seasonal_role(feedback_df, user_name)

    return {
        "season": new_season,
        "narrative": narrative,
        "quests": new_quests,
        "role": role,
        "unlocked_scenarios": unlocked
    }


