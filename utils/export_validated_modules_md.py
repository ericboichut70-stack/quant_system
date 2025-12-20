# 📋 Export .md des modules validés par bot_validator.py
import yaml

def export_validated_modules_md(registry_path="config/module_registry.yaml", output_path="exports/validated_modules.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    lines = ["# ✅ Modules validés — Conformité certifiée\n",
             "| Module | Score |\n",
             "|--------|--------|\n"]

    for name, data in registry.items():
        if data["status"] == "verrouillé" and isinstance(data["score"], (int, float)) and data["score"] >= 80:
            lines.append(f"| {name} | {data['score']} |\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ validated_modules.md généré.")

if __name__ == "__main__":
    export_validated_modules_md()
