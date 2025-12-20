# 🎧 Version .mp3 de la synthèse de mémoire
# 📌 Résultat : onboarding_memory_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment

def export_memory_mp3(output_path="exports/audio/onboarding_memory_summary.mp3"):
    summary = """
Mémoire consolidée du projet Private Assistant.

Elle regroupe les intentions, signatures, attestations, validations, soumission et clôture.
Tous les blocs sont archivés et prêts pour audit, transmission ou onboarding collaboratif.
"""

    temp_wav = "exports/audio/temp_memory.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
