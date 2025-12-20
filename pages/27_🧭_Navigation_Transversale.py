# 🧭 Carte logique des pages activées
import streamlit as st

st.set_page_config(page_title="🧭 Navigation Transversale", layout="wide")
st.title("🧭 Carte logique des pages activées — Private Assistant")

sections = {
    "🧠 Onboarding & Mémoire": ["10_🧠_Synthèse_Onboarding.py", "25_🧠_Mémoire_Projet.py"],
    "📘 Contrats & Certification": ["15_📘_Contrats_Vocaux.py", "16_🧾_Certification_Final.py", "22_📜_Attestation_Projet.py"],
    "📢 Diffusion & Soumission": ["17_📢_Diffusion_Projet.py", "18_🌐_Partage_Externe.py", "19_📤_Soumission_Projet.py"],
    "📁 Historique & Export": ["20_📁_Historique_Projet.py", "21_📦_Export_Final.py", "26_🗂️_Index_Manifestes.py"],
    "🧭 Navigation": ["23_🧭_Navigation_Projet.py", "27_🧭_Navigation_Transversale.py"]
}

for label, pages in sections.items():
    st.subheader(label)
    for page in pages:
        st.markdown(f"- `{page}`")

# 🧭 Ajout de bot_registry_index_pages.yaml
st.subheader("📘 Index YAML des pages activées")

index_pages_path = "config/bot_registry_index_pages.yaml"
if os.path.exists(index_pages_path):
    with open(index_pages_path, "r") as f:
        index_pages_content = f.read()
    st.text_area("🧭 Contenu du fichier index_pages", index_pages_content, height=300)
else:
    st.warning("⚠️ Fichier index_pages introuvable.")
