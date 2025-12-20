# ✅ Bloc bot_validator.py — vérification avant certification
import yaml

def validate_bot(registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    locked = [data for data in registry.values() if data["status"] == "verrouillé"]
    if not locked:
        print("❌ Aucun module verrouillé — certification impossible.")
        return False

    scores = [data["score"] for data in locked if isinstance(data["score"], (int, float))]
    if not scores or min(scores) < 80:
        print("❌ Score insuffisant — tous les modules doivent avoir ≥ 80.")
        return False

    print("✅ Conformité validée — certification possible.")
    return True

if __name__ == "__main__":
    validate_bot()
