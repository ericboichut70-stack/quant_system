# 📜 “Générer index des certificats”
import yaml

def generate_certificates_index(output_path="config/bot_registry_certificates.yaml"):
    certificates = {
        "1.0.0": {
            "certificat": "bot_certificate.md",
            "validé_par": "Dr. Lemoine",
            "score": 95,
            "date": "2025-11-01",
            "artefacts": [
                "bot_roadmap_contract.md",
                "bot_roadmap_attestations.md",
                "bot_registry_manifest.yaml"
            ]
        },
        "1.1.0": {
            "certificat": "prévu",
            "validé_par": "simulateur mentor",
            "score": None,
            "date": "2025-12-01",
            "artefacts": [
                "bot_roadmap_forecast.yaml",
                "bot_roadmap_commitments.yaml"
            ]
        }
    }

    with open(output_path, "w") as f:
        yaml.dump(certificates, f)

    print("✅ bot_registry_certificates.yaml généré.")
