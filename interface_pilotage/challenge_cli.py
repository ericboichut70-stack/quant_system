# 🧑‍🏫 Interface CLI pour lancer ou suivre les défis
from modules.signal_challenges import generate_challenge, assign_level

def launch_challenge():
    print("\n🎮 Lancement de défi pédagogique")
    scenario = input("🎭 Scénario : ")
    score = int(input("📊 Score : "))

    level = assign_level(score)
    challenge = generate_challenge(scenario, level)

    print(f"\n📈 Niveau : {level}")
    print(f"📜 Défi : {challenge}")

if __name__ == "__main__":
    launch_challenge()
