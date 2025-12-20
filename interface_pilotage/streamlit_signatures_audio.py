# 🔊 Rapport vocal des validations mentor
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Validations mentor", layout="centered")
st.title("🔊 Synthèse vocale — Signatures mentor")

with open("config/bot_roadmap_signatures.yaml", "r") as f:
    signatures = yaml.safe_load(f)

summary = "✍️ Validations mentor :\n"
for version, data in signatures.items():
    summary += f"Version {version} :\n"
    for mentor in data.get("mentor", []):
        summary += f"- {mentor['nom']} ({mentor['rôle']}) — Score {mentor['score']}\n"
        summary += f"  Commentaire : {mentor['commentaire']}\n"

st.text_area("📝 Synthèse vocale des signatures :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
