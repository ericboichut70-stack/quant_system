# 📋 Export .md des modules verrouillés par bot_finalizer.py
import yaml

def export_finalized_modules_md(registry_path="config/module_registry.yaml", output_path="exports/finalized_modules.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    lines = ["# 🔒 Modules verrouillés — Finalisation\n",
             "| Module | Score | Replay | Export |\n",
             "|--------|-------|--------|--------|\n"]

    for name, data in registry.items():
        if data["status"] == "verrouillé":
            lines.append(f"| {name} | {data['score']} | {data['replay']} | {data['export']} |\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ finalized_modules.md généré.")

if __name__ == "__main__":
    export_finalized_modules_md()
