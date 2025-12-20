# ✅ Interface de suivi des quêtes
# 🎯 Objectif : Permettre à chaque élève de :
# Visualiser ses quêtes en cours, Suivre l’état d’avancement,
# Marquer une quête comme accomplie, Recevoir une récompense ou un badge
def track_quests(user_name, feedback_df, quest_log_path="utils/quest_log.txt"):
    """
    Génère le suivi des quêtes pour un élève.
    """
    import pandas as pd
    from datetime import datetime

    # Chargement des quêtes enregistrées
    try:
        quests = pd.read_csv(quest_log_path, sep="|", names=["timestamp", "user", "titre", "objectif", "status"])
    except FileNotFoundError:
        quests = pd.DataFrame(columns=["timestamp", "user", "titre", "objectif", "status"])

    user_quests = quests[quests["user"] == user_name]

    # Mise à jour automatique si objectif atteint
    updated = []
    for _, row in user_quests.iterrows():
        if row["status"] == "En cours":
            if "Valider" in row["objectif"]:
                valides = (feedback_df[(feedback_df["user"] == user_name)]["decision"] == "Valider").sum()
                target = int("".join(filter(str.isdigit, row["objectif"])))
                if valides >= target:
                    updated.append(row["titre"])
                    quests.loc[(quests["user"] == user_name) & (quests["titre"] == row["titre"]), "status"] = "✅ Accomplie"

    # Sauvegarde
    if updated:
        quests.to_csv(quest_log_path, sep="|", index=False)

    return quests[quests["user"] == user_name]
