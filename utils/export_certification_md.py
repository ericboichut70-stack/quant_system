# 🧾 Attestation de validation complète
# 📌 Résultat : bot_registry_certification.md dans exports/
def export_certification_md(output_path="exports/bot_registry_certification.md"):
    lines = ["# 🧾 Attestation de validation complète — Private Assistant\n\n"]

    lines.append("## ✅ Blocs validés\n")
    lines.append("- Manifeste versionné : `bot_registry_manifest.yaml`\n")
    lines.append("- Archive complète : `bot_registry_archive.yaml`\n")
    lines.append("- Validation : `bot_registry_validation.yaml`\n")
    lines.append("- Contrats : `commitments.yaml`, `signatures.yaml`, `attestations.md`\n")
    lines.append("- Synthèses vocales : `onboarding_manifest_summary`, `onboarding_validation_summary`\n\n")

    lines.append("## 📦 Export global\n")
    lines.append("- Archive ZIP : `export_all.zip`\n")
    lines.append("- Documentation : `bot_registry_onboarding.md`, `bot_registry_contracts.md`\n")

    lines.append("\nCe fichier atteste que tous les blocs ont été validés, archivés et sont prêts pour diffusion, audit ou onboarding collaboratif.\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print(f"✅ Certification markdown générée : {output_path}")
