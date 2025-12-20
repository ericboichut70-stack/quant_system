# 🔊 Rapport vocal du manifeste figé
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Manifeste figé", layout="centered")
st.title("🔊 Synthèse vocale — Manifeste figé")

with open("config/bot_registry_manifest.yaml", "r") as f:
    manifest = yaml.safe_load(f)

summary = f"""
📘 Manifeste figé — Version {manifest['version']}
Livré le {manifest['date']} par {manifest['auteur']}.
Modules verrouillés : {', '.join(manifest['modules_verrouillés'])}.
Score moyen : {manifest['score_moyen']}.
Contrat : {manifest['contrat']}, Certificat : {manifest['certificat']}.
Archive : {manifest['archive']}, Gel : {manifest['gel']}.
"""

st.text_area("📝 Synthèse vocale du manifeste :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
