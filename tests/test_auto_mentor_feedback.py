# RESOLUTION ERREUR EXECUTION POWERSHELL:
# Ce premier bloc ajoute le dossier racine TRADING_BOT/ au PYTHONPATH,
# ce qui permet à Python de trouver modules/.
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 🧪 Test auto_mentor_feedback avec tableau simulé
from modules.auto_mentor_feedback import auto_mentor_feedback

# Tableau simulé
rows = [
    {"ScenarioType": "breaker", "ConfidenceScore": 85},
    {"ScenarioType": "sweep", "ConfidenceScore": 72},
    {"ScenarioType": "mitigation", "ConfidenceScore": 58}
]

print("🧠 Test auto_mentor_feedback")
for row in rows:
    decision, comment = auto_mentor_feedback(row)
    print(f"{row['ScenarioType']} | Score: {row['ConfidenceScore']} → {decision} | {comment}")
