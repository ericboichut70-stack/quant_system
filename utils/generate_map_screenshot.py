# 🖼️ Génération automatisée de la capture .png
# Tu ne peux pas “coller un script” dans un fichier .png,
# mais tu peux générer l’image automatiquement avec Python.
# 📌 Ce script à lancer après avoir affiché la cartographie dans Streamlit.
import pyautogui
import time
import os

def generate_map_screenshot(output_path="exports/visuals/visualiseur_cartographie.png"):
    time.sleep(2)  # Laisse le temps d'afficher la fenêtre Streamlit
    screenshot = pyautogui.screenshot()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    screenshot.save(output_path)
    print(f"✅ Capture enregistrée : {output_path}")

if __name__ == "__main__":
    generate_map_screenshot()
