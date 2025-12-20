# 🗳️ Export .md des votes par scénario
import json
from collections import defaultdict

def export_votes_md():
    path_json = "exports/community_votes.json"
    path_md = "exports/votes_by_scenario.md"

    votes = defaultdict(list)
    with open(path_json, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            v = json.loads(line)
            votes[v["scenario"]].append((v["user"], v["score"], v["timestamp"]))

    lines = ["# 🗳️ Votes par scénario\n"]
    for scenario, entries in votes.items():
        lines.append(f"\n## {scenario}\n")
        lines.append("| Utilisateur | Score | Date |\n")
        lines.append("|-------------|-------|------|\n")
        for user, score, ts in entries:
            lines.append(f"| {user} | {score} | {ts} |\n")

    with open(path_md, "w") as f:
        f.writelines(lines)

    print("✅ votes_by_scenario.md généré.")

if __name__ == "__main__":
    export_votes_md()
