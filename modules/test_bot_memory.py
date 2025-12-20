import pandas as pd
from bot_memory import update_bot_memory, get_memory_summary, save_feedback

# --- Création d'un DataFrame de signaux validés ---
df_validated = pd.DataFrame([
    {"timestamp": "2025-12-16 10:00:00", "SignalSuccess": 1, "RiskReward": 2.0},
    {"timestamp": "2025-12-16 11:00:00", "SignalSuccess": 0, "RiskReward": 1.5},
    {"timestamp": "2025-12-16 12:00:00", "SignalSuccess": 0, "RiskReward": 0.8},
])

# --- Mise à jour de la mémoire ---
nb_errors = update_bot_memory(df_validated)
print(f"Nombre d'erreurs mémorisées : {nb_errors}")

# --- Résumé de la mémoire ---
summary = get_memory_summary()
print(summary)

# --- Sauvegarde d'un feedback ---
save_feedback("signal_123", "Erreur détectée sur la logique intraday.")
print("Feedback sauvegardé dans utils/feedback_log.txt")
