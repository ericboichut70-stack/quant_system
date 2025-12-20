# 🧑‍🏫 Structure du bloc mentor_validation.py
# Appel possible depuis l’interface CLI ou Streamlit.
# modules/mentor_validation.py

def validate_scenario(score, scenario_type):
    if score >= 80:
        return "Valider", f"{scenario_type} bien formé"
    elif score >= 60:
        return "À revoir", f"{scenario_type} à affiner"
    else:
        return "Rejeter", f"{scenario_type} trop faible"
