# ✅ Génération de feedback.py — Enregistrement des retours
# Appel possible depuis n’importe quel test ou interface CLI.
# utils/feedback.py
import yaml
from datetime import datetime

FEEDBACK_PATH = "config/feedback.yaml"

def save_feedback(module, score, comment):
    feedback = {
        "last_feedback": {
            "module": module,
            "score": score,
            "comment": comment,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    }
    with open(FEEDBACK_PATH, "w") as f:
        yaml.dump(feedback, f)
    print("✅ Feedback enregistré dans feedback.yaml")
