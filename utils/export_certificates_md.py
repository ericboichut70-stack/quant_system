# 📋 Export .md des certificats techniques
import yaml

def export_certificates_md(cert_path="config/bot_registry_certificates.yaml", output_path="exports/bot_registry_certificates.md"):
    with open(cert_path, "r") as f:
        certs = yaml.safe_load(f)

    lines = ["# 📜 Certificats techniques — Private Assistant\n\n"]
    for version, data in certs.items():
        lines.append(f"## Version {version} — {data['date']}\n")
        lines.append(f"- Certificat : {data['certificat']}\n")
        lines.append(f"- Validé par : {data['validé_par']}\n")
        lines.append(f"- Score : {data['score']}\n")
        lines.append("### Artefacts liés :\n")
        for art in data["artefacts"]:
            lines.append(f"- {art}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_certificates.md généré.")

if __name__ == "__main__":
    export_certificates_md()
