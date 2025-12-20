# 🧾 Affichage des blocs validés et clôture
import streamlit as st
import yaml
import os

st.set_page_config(page_title="🧾 Certification Finale", layout="wide")
st.title("🧾 Clôture et certification du projet — Private Assistant")

# ✅ Validation
st.subheader("✅ Validation des blocs")
validation_path = "config/bot_registry_validation.yaml"
if os.path.exists(validation_path):
    with open(validation_path, "r") as f:
        validation = yaml.safe_load(f)
    for key, value in validation.items():
        st.markdown(f"**🔹 {key}**")
        if isinstance(value, dict):
            for subkey, subval in value.items():
                st.markdown(f"- {subkey} : `{subval}`")
        else:
            st.markdown(f"`{value}`")
else:
    st.warning("⚠️ Fichier de validation introuvable.")

# 📘 Certification
st.subheader("📘 Attestation finale")
cert_path = "exports/bot_registry_certification.md"
if os.path.exists(cert_path):
    with open(cert_path, "r") as f:
        content = f.read()
    st.text_area("📄 Contenu de la certification", content, height=300)
else:
    st.warning("⚠️ Fichier de certification introuvable.")

# 🔐 Clôture
if st.button("🔐 Signer la clôture du projet"):
    st.success("✅ Clôture signée. Le projet est certifié et verrouillé.")

# 🔊 Ajouter la synthèse dans la page Certification Finale
st.subheader("🔊 Synthèse vocale de clôture")

cert_audio = "exports/audio/onboarding_certification_summary.wav"
if os.path.exists(cert_audio):
    st.audio(cert_audio, format="audio/wav")
    st.success("✅ Synthèse de certification prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 🧾 Ajout de bot_registry_index_certification.yaml
st.subheader("📘 Index de certification finale")

certification_index_path = "config/bot_registry_index_certification.yaml"
if os.path.exists(certification_index_path):
    with open(certification_index_path, "r") as f:
        certification_index_content = f.read()
    st.text_area("🧾 Contenu du fichier index_certification", certification_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de certification introuvable.")
    
# 📄 Ajout de bot_registry_index_certification.yaml
st.subheader("📘 Index de certification finale")

certification_index_path = "config/bot_registry_index_certification.yaml"
if os.path.exists(certification_index_path):
    with open(certification_index_path, "r") as f:
        certification_index_content = f.read()
    st.text_area("📄 Contenu du fichier index_certification", certification_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de certification introuvable.")
