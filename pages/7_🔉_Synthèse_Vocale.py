# 🗣️ Ecoute des résumés vocaux
import streamlit as st
import os

st.set_page_config(page_title="🔉 Synthèse vocale", layout="centered")
st.title("🔉 Écoute des résumés vocaux — Private Assistant")

audio_folder = "exports/audio"

if not os.path.exists(audio_folder):
    st.warning("⚠️ Aucun fichier audio trouvé.")
else:
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith(".wav")]
    if not audio_files:
        st.warning("⚠️ Aucun fichier .wav disponible.")
    else:
        selected = st.selectbox("🎧 Choisir un fichier audio :", audio_files)
        st.audio(os.path.join(audio_folder, selected), format="audio/wav")
        st.success(f"✅ Lecture de `{selected}` prête.")

# 🔊 Ajout de bot_registry_index_vocal.yaml
st.subheader("📘 Index vocal final")

vocal_index_path = "config/bot_registry_index_vocal.yaml"
if os.path.exists(vocal_index_path):
    with open(vocal_index_path, "r") as f:
        vocal_index_content = f.read()
    st.text_area("🔊 Contenu du fichier index_vocal", vocal_index_content, height=300)
else:
    st.warning("⚠️ Fichier index vocal introuvable.")
