# 🔊 Résumé vocal des objectifs post-1.0.0
import streamlit as st
import yaml
import pyttsx3

st.set_page_config(page_title="🔊 Feuille de route", layout="centered")
st.title("🔊 Synthèse vocale — Objectifs post-1.0.0")

with open("config/bot_roadmap.yaml", "r") as f:
    roadmap = yaml.safe_load(f)

summary = f"Version prévue : {roadmap['next_version']} — Date : {roadmap['planned_date']}\n"
summary += "Objectifs :\n"
for obj in roadmap["objectifs"]:
    summary += f"- {obj}\n"

st.text_area("📝 Résumé vocal de la roadmap :", summary, height=250)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
