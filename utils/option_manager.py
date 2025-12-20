# ✅ Interface de gestion des options pédagogiques
import streamlit as st

def option_manager(user_name):
    """
    Interface de gestion des options pédagogiques.
    """
    st.subheader("🛠️ Gestion des modules pédagogiques")

    modules = {
        "feedback_adaptatif": st.checkbox("🧠 Feedback adaptatif", value=True),
        "recommandation_personnalisée": st.checkbox("🎯 Recommandations personnalisées", value=True),
        "désactivation_dynamique": st.checkbox("🔻 Désactivation automatique", value=True),
        "coaching_hebdo": st.checkbox("📅 Coaching hebdomadaire", value=True),
        "certification": st.checkbox("🎓 Suivi de certification", value=True)
    }

    if st.button("🔄 Réinitialiser tous les paramètres"):
        modules = {k: False for k in modules}
        st.warning("⚠️ Tous les modules ont été désactivés temporairement.")

    st.success("✅ Paramètres enregistrés")
    return modules
