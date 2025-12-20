# 📤 Export .json des signatures lisibles
import json

def export_signatures_json(output_path="exports/bot_registry_signatures.json"):
    signatures = {
        "1.0.0": [
            {
                "nom": "Dr. Lemoine",
                "rôle": "Validateur principal",
                "score": 95,
                "commentaire": "Livraison conforme, structure claire, modules verrouillés"
            },
            {
                "nom": "A. Dupont",
                "rôle": "Relecteur secondaire",
                "score": 88,
                "commentaire": "Très bon niveau, interface mentor bien pensée"
            }
        ],
        "1.1.0": [
            {
                "nom": None,
                "rôle": None,
                "score": None,
                "commentaire": "Validation prévue via simulateur mentor"
            }
        ]
    }

    with open(output_path, "w") as f:
        json.dump(signatures, f, indent=2)

    print("✅ bot_registry_signatures.json généré.")

if __name__ == "__main__":
    export_signatures_json()
