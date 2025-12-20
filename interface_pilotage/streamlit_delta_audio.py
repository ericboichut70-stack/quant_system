# 🔊 Générer un rapport vocal des écarts entre versions
import streamlit as st
import json
import pyttsx3

st.set_page_config(page_title="🔊 Écarts entre versions", layout="centered")
st.title("🔊 Synthèse vocale — Comparaison de versions")

with open("config/bot_registry_delta.json", "r") as f:
    delta = json.load(f)

summary = "🔍 Comparaison entre versions :\n"
for key, diff in delta.items():
    summary += f"{key.replace('_vs_', ' vs ')} :\n"
    for k, v in diff.items():
        if v:
            summary += f"{k.capitalize()} : {', '.join(v)}\n"
    summary += "\n"

st.text_area("📝 Synthèse vocale des écarts :", summary, height=300)

if st.button("🔊 Lire à voix haute"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    st.success("Lecture terminée.")
