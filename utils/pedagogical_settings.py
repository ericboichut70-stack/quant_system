# ✅ Interface de paramétrage pédagogique
import streamlit as st

def pedagogical_settings():
    """
    Interface de paramétrage pédagogique personnalisée.
    """
    st.subheader("⚙️ Paramétrage pédagogique")

    mode = st.selectbox("🎓 Mode d’apprentissage", ["Autonome", "Mentoré", "Collaboratif"])
    difficulty = st.select_slider("📈 Niveau de difficulté ciblé", options=["Débutant", "Intermédiaire", "Avancé"])
    deactivation_threshold = st.slider("🔻 Seuil de désactivation automatique", -5, 5, -3)
    focus = st.multiselect("🎯 Objectifs pédagogiques", ["Compréhension", "Validation", "Cohérence", "Diversité", "Autonomie"])

    settings = {
        "mode": mode,
        "difficulty": difficulty,
        "deactivation_threshold": deactivation_threshold,
        "focus": focus
    }

    st.success("✅ Paramètres pédagogiques enregistrés")
    return settings
