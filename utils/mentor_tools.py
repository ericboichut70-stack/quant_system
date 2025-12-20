## 🧑‍🏫 Interface mentor-élève
if st.button("📨 Envoyer au mentor"):
    save_mentor_comment(selected_signal["timestamp"], mentor_comment)
    st.success("✅ Signal envoyé au mentor. En attente de retour.")

# 🔧 Module de validation mentorale
def validate_signal(signal_id, decision, comment):
    with open("utils/mentor_validation.txt", "a", encoding="utf-8") as f:
        f.write(f"{signal_id} | {decision} | {comment}\n")

# 🧑‍🏫 2. Interface mentorale multi-utilisateur
def save_mentor_feedback(user_id, signal_id, mentor_name, decision, comment):
    with open("utils/mentor_feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"{user_id} | {signal_id} | {mentor_name} | {decision} | {comment}\n")
