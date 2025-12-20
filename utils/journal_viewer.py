## 📖 Interface de lecture du journal
st.subheader("📖 Lecture du journal personnel")

if st.button("📂 Ouvrir mon journal"):
    with open("utils/user_journal.txt", "r", encoding="utf-8") as f:
        journal_content = f.read()
    st.text_area("📝 Journal complet", value=journal_content, height=400)

from datetime import datetime
# 📆 Filtre temporel pour le journal personnel
st.subheader("📅 Filtrer le journal par date")

date_filter = st.date_input("📆 Choisir une date", value=datetime.today())
with open("utils/user_journal.txt", "r", encoding="utf-8") as f:
    journal_lines = f.readlines()

filtered = [line for line in journal_lines if str(date_filter) in line]
st.text_area("📝 Journal filtré", value="".join(filtered), height=300)

