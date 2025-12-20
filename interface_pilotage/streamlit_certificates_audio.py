# 🔊 Rapport vocal des certificats validés
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Certificats techniques", layout="centered")
st.title("🔊 Synthèse vocale — Certificats validés")

with open("config/bot_registry_certificates.yaml", "r") as f:
    certs = yaml.safe_load(f)

summary = "📜 Certificats techniques validés :\n"
for version, data in certs.items():
    summary += f"Version {version} — {data['date']}\n"
    summary += f"Validé par {data['validé_par']}, score : {data['score']}\n"
    summary += f"Certificat : {data['certificat']}\n\n"

st.text_area("📝 Synthèse vocale des certificats :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
