# 🔊 Synthèse vocale finale — Private Assistant
# Affiché ici pour une lecture dédiée

import streamlit as st
import os

st.set_page_config(page_title="🔊 Synthèse Finale", layout="wide")
st.title("🔊 Synthèse vocale finale — Private Assistant")

# 📘 Lecture du manifeste texte
txt_path = "config/onboarding_final_project_summary.txt"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte de la synthèse finale")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier texte de synthèse finale introuvable.")

# 🔊 Lecture de la synthèse vocale
audio_path = "config/onboarding_final_project_summary.mp3"
if os.path.exists(audio_path):
    st.subheader("🔊 Lecture vocale")
    st.audio(audio_path)
else:
    st.warning("⚠️ Fichier audio de synthèse finale introuvable.")

# 🎬 Intégration de la bannière visuelle de synthèse finale avec animation d’entrée
import streamlit as st
import time

st.set_page_config(page_title="🔊 Synthèse Finale", layout="wide")
st.title("🔊 Synthèse vocale finale — Private Assistant")

# 🎬 Animation d’entrée
with st.spinner("Chargement de la synthèse finale…"):
    time.sleep(1.5)
    st.image("assets/banner_synthese_finale.png", use_column_width=True)

# 📘 Texte de la synthèse
txt_path = "config/onboarding_final_project_summary.txt"
if txt_path:
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte de la synthèse finale")
        st.text(f.read())

# 🔊 Audio
audio_path = "config/onboarding_final_project_summary.mp3"
if audio_path:
    st.subheader("🔊 Lecture vocale")
    st.audio(audio_path)

# 🎬 Intégration de la bannière visuelle de synthèse finale avec animation d’entrée
st.image("assets/banner_synthese_finale.png", use_column_width=True)
