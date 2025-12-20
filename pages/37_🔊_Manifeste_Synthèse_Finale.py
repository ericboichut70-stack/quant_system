# 📄 Page de lecture dédiée
# 🔊 Lecture du manifeste vocal final — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🔊 Manifeste Final", layout="wide")
st.title("🔊 Synthèse vocale — Manifest Final")

# 📘 Lecture du texte
txt_path = "config/onboarding_manifest_synthese_finale.txt"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier texte introuvable.")

# 🔊 Lecture audio
audio_path = "config/onboarding_manifest_synthese_finale.mp3"
if os.path.exists(audio_path):
    st.subheader("🔊 Lecture vocale")
    st.audio(audio_path)
else:
    st.warning("⚠️ Fichier audio introuvable.")
