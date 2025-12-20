# 📂 Page 11_📦_Export_Global.py — visualisation de tous les fichiers .md, .wav, .mp3, .yaml
import streamlit as st
import os

st.set_page_config(page_title="📦 Export Global", layout="wide")
st.title("📦 Visualisation des exports — Private Assistant")

folders = {
    "Markdown (.md)": "exports",
    "Audio WAV (.wav)": "exports/audio",
    "Audio MP3 (.mp3)": "exports/audio",
    "YAML (.yaml)": "config"
}

for label, folder in folders.items():
    st.subheader(f"📁 {label}")
    if not os.path.exists(folder):
        st.warning(f"Dossier introuvable : {folder}")
        continue

    files = [f for f in os.listdir(folder) if f.endswith(label.split()[1])]
    if not files:
        st.info("Aucun fichier trouvé.")
    else:
        for f in sorted(files):
            st.markdown(f"- `{f}`")
