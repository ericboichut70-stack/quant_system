# 🧩 Logique de pause pédagogique
def toggle_pedagogical_pause(user_name, pause=True, path="utils/pause_log.txt"):
    """
    Active ou désactive une pause pédagogique pour un utilisateur.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        status = "PAUSE" if pause else "ACTIVE"
        f.write(f"{datetime.now()} | {user_name} | {status}\n")
