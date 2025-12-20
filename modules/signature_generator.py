# modules/signature_generator.py

import pandas as pd
import hashlib
import json

def generate_signature(row: dict) -> str:
    """
    Génère une signature unique (hash SHA256) à partir d'un dictionnaire représentant un signal ou un trade.

    Paramètres :
    - row : dictionnaire contenant les champs du signal (timestamp, prix, direction, etc.)

    Retour :
    - Chaîne hexadécimale représentant la signature SHA256
    """
    # On convertit le dictionnaire en JSON stable (tri des clés)
    serialized = json.dumps(row, sort_keys=True)
    signature = hashlib.sha256(serialized.encode()).hexdigest()
    return signature


def add_signatures(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajoute une colonne 'Signature' à un DataFrame de signaux ou trades.

    Paramètres :
    - df : DataFrame contenant les colonnes du signal

    Retour :
    - DataFrame enrichi avec une colonne 'Signature'
    """
    df = df.copy()
    df["Signature"] = df.apply(lambda r: generate_signature(r.to_dict()), axis=1)
    return df
