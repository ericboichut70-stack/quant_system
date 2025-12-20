# 🎧 Générer la version .mp3 de clôture officielle
# 📌 Résultat : onboarding_cloture_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment
from datetime import datetime

def export_cloture_mp3(output_path="exports/audio/onboarding_cloture_summary.mp3"):
    now = datetime.now().strftime("%d %B %Y à %Hh%M")
    version = "1.0.0"

    summary = f"""
Clôture officielle du projet Private Assistant.

Version : {version}
Date : {now}

Tous les blocs ont été validés, archivés et soumis :
- Manifeste versionné
- Contrats et attestations
- Synthèses vocales
- Certification finale
- Archive complète

Le projet est verrouillé et prêt pour diffusion.
"""

    temp_wav = "exports/audio/temp_cloture.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
