# 🎧 Générer la version .mp3 de la synthèse de soumission
# 📌 Résultat : onboarding_submission_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment
from datetime import datetime

def export_submission_mp3(output_path="exports/audio/onboarding_submission_summary.mp3"):
    now = datetime.now().strftime("%d %B %Y à %Hh%M")
    version = "1.0.0"

    summary = f"""
Soumission officielle du projet Private Assistant.

Version : {version}
Date : {now}

Tous les blocs publics sont validés :
- Documentation consolidée
- Synthèses vocales
- Archive complète
- Certification finale

Le projet est prêt pour diffusion vers mentor, archive et communauté.
"""

    temp_wav = "exports/audio/temp_submission.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
