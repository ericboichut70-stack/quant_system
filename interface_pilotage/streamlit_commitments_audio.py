# 🔊 Rapport vocal des engagements par version
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Engagements roadmap", layout="centered")
st.title("🔊 Synthèse vocale — Engagements roadmap")

with open("config/bot_roadmap_commitments.yaml", "r") as f:
    commitments = yaml.safe_load(f)

summary = "📜 Engagements roadmap :\n"
for version, data in commitments.items():
    summary += f"Version {version} — Certifié : {data['certifié']}, Livré : {data['livré']}\n"
    for item in data["engagements"]:
        summary += f"- {item}\n"
    summary += "\n"

st.text_area("📝 Synthèse vocale des engagements :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
