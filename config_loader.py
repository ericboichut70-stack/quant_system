
# Chargement dynamique des fichiers .yaml
# 🧰 Loader de configuration pour Private Assistant
# Version: 1.0 | Date: 2025-10-24 | Auteur: Eric
# config_loader.py
import yaml
import os

CONFIG_DIR = "config"

def load_config(file_name):
    path = os.path.join(CONFIG_DIR, file_name)
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_all_configs():
    configs = {}
    for file in ["modules.yaml", "flags.yaml", "paths.yaml", "limits.yaml", "user.yaml"]:
        configs[file.replace(".yaml", "")] = load_config(file)
    return configs

if __name__ == "__main__":
    configs = load_all_configs()
    for name, content in configs.items():
        print(f"\n--- {name.upper()} ---")
        print(content)
