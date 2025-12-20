# ✅ Interface de lancement scénarisé
# 🎯 Objectif : Permettre au bot ou au mentor de :
# Lancer un scénario pédagogique avec narration, Définir les objectifs, durée, récompenses,
# Activer une interface immersive pour les élèves
def launch_scenario(name, description, goal, duration_days, reward, path="utils/scenario_launch_log.txt"):
    """
    Lance un scénario pédagogique scénarisé.
    """
    from datetime import datetime, timedelta
    deadline = datetime.now() + timedelta(days=duration_days)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {name} | {description} | Objectif : {goal} | Récompense : {reward} | Deadline : {deadline.date()}\n")

    return {
        "Nom": name,
        "Description": description,
        "Objectif": goal,
        "Récompense": reward,
        "Deadline": deadline.date()
    }
