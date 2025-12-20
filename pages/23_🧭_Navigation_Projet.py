# 🧭 Exploration des blocs activés
import streamlit as st
import os

st.set_page_config(page_title="🧭 Navigation Projet", layout="wide")
st.title("🧭 Navigation consolidée — Private Assistant")

st.markdown("Explore tous les blocs activés, pages disponibles et fichiers validés.")

sections = {
    "🔹 Onboarding & Synthèses": [
        "10_🧠_Synthèse_Onboarding.py",
        "15_📘_Contrats_Vocaux.py",
        "16_🧾_Certification_Final.py"
    ],
    "🔹 Diffusion & Soumission": [
        "17_📢_Diffusion_Projet.py",
        "18_🌐_Partage_Externe.py",
        "19_📤_Soumission_Projet.py"
    ],
    "🔹 Clôture & Export": [
        "20_📁_Historique_Projet.py",
        "21_📦_Export_Final.py",
        "22_📜_Attestation_Projet.py"
    ]
}

for section, pages in sections.items():
    st.subheader(section)
    for page in pages:
        st.markdown(f"- `{page}`")

st.subheader("📘 Fichiers clés")
files = [
    "bot_registry_manifest.yaml",
    "bot_registry_archive.yaml",
    "bot_registry_validation.yaml",
    "bot_registry_submission.yaml",
    "bot_registry_attestation.yaml"
]
for file in files:
    path = os.path.join("config", file)
    if os.path.exists(path):
        st.markdown(f"- 📄 `{file}`")
    else:
        st.warning(f"⚠️ Fichier manquant : {file}")

# 🔊 Ajout de bot_registry_index_vocal.yaml
st.subheader("📘 Index de manifeste vocal")

vocal_index_path = "config/bot_registry_index_vocal.yaml"
if os.path.exists(vocal_index_path):
    with open(vocal_index_path, "r") as f:
        vocal_index_content = f.read()
    st.text_area("🔊 Contenu du fichier index vocal", vocal_index_content, height=300)
else:
    st.warning("⚠️ Fichier index vocal introuvable.")

# 🧭 Ajout de bot_registry_index_navigation.yaml
st.subheader("📘 Index de navigation finale")

navigation_index_path = "config/bot_registry_index_navigation.yaml"
if os.path.exists(navigation_index_path):
    with open(navigation_index_path, "r") as f:
        navigation_index_content = f.read()
    st.text_area("🧭 Contenu du fichier index_navigation", navigation_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de navigation introuvable.")
