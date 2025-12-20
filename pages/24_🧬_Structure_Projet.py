# 🧬 Visualisation des dépendances et blocs activés
import streamlit as st
import os

st.set_page_config(page_title="🧬 Structure Projet", layout="wide")
st.title("🧬 Visualisation des dépendances et blocs activés — Private Assistant")

st.markdown("Explore la structure modulaire du projet, les blocs validés et les pages activées.")

sections = {
    "📘 Fichiers de configuration": [
        "bot_registry_manifest.yaml",
        "bot_registry_archive.yaml",
        "bot_registry_validation.yaml",
        "bot_registry_submission.yaml",
        "bot_registry_attestation.yaml"
    ],
    "📄 Documentation publique": [
        "bot_registry_onboarding.md",
        "bot_registry_contracts.md",
        "bot_registry_certification.md"
    ],
    "🔊 Synthèses vocales": [
        "onboarding_manifest_summary.mp3",
        "onboarding_certification_summary.mp3",
        "onboarding_submission_summary.mp3",
        "onboarding_cloture_summary.mp3",
        "onboarding_attestation_summary.wav"
    ],
    "📁 Pages activées": [
        "10_🧠_Synthèse_Onboarding.py",
        "15_📘_Contrats_Vocaux.py",
        "16_🧾_Certification_Final.py",
        "17_📢_Diffusion_Projet.py",
        "18_🌐_Partage_Externe.py",
        "19_📤_Soumission_Projet.py",
        "20_📁_Historique_Projet.py",
        "21_📦_Export_Final.py",
        "22_📜_Attestation_Projet.py",
        "23_🧭_Navigation_Projet.py",
        "24_🧬_Structure_Projet.py"
    ]
}

for label, items in sections.items():
    st.subheader(label)
    for item in items:
        st.markdown(f"- `{item}`")

# 🧠 Ajout de bot_registry_structure.yaml
st.subheader("📘 Fichier d’arborescence")

structure_path = "config/bot_registry_structure.yaml"
if os.path.exists(structure_path):
    with open(structure_path, "r") as f:
        structure_content = f.read()
    st.text_area("🧬 Arborescence YAML", structure_content, height=300)
else:
    st.warning("⚠️ Fichier d’arborescence introuvable.")

# Ajout de bot_registry_index_structure.yaml
st.subheader("📘 Index structurel final")

structure_index_path = "config/bot_registry_index_structure.yaml"
if os.path.exists(structure_index_path):
    with open(structure_index_path, "r") as f:
        structure_index_content = f.read()
    st.text_area("🧬 Contenu du fichier index structurel", structure_index_content, height=300)
else:
    st.warning("⚠️ Fichier index structurel introuvable.")

# Ajout de bot_registry_index_pages.yaml
st.subheader("📘 Index des pages activées")

pages_index_path = "config/bot_registry_index_pages.yaml"
if os.path.exists(pages_index_path):
    with open(pages_index_path, "r") as f:
        pages_index_content = f.read()
    st.text_area("🗂️ Contenu du fichier index_pages", pages_index_content, height=300)
else:
    st.warning("⚠️ Fichier index des pages activées introuvable.")

# 🧬 Ajout de bot_registry_index_validation.yaml
st.subheader("📘 Index de validation croisée")

validation_index_path = "config/bot_registry_index_validation.yaml"
if os.path.exists(validation_index_path):
    with open(validation_index_path, "r") as f:
        validation_index_content = f.read()
    st.text_area("🧬 Contenu du fichier index_validation", validation_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de validation croisée introuvable.")

#🧭 Carte interactive manuelle des fichiers bot_registry_index_*.yaml activés
# Chaque bloc ci-dessous peut être intégré dans une page 28_🧭_Carte_Interactive.py,
# ou injecté dans ton visualiseur YAML existant.
# 🔹 Structure du viewer
import streamlit as st
import os
import yaml

st.title("🧭 Carte interactive des fichiers index activés")

index_folder = "config/"
index_prefix = "bot_registry_index_"
index_files = [f for f in os.listdir(index_folder) if f.startswith(index_prefix) and f.endswith(".yaml")]

for filename in sorted(index_files):
    st.subheader(f"📘 {filename}")
    file_path = os.path.join(index_folder, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
        st.json(content)
    except Exception as e:
        st.error(f"Erreur de lecture : {e}")
