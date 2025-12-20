# 🧑‍🏫 Interface CLI pour soumettre des validations
import json
from datetime import datetime

def submit_validation():
    print("\n🧑‍🏫 Soumission de validation mentorale")
    scenario = input("🎭 Scénario : ")
    score = int(input("📊 Score : "))
    decision = input("🧠 Décision (Valider / Rejeter / À revoir) : ")
    comment = input("📝 Commentaire : ")

    validation = {
        "scenario": scenario,
        "score": score,
        "decision": decision,
        "comment": comment,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    with open("exports/mentor_validations.json", "a") as f:
        f.write(json.dumps(validation) + "\n")

    print("✅ Validation enregistrée.")

if __name__ == "__main__":
    submit_validation()

# Boucle de validation pour saisie de score imposée.
while True:
    try:
        score = int(input("📊 Score : "))
        break
    except ValueError:
        print("❌ Entrée invalide. Saisis un nombre entier.")
