# 🧾 Navigation dans tous les blocs du manifeste
import streamlit as st
import yaml
import os

st.set_page_config(page_title="🧾 Manifeste Interactif", layout="wide")
st.title("🧾 Navigation dans le manifeste — Private Assistant")

manifest_path = "config/bot_registry_manifest.yaml"

if not os.path.exists(manifest_path):
    st.warning("⚠️ Fichier `bot_registry_manifest.yaml` introuvable.")
else:
    with open(manifest_path, "r") as f:
        manifest = yaml.safe_load(f)

    versions = list(manifest.keys())
    selected = st.selectbox("📌 Choisir une version :", versions)

    st.subheader(f"📄 Blocs de la version {selected}")
    for key, value in manifest[selected].items():
        st.markdown(f"### 🔹 {key}")
        if isinstance(value, list):
            for item in value:
                st.markdown(f"- `{item}`")
        else:
            st.markdown(f"`{value}`")
