# 📤 Export .json de la timeline
import json

def export_timeline_json(output_path="exports/bot_registry_timeline.json"):
    timeline = [
        {
            "version": "1.0.0",
            "date": "2025-11-01",
            "statut": "livrée",
            "artefacts": ["contrat", "certificat", "attestations", "archive"]
        },
        {
            "version": "0.9.0",
            "date": "2025-10-28",
            "statut": "livrée",
            "artefacts": ["release_notes", "changelog", "validations"]
        },
        {
            "version": "0.8.0",
            "date": "2025-10-20",
            "statut": "livrée",
            "artefacts": ["registre_initial", "modules_base"]
        },
        {
            "version": "1.1.0",
            "date": "2025-12-01",
            "statut": "en cours",
            "artefacts": ["forecast", "engagements", "signatures"]
        }
    ]

    with open(output_path, "w") as f:
        json.dump(timeline, f, indent=2)

    print("✅ bot_registry_timeline.json généré.")

if __name__ == "__main__":
    export_timeline_json()
