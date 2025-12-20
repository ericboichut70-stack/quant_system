# 🔁 Relecture des intégrations
# 🔁 Relecture des intégrations — Private Assistant

import streamlit as st
import yaml
import os

st.set_page_config(page_title="🔁 Replay Validation", layout="wide")
st.title("🔁 Relecture des intégrations — Private Assistant")

replay_path = "config/bot_registry_replay.yaml"

if os.path.exists(replay_path):
    with open(replay_path, "r") as f:
        replay_data = yaml.safe_load(f)

    st.subheader("🔁 Séquence de relecture")
    for step in replay_data.get("replay_sequence", []):
        st.markdown(f"- 🔁 {step}")

    st.subheader("🧠 Logique de relecture")
    for line in replay_data.get("logique", []):
        st.markdown(f"- {line}")
else:
    st.warning("⚠️ Fichier de relecture introuvable.")
