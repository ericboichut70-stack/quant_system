# ✅ Lecture du rapport de test — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="✅ Rapport de Test Registry", layout="wide")
st.title("✅ Rapport de Test — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_test_report.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_test_report.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Rapport consigné")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier rapport introuvable.")

# 🔊 Lecture audio (optionnel si version vocale générée)
audio_path = "config/onboarding_test_report.mp3"
if os.path.exists(audio_path):
    st.subheader("🔊 Lecture vocale")
    st.audio(audio_path)
else:
    st.info("ℹ️ Pas de version vocale disponible pour ce rapport.")
