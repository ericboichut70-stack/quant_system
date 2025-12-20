# 🏅 Lecture consolidée
# 🏅 Certification communautaire — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🏅 Certification Communautaire", layout="wide")
st.title("🏅 Certification communautaire — Private Assistant")

# 📘 Lecture de la synthèse Markdown
md_path = "config/bot_registry_certification_communautaire.md"
if os.path.exists(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    st.markdown(md_content)
else:
    st.warning("⚠️ Fichier Markdown de certification communautaire introuvable.")

# 🔊 Lecture de la synthèse vocale
audio_path = "config/onboarding_certification_communautaire_summary.mp3"
if os.path.exists(audio_path):
    st.audio(audio_path)
else:
    st.warning("⚠️ Synthèse vocale communautaire introuvable.")
