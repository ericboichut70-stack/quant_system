# 📤 Export .json des attestations
import json

def export_attestations_json(output_path="exports/bot_roadmap_attestations.json"):
    attestations = {
        "1.0.0": {
            "mentors": [
                {
                    "nom": "Dr. Lemoine",
                    "rôle": "Validateur principal",
                    "score": 95,
                    "commentaire": "Livraison conforme, structure claire, modules verrouillés avec rigueur.",
                    "date": "2025-11-01"
                },
                {
                    "nom": "A. Dupont",
                    "rôle": "Relecteur secondaire",
                    "score": 88,
                    "commentaire": "Très bon niveau, interface mentor bien pensée.",
                    "date": "2025-11-01"
                }
            ],
            "communautaire": {
                "statut": "prévue",
                "remarques": "Scoring multi-utilisateur en cours de structuration"
            }
        }
    }

    with open(output_path, "w") as f:
        json.dump(attestations, f, indent=2)

    print("✅ bot_roadmap_attestations.json généré.")

if __name__ == "__main__":
    export_attestations_json()
