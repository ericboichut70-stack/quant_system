# 📋 Tableau .md des modules verrouillés
import yaml

def export_locked_modules(registry_path="config/module_registry.yaml", output_path="exports/locked_modules.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    lines = ["# 🔒 Modules verrouillés — Private Assistant\n",
             "| Module | Score | Replay | Export |\n",
             "|--------|-------|--------|--------|\n"]

    for name, data in registry.items():
        if data["status"] == "verrouillé":
            lines.append(f"| {name} | {data['score']} | {data['replay']} | {data['export']} |\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ locked_modules.md généré.")

if __name__ == "__main__":
    export_locked_modules()
