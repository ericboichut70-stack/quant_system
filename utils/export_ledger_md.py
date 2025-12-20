# 📋 Export .md du ledger
import yaml

def export_ledger_md(ledger_path="config/bot_registry_ledger.yaml", output_path="exports/bot_registry_ledger.md"):
    with open(ledger_path, "r") as f:
        ledger = yaml.safe_load(f)

    lines = ["# 📒 Registre comptable des livraisons — Private Assistant\n\n"]
    for entry in ledger:
        lines.append(f"- 📅 {entry['date']} — Version {entry['version']}\n")
        lines.append(f"  ➤ Action : {entry['action']}\n")
        lines.append(f"  ➤ Artefact : {entry['artefact']}\n")
        lines.append(f"  ➤ Validé par : {entry['validé_par']}\n\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_ledger.md généré.")

if __name__ == "__main__":
    export_ledger_md()
