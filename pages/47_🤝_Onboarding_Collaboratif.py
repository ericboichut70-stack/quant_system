# 🤝 Lecture du manifeste d’onboarding collaboratif — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🤝 Onboarding collaboratif", layout="wide")
st.title("🤝 Onboarding collaboratif — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_onboarding_collaboratif.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_onboarding_collaboratif.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
