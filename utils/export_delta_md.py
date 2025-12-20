# import json

def export_delta_md(delta_path="config/bot_registry_delta.json", output_path="exports/bot_registry_delta.md"):
    with open(delta_path, "r") as f:
        delta = json.load(f)

    lines = ["# 🔍 Comparaison inter-version — Private Assistant\n\n"]
    for key, diff in delta.items():
        lines.append(f"## {key.replace('_vs_', ' vs ')}\n")
        for k, v in diff.items():
            if v:
                lines.append(f"### {k.capitalize()} :\n")
                for item in v:
                    lines.append(f"- {item}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_delta.md généré.")

if __name__ == "__main__":
    export_delta_md()

