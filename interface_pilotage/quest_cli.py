# 🎮 Interface CLI pour lancer des quêtes
from modules.narration_quests import generate_quest, assign_badge

def launch_quest():
    print("\n🎮 Lancement de quête pédagogique")
    scenario = input("🎭 Scénario : ")
    score = int(input("📊 Score : "))

    quest = generate_quest(scenario, score)
    badge = assign_badge(score)

    print(f"\n🏅 Badge attribué : {badge}")
    print(f"📜 Quête : {quest}")

if __name__ == "__main__":
    launch_quest()
