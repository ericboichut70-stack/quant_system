# ✅ Verrouillage des tailles de compte
def get_account_size_options():
    """
    Renvoie une liste sécurisée de tailles de compte disponibles.
    """
    return ["5K", "10K", "25K", "50K", "100K", "200K"]

def validate_account_size(selected_size, user_profile):
    """
    Vérifie que la taille sélectionnée est cohérente avec le profil utilisateur.
    """
    allowed_sizes = user_profile.get("allowed_sizes", [])
    return selected_size in allowed_sizes
