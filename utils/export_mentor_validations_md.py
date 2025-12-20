# 📋 Export .md des validations mentor
import yaml

def export_mentor_validations_md(registry_path="config/module_registry.yaml", output_path="exports/mentor_validations.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    lines = ["# 🧑‍🏫 Validations mentor — Private Assistant\n",
             "| Module | Score | Commentaire |\n",
             "|--------|-------|--------------|\n"]

    for name, data in registry.items():
        if "mentor_comment" in data:
            comment = data["mentor_comment"].replace("\n", " ")
            lines.append(f"| {name} | {data['score']} | {comment} |\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ mentor_validations.md généré.")

if __name__ == "__main__":
    export_mentor_validations_md()
