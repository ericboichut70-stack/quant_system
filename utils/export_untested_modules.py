# 📋 Export .md des modules non encore testés
import yaml

def export_untested_modules(registry_path="config/module_registry.yaml", output_path="exports/untested_modules.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    lines = ["# 🧪 Modules non testés — Private Assistant\n",
             "| Module | Status | Score |\n",
             "|--------|--------|--------|\n"]

    for name, data in registry.items():
        if data["status"] != "verrouillé":
            lines.append(f"| {name} | {data['status']} | {data['score']} |\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ untested_modules.md généré.")

if __name__ == "__main__":
    export_untested_modules()
