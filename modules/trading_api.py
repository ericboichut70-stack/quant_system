# modules/trading_api.py

import time
import random
import pandas as pd

def place_order(symbol: str, direction: str, size: float, price: float) -> dict:
    """
    Simule le placement d'un ordre auprès d'une API de trading.

    Paramètres :
    - symbol : instrument (ex. 'BTCUSD')
    - direction : 'Buy' ou 'Sell'
    - size : taille de la position
    - price : prix d'exécution demandé

    Retour :
    - Dictionnaire contenant :
      * 'order_id'
      * 'symbol'
      * 'direction'
      * 'size'
      * 'price'
      * 'timestamp'
    """
    order_id = f"ORD-{int(time.time())}-{random.randint(1000,9999)}"
    return {
        "order_id": order_id,
        "symbol": symbol,
        "direction": direction,
        "size": size,
        "price": price,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }


def fetch_positions() -> pd.DataFrame:
    """
    Simule la récupération des positions ouvertes.

    Retour :
    - DataFrame contenant :
      * 'symbol'
      * 'direction'
      * 'size'
      * 'entry_price'
    """
    data = [
        {"symbol": "BTCUSD", "direction": "Buy", "size": 0.5, "entry_price": 42000},
        {"symbol": "ETHUSD", "direction": "Sell", "size": 1.2, "entry_price": 2300},
    ]
    return pd.DataFrame(data)


def close_position(symbol: str) -> dict:
    """
    Simule la fermeture d'une position.

    Paramètres :
    - symbol : instrument à clôturer

    Retour :
    - Dictionnaire contenant :
      * 'symbol'
      * 'closed_at'
      * 'pnl'
    """
    pnl = round(random.uniform(-50, 150), 2)
    return {
        "symbol": symbol,
        "closed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "pnl": pnl
    }
