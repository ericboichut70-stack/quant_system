# 🗂️ Exploration de tous les fichiers .yaml du projet
import streamlit as st
import os

st.set_page_config(page_title="🗂️ Index Manifestes", layout="wide")
st.title("🗂️ Index des fichiers YAML — Private Assistant")

st.markdown("Visualise tous les fichiers de structure, validation, mémoire et soumission.")

yaml_dir = "config"
yaml_files = [f for f in os.listdir(yaml_dir) if f.endswith(".yaml")]

for file in sorted(yaml_files):
    path = os.path.join(yaml_dir, file)
    st.markdown(f"- 📄 `{file}`")

# 🗂️ Ajout de bot_registry_index_manifestes.yaml
st.subheader("📘 Index final des fichiers manifeste")

manifestes_index_path = "config/bot_registry_index_manifestes.yaml"
if os.path.exists(manifestes_index_path):
    with open(manifestes_index_path, "r") as f:
        manifestes_index_content = f.read()
    st.text_area("🗂️ Contenu du fichier index_manifestes", manifestes_index_content, height=300)
else:
    st.warning("⚠️ Fichier index_manifestes introuvable.")

# 🗂️ Ajout de bot_registry_index_manifestes.yaml
st.subheader("📘 Index des manifestes activés")

manifestes_index_path = "config/bot_registry_index_manifestes.yaml"
if os.path.exists(manifestes_index_path):
    with open(manifestes_index_path, "r") as f:
        manifestes_index_content = f.read()
    st.text_area("🗂️ Contenu du fichier index_manifestes", manifestes_index_content, height=300)
else:
    st.warning("⚠️ Fichier index des manifestes introuvable.")

# Ajout de bot_registry_index_complet.yaml
st.subheader("📘 Index complet final")

complet_index_path = "config/bot_registry_index_complet.yaml"
if os.path.exists(complet_index_path):
    with open(complet_index_path, "r") as f:
        complet_index_content = f.read()
    st.text_area("🗂️ Contenu du fichier index_complet", complet_index_content, height=300)
else:
    st.warning("⚠️ Fichier index complet introuvable.")
