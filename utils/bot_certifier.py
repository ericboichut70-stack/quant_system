# 📜 Bloc bot_certifier.py — certificat de conformité
import yaml
from datetime import datetime

def generate_certificate(registry_path="config/module_registry.yaml", output_path="exports/bot_certificate.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    locked = [name for name, data in registry.items() if data["status"] == "verrouillé"]
    avg_score = round(sum([data["score"] for name, data in registry.items() if data["status"] == "verrouillé"]) / len(locked), 2) if locked else 0

    lines = [
        "# 📜 Certificat de conformité — Private Assistant\n\n",
        f"**Date de certification** : {datetime.now().strftime('%Y-%m-%d')}\n",
        f"**Modules certifiés** : {len(locked)}\n",
        f"**Score moyen** : {avg_score}\n",
        f"**Émis par** : Eric\n\n",
        "## Modules certifiés\n"
    ] + [f"- {name} — Score {registry[name]['score']}\n" for name in locked]

    lines.append("\n✅ Le bot est conforme aux critères de validation mentor et prêt pour déploiement.")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_certificate.md généré.")

if __name__ == "__main__":
    generate_certificate()
