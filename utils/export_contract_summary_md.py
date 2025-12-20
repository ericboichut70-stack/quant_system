# 📘 Fichier .md récapitulatif des blocs contractuels et vocaux
# 📌 Résultat : bot_registry_contracts.md dans exports/
def export_contract_summary_md(output_path="exports/bot_registry_contracts.md"):
    lines = ["# 📘 Synthèse des blocs contractuels et vocaux — Private Assistant\n\n"]

    lines.append("## 📚 Contrats et engagements\n")
    lines.append("- `bot_roadmap_commitments.yaml` : engagements techniques et livrables\n")
    lines.append("- `bot_roadmap_signatures.yaml` : signatures et validations\n")
    lines.append("- `bot_roadmap_attestations.md` : attestations mentor et conformité\n\n")

    lines.append("## 🔊 Synthèses vocales contractuelles\n")
    lines.append("- `onboarding_manifest_summary.wav` : version interne\n")
    lines.append("- `onboarding_manifest_summary.mp3` : version externe\n")
    lines.append("- Usage : onboarding contractuel, documentation, validation\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print(f"✅ Fichier markdown généré : {output_path}")
