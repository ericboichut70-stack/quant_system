# 🧑‍🏫 Interface CLI pour relire les validations
import json

def read_validations():
    path = "exports/mentor_validations.json"
    print("\n📖 Relecture des validations mentorales\n")

    try:
        with open(path, "r") as f:
            for line in f:
                v = json.loads(line)
                print(f"{v['timestamp']} | {v['scenario']} | Score: {v['score']} → {v['decision']} | {v['comment']}")
    except FileNotFoundError:
        print("❌ Aucun fichier de validation trouvé.")

if __name__ == "__main__":
    read_validations()

# Filtre pour corriger l'’erreur indiquant que le fichier contient une ligne vide ou mal formée.
for line in f:
    line = line.strip()
    if not line:
        continue  # ignore les lignes vides
    try:
        v = json.loads(line)
        print(f"{v['timestamp']} | {v['scenario']} | Score: {v['score']} → {v['decision']} | {v['comment']}")
    except json.JSONDecodeError:
        print("❌ Ligne invalide ignorée.")
