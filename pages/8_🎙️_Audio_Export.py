# 🗂️ Gestion des formats vocaux
import streamlit as st
import yaml
import os

st.set_page_config(page_title="🎙️ Audio Export", layout="wide")
st.title("🎙️ Gestion des formats vocaux — Private Assistant")

with open("config/bot_registry_audio.yaml", "r") as f:
    audio_index = yaml.safe_load(f)

for filename, meta in audio_index.items():
    with st.expander(f"🔉 {filename}", expanded=False):
        st.markdown(f"- **Rôle** : {meta['rôle']}")
        st.markdown(f"- **Format** : `{meta['format']}`")
        st.markdown(f"- **Source** : `{meta['source']}`")
        st.markdown(f"- **Usage** : {meta['usage']}")
        audio_path = os.path.join("exports/audio", filename)
        if os.path.exists(audio_path):
            st.audio(audio_path, format=f"audio/{meta['format']}")
        else:
            st.warning("⚠️ Fichier audio non trouvé.")
