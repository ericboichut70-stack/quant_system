# ✅ Logique de rôle communautaire temporaire
# 🎯 Objectif : Attribuer des rôles temporaires à des membres selon :
# Leur contribution à une saison ou défi, Leur engagement communautaire, Leur participation à des validations croisées
def assign_temporary_role(user_name, role_name, duration_days, path="utils/temporary_roles_log.txt"):
    """
    Attribue un rôle communautaire temporaire.
    """
    from datetime import datetime, timedelta
    expiry = datetime.now() + timedelta(days=duration_days)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user_name} | Rôle : {role_name} | Expire : {expiry.date()}\n")

    return {
        "Utilisateur": user_name,
        "Rôle": role_name,
        "Expire le": expiry.date()
    }

