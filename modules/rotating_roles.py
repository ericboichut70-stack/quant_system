# ✅ Interface de rôle tournant
# 🎯 Objectif : Attribuer à des membres des rôles temporaires tournants :
# Animateur de saison, Validateur communautaire, Parrain de binôme, Archiviste pédagogique
def assign_rotating_role(user_name, role_name, start_date, end_date, path="utils/rotating_roles_log.txt"):
    """
    Attribue un rôle tournant à un membre.
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{start_date} → {end_date} | {user_name} | Rôle : {role_name}\n")

    return {
        "Utilisateur": user_name,
        "Rôle": role_name,
        "Période": f"{start_date} → {end_date}"
    }
