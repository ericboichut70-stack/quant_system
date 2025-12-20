# 🏷️ Interface CLI pour attribuer les rôles selon roles_badges.yaml
import yaml

def assign_role_from_yaml(score):
    with open("config/roles_badges.yaml", "r") as f:
        config = yaml.safe_load(f)

    for role, data in config["roles"].items():
        if score >= data["min_score"]:
            return data["badge"], role
    return "❌", "Non défini"

def cli():
    print("\n🎭 Attribution de rôle selon score")
    score = int(input("📊 Score moyen : "))
    badge, role = assign_role_from_yaml(score)
    print(f"🏅 Badge : {badge} | Rôle : {role}")

if __name__ == "__main__":
    cli()
