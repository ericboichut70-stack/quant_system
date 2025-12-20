# 🔊 Synthèse vocale “Attestation finale”
# 📌 Résultat : onboarding_attestation_summary.wav dans exports/audio/
import pyttsx3
from datetime import datetime

def export_attestation_vocal(output_path="exports/audio/onboarding_attestation_summary.wav"):
    now = datetime.now().strftime("%d %B %Y à %Hh%M")
    version = "1.0.0"

    summary = f"""
Attestation finale du projet Private Assistant.

Version : {version}
Date : {now}
Signataire : Eric

Tous les blocs ont été validés, archivés et soumis :
- Manifeste versionné
- Contrats et attestations
- Synthèses vocales
- Certification et soumission
- Clôture officielle

Le projet est certifié et prêt pour diffusion.
"""

    engine = pyttsx3.init()
    engine.save_to_file(summary, output_path)
    engine.runAndWait()
    print(f"✅ Synthèse vocale d’attestation exportée : {output_path}")
