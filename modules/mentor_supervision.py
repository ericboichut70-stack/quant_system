# ✅ Interface mentorale de supervision
import streamlit as st
import pandas as pd

def mentor_supervision_interface(feedback_df, memory_dict, user_list, supervision_log):
    st.subheader("🧑‍🏫 Supervision mentorale")

    selected_user = st.selectbox("👤 Élève à superviser", user_list)
    user_df = feedback_df[feedback_df["user"] == selected_user]

    st.markdown(f"**Total de signaux :** {len(user_df)}")
    st.markdown(f"**Taux de validation :** {round((user_df['decision'] == 'Valider').mean() * 100, 2)}%")

    st.dataframe(user_df[["timestamp", "ScenarioType", "decision", "mentor"]])

    # Commentaire mentoral
    st.subheader("📝 Commentaire mentoral")
    comment = st.text_area("Commentaire pour l’élève", height=100)
    if st.button("📨 Envoyer le commentaire"):
        from datetime import datetime
        with open(supervision_log, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} | {selected_user} | {comment}\n")
        st.success("✅ Commentaire enregistré.")

    # Activation pédagogique
    st.subheader("🎓 Mode pédagogique")
    mode = st.radio("Activer le mode pédagogique ?", ["Oui", "Non"])
    st.markdown(f"🔒 Le bot reste actif en toute circonstance. Le mode pédagogique est une plus-value facultative.")
