# 📊 Export .csv des scores communautaires
import json
import pandas as pd

def export_scores():
    path = "exports/community_votes.json"
    votes = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            votes.append(json.loads(line))

    df = pd.DataFrame(votes)
    df_grouped = df.groupby("user").agg({"score": "mean"}).reset_index()
    df_grouped.columns = ["User", "AverageScore"]
    df_grouped.to_csv("exports/community_scores.csv", index=False)

    print("✅ Export CSV généré : community_scores.csv")

if __name__ == "__main__":
    export_scores()
