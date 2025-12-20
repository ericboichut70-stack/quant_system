# Script principal de test
# 🧪 Lancement des tests modulaires
# Ce script permet de tester un module donné avec un scénario simulé, en activant scoring, logs et replay selon les flags.
# run_test.py
import argparse
from config_loader import load_all_configs

def run_core_analysis_test(configs):
    print("🧪 Test du module core_analysis")
    # Simulation d’un signal
    signal = {
        "asset": "EURUSD",
        "structure": "breaker + imbalance",
        "timeframe": "M15",
        "confidence": 0.82
    }
    print(f"Signal détecté : {signal}")
    
    if configs["flags"]["scoring_enabled"]:
        score = round(signal["confidence"] * 100)
        print(f"Score du signal : {score}/100")

    if configs["flags"]["replay_enabled"]:
        replay = f"[REPLAY] {signal['asset']} | {signal['structure']} | {signal['timeframe']} | {score}/100"
        with open("replays/core_analysis_replay.txt", "w") as f:
            f.write(replay)
        print("Replay généré.")

    if configs["flags"]["export_format"] == "csv":
        with open("exports/core_analysis_export.csv", "w") as f:
            f.write("asset,structure,timeframe,confidence,score\n")
            f.write(f"{signal['asset']},{signal['structure']},{signal['timeframe']},{signal['confidence']},{score}\n")
        print("Export CSV généré.")

# 🧪 Fonction test du module interface_pilotage
def run_interface_pilotage_test(configs):
    print("🧪 Test du module interface_pilotage")

    signal = {
        "asset": "EURUSD",
        "structure": "breaker + imbalance",
        "confidence": 0.84,
        "entry": 1.0650,
        "tp": 1.0680,
        "sl": 1.0620
    }

    score = round(signal["confidence"] * 100)

    print(f"📡 Signal : {signal['asset']} | {signal['structure']} | Confiance : {score}/100")
    print(f"🎯 Entrée : {signal['entry']} | TP : {signal['tp']} | SL : {signal['sl']}")

    # Export CSV
    if configs["flags"]["export_format"] == "csv":
        with open("exports/interface_pilotage_export.csv", "w") as f:
            f.write("asset,structure,confidence,entry,tp,sl,score\n")
            f.write(f"{signal['asset']},{signal['structure']},{signal['confidence']},{signal['entry']},{signal['tp']},{signal['sl']},{score}\n")
        print("Export CSV généré.")

    # Replay
    if configs["flags"]["replay_enabled"]:
        replay = f"[REPLAY] {signal['asset']} | Entrée: {signal['entry']} | TP: {signal['tp']} | SL: {signal['sl']} | Score: {score}/100"
        with open("replays/interface_pilotage_replay.txt", "w") as f:
            f.write(replay)
        print("Replay généré.")

    # Log global
    log_global_test("interface_pilotage", signal["asset"], "signal", score, 0, True, True)

    # Validation
    validate_score("interface_pilotage", score, configs)

    # Feedback utilisateur
    from utils.feedback import save_feedback
    save_feedback("interface_pilotage", score, "TP bien placé, SL serré")

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# 🧪 Bloc execution_engine    
import argparse
from config_loader import load_all_configs

def main():
    parser = argparse.ArgumentParser(description="Lance un test modulaire")
    parser.add_argument("--module", type=str, required=True, help="Nom du module à tester")
    args = parser.parse_args()

    configs = load_all_configs()
    module = args.module

    if module == "core_analysis":
        run_core_analysis_test(configs)
    elif module == "execution_engine":
        run_execution_engine_test(configs)
    elif module == "propfirm_guard":
        run_propfirm_guard_test(configs)
    elif module == "pedagogical_output":
        run_pedagogical_output_test(configs)
    elif module == "memory_local":
        run_memory_local_test(configs)
    elif module == "interface_pilotage":
        run_interface_pilotage_test(configs)
    else:
        print(f"Module {module} non pris en charge.")

if __name__ == "__main__":
    main()

# 🧪 Test
elif module == "memory_local":
    run_memory_local_test(configs)    

# ✅ Fonction de validation automatique selon validation_threshold
def validate_score(module, score, configs):
    rules = load_config("scoring_rules.yaml")
    threshold = rules[module]["validation_threshold"]
    if score >= threshold:
        print(f"✅ Score validé ({score} ≥ {threshold})")
        return True
    else:
        print(f"❌ Score insuffisant ({score} < {threshold})")
        return False

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# ✅ Appel fonction de validation automatique
valid = validate_score("execution_engine", score, configs)

def main():
    parser = argparse.ArgumentParser(description="Lance un test modulaire")
    parser.add_argument("--module", type=str, required=True, help="Nom du module à tester")
    args = parser.parse_args()

    configs = load_all_configs()
    module = args.module

    if module == "core_analysis":
        run_core_analysis_test(configs)
    else:
        print(f"Module {module} non pris en charge.")

if __name__ == "__main__":
    main()

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# ✅ Appel fonction de validation automatique
valid = validate_score("execution_engine", score, configs)

# 🧪 Test du bloc execution_engine
# Ce test simule une prise de position sur un signal donné, avec sizing, TP/SL, et scoring de rigueur.
def run_execution_engine_test(configs):
    print("🧪 Test du module execution_engine")
    # Signal simulé
    signal = {
        "asset": "EURUSD",
        "confidence": 0.82,
        "risk_reward": 2.0,
        "volatility": 1.3
    }

    # Sizing simulé
    max_size = configs["limits"]["max_position_size"]
    size = round(min(signal["confidence"] * signal["risk_reward"], max_size), 2)
    print(f"Position simulée : {signal['asset']} | Taille : {size}")

    # TP/SL simulés
    tp = round(size * signal["risk_reward"], 2)
    sl = round(size / signal["risk_reward"], 2)
    print(f"TP : {tp} | SL : {sl}")

    # Scoring
    if configs["flags"]["scoring_enabled"]:
        score = round((signal["confidence"] + signal["risk_reward"]) * 10)
        print(f"Score de rigueur : {score}/100")

    # Replay
    if configs["flags"]["replay_enabled"]:
        replay = f"[REPLAY] {signal['asset']} | Size: {size} | TP: {tp} | SL: {sl} | Score: {score}/100"
        with open("replays/execution_engine_replay.txt", "w") as f:
            f.write(replay)
        print("Replay généré.")

    # Export CSV
    if configs["flags"]["export_format"] == "csv":
        with open("exports/execution_engine_export.csv", "w") as f:
            f.write("asset,size,tp,sl,confidence,risk_reward,score\n")
            f.write(f"{signal['asset']},{size},{tp},{sl},{signal['confidence']},{signal['risk_reward']},{score}\n")
        print("Export CSV généré.")

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# ✅ Appel fonction de validation automatique
valid = validate_score("execution_engine", score, configs)

# 🧪 Test du bloc propfirm_guard
# Ce test simule une session avec dépassement de règles propfirm.
def run_propfirm_guard_test(configs):
    print("🧪 Test du module propfirm_guard")
    # Session simulée
    session = {
        "daily_loss": -5.5,
        "max_size": 2.5,
        "open_trades": 4
    }

    limits = configs["limits"]
    violations = []

    if session["daily_loss"] < limits["max_daily_loss"]:
        violations.append("Dépassement du drawdown journalier")

    if session["max_size"] > limits["max_position_size"]:
        violations.append("Taille de position excessive")

    if session["open_trades"] > limits["max_open_trades"]:
        violations.append("Trop de positions ouvertes")

    if violations:
        print("🚨 Violations détectées :")
        for v in violations:
            print(f" - {v}")
    else:
        print("✅ Aucune violation détectée.")

    # Scoring
    if configs["flags"]["scoring_enabled"]:
        score = 100 - len(violations) * 30
        score = max(score, 0)
        print(f"Score de conformité : {score}/100")

    # Replay
    if configs["flags"]["replay_enabled"]:
        replay = f"[REPLAY] Violations : {len(violations)} | Score : {score}/100"
        with open("replays/propfirm_guard_replay.txt", "w") as f:
            f.write(replay)
        print("Replay généré.")

    # Export
    if configs["flags"]["export_format"] == "csv":
        with open("exports/propfirm_guard_export.csv", "w") as f:
            f.write("daily_loss,max_size,open_trades,violations,score\n")
            f.write(f"{session['daily_loss']},{session['max_size']},{session['open_trades']},{len(violations)},{score}\n")
        print("Export CSV généré.")

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# ✅ Appel fonction de validation automatique
valid = validate_score("execution_engine", score, configs)

# 🧪 6. Génération du test du bloc pedagogical_output
# Ce test vérifie la clarté, la structure, et la lisibilité du message pédagogique.
def run_pedagogical_output_test(configs):
    print("🧪 Test du module pedagogical_output")
    # Message simulé
    message = {
        "intention": "Entrer sur EURUSD M15",
        "justification": "Breaker + imbalance + sweep",
        "cible": "Zone de liquidité haute",
        "score_lisibilite": 88
    }

    print(f"📢 Message pédagogique : {message}")

    # Export
    if configs["flags"]["export_format"] == "csv":
        with open("exports/pedagogical_output_export.csv", "w") as f:
            f.write("intention,justification,cible,score_lisibilite\n")
            f.write(f"{message['intention']},{message['justification']},{message['cible']},{message['score_lisibilite']}\n")
        print("Export CSV généré.")

    # Replay
    if configs["flags"]["replay_enabled"]:
        replay = f"[REPLAY] {message['intention']} | {message['justification']} | {message['cible']} | Score: {message['score_lisibilite']}/100"
        with open("replays/pedagogical_output_replay.txt", "w") as f:
            f.write(replay)
        print("Replay généré.")

    # Log global
    log_global_test("pedagogical_output", "EURUSD", "message", message["score_lisibilite"], 0, True, True)

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# ✅ Appel fonction de validation automatique
valid = validate_score("execution_engine", score, configs)

# 🧪 Test
def run_memory_local_test(configs):
    print("🧪 Test du module memory_local")

    # Historique simulé
    history = [
        {"asset": "EURUSD", "entry": 1.0650, "exit": 1.0680, "result": "TP", "error": None},
        {"asset": "GBPUSD", "entry": 1.2150, "exit": 1.2100, "result": "SL", "error": "Invalidation non détectée"},
        {"asset": "USDJPY", "entry": 149.80, "exit": 149.90, "result": "BE", "error": None}
    ]

    # Affichage
    for trade in history:
        print(f"{trade['asset']} | Entrée: {trade['entry']} | Sortie: {trade['exit']} | Résultat: {trade['result']}")

    # Export JSON
    if configs["flags"]["export_format"] == "json":
        import json
        with open("exports/memory_local_export.json", "w") as f:
            json.dump(history, f, indent=2)
        print("Export JSON généré.")

    # Replay TXT
    if configs["flags"]["replay_enabled"]:
        with open("replays/memory_local_replay.txt", "w") as f:
            for trade in history:
                line = f"{trade['asset']} | {trade['result']} | Erreur: {trade['error'] or 'Aucune'}\n"
                f.write(line)
        print("Replay généré.")

    # Log global
    log_global_test("memory_local", "multi", "historique", 100, 0, True, True)
 
# 📄 Enrichissement pédagogique du replay avec corrections
corrections = {
    "Invalidation non détectée": "Ajouter une alerte sur structure cassée + confirmation temporelle",
    "SL trop proche": "Revoir le ratio RR minimum dans limits.yaml",
    "Entrée trop tardive": "Activer le filtre de timing dans signal_filter.py"
}

with open("replays/memory_local_replay.txt", "w") as f:
    for trade in history:
        error = trade["error"]
        correction = corrections.get(error, "Aucune correction nécessaire") if error else "Aucune"
        line = f"{trade['asset']} | {trade['result']} | Erreur: {error or 'Aucune'} | Correction: {correction}\n"
        f.write(line)

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# 🧪 Génération du test interface_pilotage
def run_interface_pilotage_test(configs):
    print("🧪 Test du module interface_pilotage")

    # Signal simulé
    signal = {
        "asset": "EURUSD",
        "structure": "breaker + imbalance",
        "confidence": 0.82,
        "entry": 1.0650,
        "tp": 1.0680,
        "sl": 1.0620
    }

    print(f"📡 Signal : {signal['asset']} | {signal['structure']} | Confiance : {int(signal['confidence']*100)}%")
    print(f"🎯 Entrée : {signal['entry']} | TP : {signal['tp']} | SL : {signal['sl']}")

    # Export CSV
    if configs["flags"]["export_format"] == "csv":
        with open("exports/interface_pilotage_export.csv", "w") as f:
            f.write("asset,structure,confidence,entry,tp,sl\n")
            f.write(f"{signal['asset']},{signal['structure']},{signal['confidence']},{signal['entry']},{signal['tp']},{signal['sl']}\n")
        print("Export CSV généré.")

    # Replay
    if configs["flags"]["replay_enabled"]:
        replay = f"[REPLAY] {signal['asset']} | Entrée: {signal['entry']} | TP: {signal['tp']} | SL: {signal['sl']} | Confiance: {int(signal['confidence']*100)}%"
        with open("replays/interface_pilotage_replay.txt", "w") as f:
            f.write(replay)
        print("Replay généré.")

    # Log global
    log_global_test("interface_pilotage", signal["asset"], "signal", int(signal["confidence"]*100), 0, True, True)

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

# 🧪 3. Lancement du test
def run_interface_pilotage_test(configs):
    print("🧪 Test du module interface_pilotage")

    signal = {
        "asset": "EURUSD",
        "structure": "breaker + imbalance",
        "confidence": 0.84,
        "entry": 1.0650,
        "tp": 1.0680,
        "sl": 1.0620
    }

    print(f"📡 Signal : {signal['asset']} | {signal['structure']} | Confiance : {int(signal['confidence']*100)}%")
    print(f"🎯 Entrée : {signal['entry']} | TP : {signal['tp']} | SL : {signal['sl']}")

    score = round(signal["confidence"] * 100)

    # Export CSV
    if configs["flags"]["export_format"] == "csv":
        with open("exports/interface_pilotage_export.csv", "w") as f:
            f.write("asset,structure,confidence,entry,tp,sl,score\n")
            f.write(f"{signal['asset']},{signal['structure']},{signal['confidence']},{signal['entry']},{signal['tp']},{signal['sl']},{score}\n")
        print("Export CSV généré.")

    # Replay
    if configs["flags"]["replay_enabled"]:
        replay = f"[REPLAY] {signal['asset']} | Entrée: {signal['entry']} | TP: {signal['tp']} | SL: {signal['sl']} | Score: {score}/100"
        with open("replays/interface_pilotage_replay.txt", "w") as f:
            f.write(replay)
        print("Replay généré.")

    # Log global
    log_global_test("interface_pilotage", signal["asset"], "signal", score, 0, True, True)

    # Validation
    validate_score("interface_pilotage", score, configs)

    # Feedback utilisateur
    save_feedback("interface_pilotage", score, "TP bien placé, SL serré")

# 📦 Automatisation de global_test_log.csv
# Script à ajouter à la fin de chaque test
import csv
from datetime import datetime

def log_global_test(module, asset, action, score, violations, export, replay):
    path = "exports/global_test_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [timestamp, module, asset, action, score, violations, export, replay]
    header = ["timestamp", "module", "asset", "action", "score", "violations", "export", "replay"]

    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)
