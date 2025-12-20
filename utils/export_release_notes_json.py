# 📤 Export .json des évolutions entre versions
import json

def export_release_notes_json(output_path="exports/bot_release_notes.json"):
    notes = {
        "1.0.0": {
            "date": "2025-11-01",
            "changes": [
                "Activation officielle du bot",
                "Modules verrouillés : memory_evolution, auto_mentor_feedback, trend_detector",
                "Score moyen : 89.0",
                "Interface mentor déployée",
                "Certificat généré"
            ]
        },
        "0.9.0": {
            "date": "2025-10-28",
            "changes": [
                "Tests sur trend_detector et community_scoring",
                "Export CSV et replay activés",
                "Simulation inter-module"
            ]
        },
        "0.8.0": {
            "date": "2025-10-20",
            "changes": [
                "Création du registre",
                "Structuration des modules",
                "Ajout des scripts de test, export, replay"
            ]
        }
    }

    with open(output_path, "w") as f:
        json.dump(notes, f, indent=2)

    print("✅ bot_release_notes.json généré.")

if __name__ == "__main__":
    export_release_notes_json()
