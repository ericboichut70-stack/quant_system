# 🔊 Résumé vocal du manifeste final
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Manifeste final", layout="centered")
st.title("🔊 Synthèse vocale — Manifeste final")

with open("config/bot_manifest_final.yaml", "r") as f:
    manifest = yaml.safe_load(f)

summary = f"""
Version {manifest['version']} — {manifest['release_date']}
Modules verrouillés : {', '.join(manifest['modules_verrouillés'])}
Score moyen certifié : {manifest['certification']['score_moyen']}
Statut : {manifest['status']}
Fonctionnalités activées : {', '.join([k for k, v in manifest['features'].items() if v])}
"""

st.text_area("📝 Résumé vocal du manifeste :", summary, height=200)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
