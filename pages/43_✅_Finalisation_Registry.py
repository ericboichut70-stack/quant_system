# ✅ Lecture du manifeste de finalisation — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="✅ Finalisation Registry", layout="wide")
st.title("✅ Finalisation Registry — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_finalisation_registry.png", use_column_width=True)

# 📘 Lecture du manifeste YAML
yaml_path = "bot_registry_manifest_finalisation.yaml"
if os.path.exists(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Manifest Finalisation")
        st.code(f.read(), language="yaml")
else:
    st.warning("⚠️ Fichier YAML introuvable.")
