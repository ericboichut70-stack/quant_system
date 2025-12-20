# 📤 Export .json du manifeste complet
import yaml
import json

def export_manifest_json(manifest_path="config/bot_registry_manifest.yaml", output_path="exports/bot_registry_manifest.json"):
    with open(manifest_path, "r") as f:
        manifest = yaml.safe_load(f)

    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print("✅ bot_registry_manifest.json généré.")

if __name__ == "__main__":
    export_manifest_json()
