# 🧑‍🤝‍🧑 Automatisation du tableau community_roles.md depuis les votes
import json
import pandas as pd
from modules.community_scoring import aggregate_scores, assign_role

def update_roles_md():
    path_json = "exports/community_votes.json"
    path_md = "exports/community_roles.md"

    votes = []
    with open(path_json, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            votes.append(json.loads(line))

    df = pd.DataFrame(votes)
    grouped = df.groupby("user").agg({"score": "mean"}).reset_index()
    grouped.columns = ["Utilisateur", "Moyenne"]

    lines = ["# 👥 Rôles attribués — Private Assistant\n",
             "| Utilisateur | Moyenne des scores | Rôle attribué |\n",
             "|-------------|--------------------|----------------|\n"]

    for _, row in grouped.iterrows():
        role = assign_role(row["Moyenne"])
        lines.append(f"| {row['Utilisateur']} | {round(row['Moyenne'],2)} | {role} |\n")

    with open(path_md, "w") as f:
        f.writelines(lines)

    print("✅ community_roles.md mis à jour.")

if __name__ == "__main__":
    update_roles_md()
