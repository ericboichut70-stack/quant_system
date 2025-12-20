# 🧑‍🏫 Automatisation de mentor_validations.md
import json
from datetime import datetime

def update_mentor_md():
    json_path = "exports/mentor_validations.json"
    md_path = "exports/mentor_validations.md"

    lines = []
    lines.append("# 🧑‍🏫 Tableau des validations mentorales\n")
    lines.append("| Scénario | Score | Décision | Commentaire | Date |\n")
    lines.append("|----------|-------|----------|-------------|------|\n")

    try:
        with open(json_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                v = json.loads(line)
                lines.append(f"| {v['scenario']} | {v['score']} | {v['decision']} | {v['comment']} | {v['timestamp']} |\n")
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return

    with open(md_path, "w") as f:
        f.writelines(lines)

    print("✅ mentor_validations.md mis à jour.")

if __name__ == "__main__":
    update_mentor_md()
