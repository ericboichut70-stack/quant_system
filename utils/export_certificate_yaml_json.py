# 📤 Export .yaml ou .json du certificat
import yaml
import json
from datetime import datetime

def export_certificate_yaml_json(registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    locked = [name for name, data in registry.items() if data["status"] == "verrouillé"]
    avg_score = round(sum([data["score"] for name in locked]) / len(locked), 2) if locked else 0

    certificate = {
        "certificat": {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "modules_certifiés": locked,
            "score_moyen": avg_score,
            "auteur": "Eric",
            "statut": "conforme"
        }
    }

    with open("exports/bot_certificate.yaml", "w") as f:
        yaml.dump(certificate, f)

    with open("exports/bot_certificate.json", "w") as f:
        json.dump(certificate, f, indent=2)

    print("✅ Certificat exporté en YAML et JSON.")

if __name__ == "__main__":
    export_certificate_yaml_json()
