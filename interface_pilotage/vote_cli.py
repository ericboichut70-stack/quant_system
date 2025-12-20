# 🗳️ Interface CLI pour voter ou noter un signal
import json
from datetime import datetime

def vote_signal():
    print("\n🗳️ Vote communautaire sur un signal")
    user = input("👤 Nom d'utilisateur : ")
    scenario = input("🎭 Scénario : ")
    score = int(input("📊 Score attribué (0–100) : "))

    vote = {
        "user": user,
        "scenario": scenario,
        "score": score,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    with open("exports/community_votes.json", "a") as f:
        f.write(json.dumps(vote) + "\n")

    print("✅ Vote enregistré.")

if __name__ == "__main__":
    vote_signal()
