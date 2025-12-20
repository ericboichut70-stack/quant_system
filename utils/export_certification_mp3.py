# 🎧 Générer une version .mp3 pour diffusion externe
# 📌 Résultat : onboarding_certification_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment

def export_certification_mp3(output_path="exports/audio/onboarding_certification_summary.mp3"):
    summary = """
Clôture du projet Private Assistant.

Tous les blocs ont été validés :
- Le manifeste est versionné et archivé
- Les engagements techniques sont consignés
- Les signatures et attestations sont enregistrées
- Les synthèses vocales sont intégrées
- La certification finale est disponible

Le projet est prêt pour diffusion, onboarding collaboratif et audit contractuel.
"""

    temp_wav = "exports/audio/temp_cert.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
