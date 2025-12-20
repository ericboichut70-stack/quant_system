# 📈 Script metrics_updater.py — calcul des scores et ratios
import yaml

def update_metrics(registry_path="config/module_registry.yaml", output_path="config/bot_metrics.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    total = len(registry)
    locked = [v for v in registry.values() if v["status"] == "verrouillé"]
    testing = [v for v in registry.values() if v["status"] == "actif"]
    untested = total - len(locked) - len(testing)

    def avg_score(modules):
        scores = [v["score"] for v in modules if isinstance(v["score"], (int, float))]
        return round(sum(scores) / len(scores), 2) if scores else 0

    metrics = {
        "total_modules": total,
        "verrouillés": len(locked),
        "en_test": len(testing),
        "non_testés": untested,
        "score_moyen_verrouillés": avg_score(locked),
        "score_moyen_testés": avg_score(testing),
        "progression_globale": round(len(locked) / total, 2)
    }

    with open(output_path, "w") as f:
        yaml.dump(metrics, f)

    print("✅ bot_metrics.yaml mis à jour.")

if __name__ == "__main__":
    update_metrics()
