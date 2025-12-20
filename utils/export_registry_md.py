# 📋 Export .md du registre consolidé
import yaml

def export_registry_md(registry_path="config/bot_roadmap_registry.yaml", output_path="exports/bot_roadmap_registry.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    lines = ["# 📚 Registre roadmap consolidé — Private Assistant\n\n"]
    for version, data in registry.items():
        lines.append(f"## Version {version}\n")
        for key, value in data.items():
            if isinstance(value, list):
                lines.append(f"- {key} : {', '.join(value)}\n")
            else:
                lines.append(f"- {key} : {value}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_roadmap_registry.md généré.")

if __name__ == "__main__":
    export_registry_md()
