# 📋 Tableau .md des modules non testés avec priorisation
import yaml

def export_prioritized_untested(registry_path="config/module_registry.yaml", output_path="exports/untested_prioritized.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    lines = ["# 🧪 Modules non testés — Priorisation\n",
             "| Module | Export | Replay |\n",
             "|--------|--------|--------|\n"]

    for name, data in registry.items():
        if data["status"] not in ["verrouillé", "actif"]:
            lines.append(f"| {name} | {data['export']} | {data['replay']} |\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ untested_prioritized.md généré.")

if __name__ == "__main__":
    export_prioritized_untested()
