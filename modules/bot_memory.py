# modules/bot_memory.py

import pandas as pd
import os

# Mémoire locale des erreurs de signaux
memory_log = []

def update_bot_memory(df_validated: pd.DataFrame) -> int:
    """
    Met à jour la mémoire du bot avec les signaux invalides.
    
    Paramètres :
    - df_validated : DataFrame contenant au minimum la colonne 'SignalSuccess'
    
    Retour :
    - Nombre d'erreurs mémorisées lors de cet appel
    """
    errors = df_validated[df_validated["SignalSuccess"] == 0]
    memory_log.extend(errors.to_dict("records"))
    return len(errors)

def get_memory_summary() -> str:
    """
    Retourne un résumé pédagogique des erreurs mémorisées.
    
    Retour :
    - Chaîne descriptive avec nombre d'erreurs et ratio moyen RiskReward
    """
    if not memory_log:
        return "🧠 Aucune erreur mémorisée pour l'instant."
    
    total = len(memory_log)
    rr_avg = sum(d.get("RiskReward", 0) for d in memory_log) / total
    return f"🧠 {total} erreurs mémorisées. Ratio moyen : {rr_avg:.2f} : 1"

def save_feedback(signal_id: str, feedback_text: str) -> None:
    """
    Sauvegarde un feedback utilisateur dans un fichier local.
    
    Paramètres :
    - signal_id : identifiant du signal concerné
    - feedback_text : texte du feedback
    """
    os.makedirs("utils", exist_ok=True)  # crée le dossier si nécessaire
    with open("utils/feedback_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{signal_id} | {feedback_text}\n")
