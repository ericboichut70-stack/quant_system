# 🎧 Générer la version .mp3 de l’attestation finale
# 📌 Résultat : onboarding_attestation_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment
from datetime import datetime

def export_attestation_mp3(output_path="exports/audio/onboarding_attestation_summary.mp3"):
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

    temp_wav = "exports/audio/temp_attestation.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
