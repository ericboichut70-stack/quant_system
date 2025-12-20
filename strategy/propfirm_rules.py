## Chargement des règles ##

def load_rules(propfirm_name):
    path = f"config/propfirms/{propfirm_name}.json"
    with open(path, "r") as f:
        return json.load(f)

## Vérification de compatibilité ##

def check_viability(rules, strategy_profile):
    violations = []
    if strategy_profile["max_drawdown"] > rules["max_drawdown"]:
        violations.append("Drawdown trop élevé")
    if strategy_profile["daily_loss"] > rules["daily_loss_limit"]:
        violations.append("Perte journalière trop élevée")
    if not rules["allow_scalping"] and strategy_profile["uses_scalping"]:
        violations.append("Scalping interdit")
    return violations

## Blocage et alerte ##

def enforce_rules(propfirm_name, strategy_profile):
    rules = load_rules(propfirm_name)
    violations = check_viability(rules, strategy_profile)
    if violations:
        archive_blacklist(propfirm_name, violations)
        raise Exception(f"⛔ Propfirm '{propfirm_name}' non compatible : {violations}")

## Archivage des propfirms non viables ##

def archive_blacklist(name, reasons):
    with open("config/propfirms/blacklist.json", "r+") as f:
        blacklist = json.load(f)
        blacklist[name] = reasons
        f.seek(0)
        json.dump(blacklist, f, indent=4)

## Swing trading autorisé ou non ##
## Si false, le bot doit fermer toutes les positions avant la fin du créneau autorisé ##

"swing_trading_allowed": true

## Horaires de trading autorisés (UTC) ##

"trading_hours_utc" 
{
    "start": "06:00",
    "end": "22:00"
}

## Jours de trading autorisés ##

"allowed_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

## Taille maximale par position ##
## En lots, ou en % du capital ##

"max_position_size": 2.0

## Nombre de positions simultanées ##

"max_open_positions": 5

## Ratio R/R minimum exigé ##

"min_risk_reward_ratio": 1.5

from datetime import datetime, timedelta

def get_closure_deadline(rules):
    end_time = datetime.strptime(rules["trading_hours_utc"]["end"], "%H:%M").time()
    closure_time = (datetime.combine(datetime.utcnow().date(), end_time) - timedelta(minutes=10)).time()
    return closure_time
