# 📁 Page 20_📁_Historique_Projet.py — visualisation des étapes validées
import streamlit as st
import yaml
import os

st.set_page_config(page_title="📁 Historique Projet", layout="wide")
st.title("📁 Historique des validations et soumissions — Private Assistant")

files = {
    "Validation": "config/bot_registry_validation.yaml",
    "Soumission": "config/bot_registry_submission.yaml"
}

for label, path in files.items():
    st.subheader(f"📄 {label}")
    if not os.path.exists(path):
        st.warning(f"⚠️ Fichier introuvable : {path}")
        continue
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    for key, value in data.items():
        if isinstance(value, list):
            st.markdown(f"**🔹 {key}**")
            for item in value:
                st.markdown(f"- {item}")
        else:
            st.markdown(f"- **{key}** : `{value}`")

# 📜 Ajout de bot_registry_historique.yaml
st.subheader("📁 Historique final du projet")

historique_path = "config/bot_registry_historique.yaml"
if os.path.exists(historique_path):
    with open(historique_path, "r") as f:
        historique_content = f.read()
    st.text_area("📘 Contenu du fichier historique", historique_content, height=300)
else:
    st.warning("⚠️ Fichier historique introuvable.")

# 📜 Ajout de bot_registry_cloture_vocale.yaml
st.subheader("🧠 Synthèses de clôture vocale")

cloture_vocale_path = "config/bot_registry_cloture_vocale.yaml"
if os.path.exists(cloture_vocale_path):
    with open(cloture_vocale_path, "r") as f:
        cloture_vocale_content = f.read()
    st.text_area("📘 Index des synthèses de clôture", cloture_vocale_content, height=300)
else:
    st.warning("⚠️ Fichier de clôture vocale introuvable.")

# 📁 Ajout de bot_registry_index_cloture.yaml
st.subheader("📘 Index de clôture finale")

cloture_index_path = "config/bot_registry_index_cloture.yaml"
if os.path.exists(cloture_index_path):
    with open(cloture_index_path, "r") as f:
        cloture_index_content = f.read()
    st.text_area("📁 Contenu du fichier index_cloture", cloture_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de clôture introuvable.")

# 📁 Ajout de bot_registry_index_historique.yaml
st.subheader("📘 Index d’historique final")

historique_index_path = "config/bot_registry_index_historique.yaml"
if os.path.exists(historique_index_path):
    with open(historique_index_path, "r") as f:
        historique_index_content = f.read()
    st.text_area("📁 Contenu du fichier index_historique", historique_index_content, height=300)
else:
    st.warning("⚠️ Fichier index d’historique introuvable.")

# 📁 Ajout de bot_registry_index_cloture.yaml
st.subheader("📘 Index de clôture totale")

cloture_index_path = "config/bot_registry_index_cloture.yaml"
if os.path.exists(cloture_index_path):
    with open(cloture_index_path, "r") as f:
        cloture_index_content = f.read()
    st.text_area("📁 Contenu du fichier index_cloture", cloture_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de clôture introuvable.")

# 🧾 Ajout de bot_registry_index_attestation.yaml
st.subheader("📘 Index d’attestation finale")

attestation_index_path = "config/bot_registry_index_attestation.yaml"
if os.path.exists(attestation_index_path):
    with open(attestation_index_path, "r") as f:
        attestation_index_content = f.read()
    st.text_area("🧾 Contenu du fichier index_attestation", attestation_index_content, height=300)
else:
    st.warning("⚠️ Fichier index d’attestation introuvable.")

# 📜 Ajout de bot_registry_attestation_publique.md
st.subheader("📜 Attestation publique — Private Assistant")

attestation_md_path = "config/bot_registry_attestation_publique.md"
if os.path.exists(attestation_md_path):
    with open(attestation_md_path, "r", encoding="utf-8") as f:
        attestation_md_content = f.read()
    st.markdown(attestation_md_content)
else:
    st.warning("⚠️ Fichier Markdown d’attestation publique introuvable.")
