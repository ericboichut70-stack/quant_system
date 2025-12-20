# 🧪 Test community_scoring avec plusieurs utilisateurs
from modules.community_scoring import aggregate_scores, assign_role

# 🧠 Le script est peut-être lancé sans inclure le chemin racine dans PYTHONPATH;
# Force l’ajout du chemin racine:
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.auto_mentor_feedback import auto_mentor_feedback

users = {
    "Alice": [85, 90, 88],
    "Bob": [72, 75, 78],
    "Charlie": [60, 62, 65],
    "Dana": [45, 50, 55]
}

print("👥 Test community_scoring")
for name, scores in users.items():
    avg = aggregate_scores(scores)
    role = assign_role(avg)
    print(f"{name} | Moyenne: {avg} → Rôle: {role}")
