# 🔊 Lecture de la clôture officielle — Private Assistant

import streamlit as st
import os

# Bannière visuelle de clôture officielle, marque l’achèvement total du projet Private Assistant.
st.image("assets/banner_cloture_officielle.png", use_column_width=True)

st.set_page_config(page_title="🔊 Clôture Officielle", layout="wide")
st.title("🔊 Clôture officielle — Private Assistant")

# 📘 Lecture du texte
txt_path = "config/onboarding_manifest_final_closure.txt"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier texte introuvable.")

# 🔊 Lecture audio
audio_path = "config/onboarding_manifest_final_closure.mp3"
if os.path.exists(audio_path):
    st.subheader("🔊 Lecture vocale")
    st.audio(audio_path)
else:
    st.warning("⚠️ Fichier audio introuvable.")
