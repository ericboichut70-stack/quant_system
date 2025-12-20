# ✅ Interface de rôle communautaire
# 🎯 Objectif : Permettre à chaque élève d’avoir un rôle visible dans la communauté :
# Initié, Explorateur, Stratège, Mentoré; Affiché dans les classements, binômes, tournois;
# Peut être lié à des permissions ou responsabilités
def get_community_roles(feedback_df, user_list):
    """
    Génère les rôles communautaires pour tous les utilisateurs.
    """
    roles = []
    for user in user_list:
        valides = (feedback_df[(feedback_df["user"] == user)]["decision"] == "Valider").sum()
        if valides < 10:
            role = "🧑‍🎓 Initié"
        elif valides < 30:
            role = "🧭 Explorateur"
        elif valides < 60:
            role = "🧠 Stratège"
        else:
            role = "🧑‍🏫 Mentoré"
        roles.append({"Utilisateur": user, "Rôle": role})
    return roles
