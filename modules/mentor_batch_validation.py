# ✅ Interface de validation en lot
# 🎯 Objectif : Permettre à un mentor de valider plusieurs signaux d’un élève en une seule action.
import streamlit as st

def batch_validation_interface(feedback_df, user_list):
    st.subheader("📦 Validation en lot mentorale")

    selected_user = st.selectbox("👤 Élève à valider", user_list)
    user_df = feedback_df[feedback_df["user"] == selected_user]

    to_validate = st.multiselect("🎭 Sélectionner les scénarios à valider", user_df["ScenarioType"].unique())

    comment = st.text_area("📝 Commentaire global", height=100)

    if st.button("✅ Valider en lot"):
        from datetime import datetime
        with open("utils/batch_validation_log.txt", "a", encoding="utf-8") as f:
            for scenario in to_validate:
                f.write(f"{datetime.now()} | {selected_user} | {scenario} | Valider | {comment}\n")
        st.success("✅ Validation en lot enregistrée.")
