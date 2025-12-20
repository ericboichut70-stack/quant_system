# 📤 Export .json du registre complet
import yaml
import json

def export_registry_json(registry_path="config/module_registry.yaml", output_path="exports/module_registry.json"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    with open(output_path, "w") as f:
        json.dump(registry, f, indent=2)

    print("✅ module_registry.json généré.")

if __name__ == "__main__":
    export_registry_json()
