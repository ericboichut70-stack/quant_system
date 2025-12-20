# -*- coding: utf-8 -*-
"""
Module: phoebus_energy

Ce module calcule le Centre de Gravité (COG) de Mostafa Ballistic via
une régression polynomiale d'ordre 2 (approximation courante) sur fenêtre glissante,
ainsi qu'une mesure d'Énergie: (Close - COG) pondérée par le volume signé.

Fonctionnalités principales:
- Chargement des données CSV au format fourni (200 barres M15) avec parsing du volume signé "VOLUME Up/Down".
- Calcul du COG (quadratique) pour des longueurs paramétrables (par défaut [14, 19, 38]).
- Calcul d'une énergie brute et d'une énergie recalibrée via régression linéaire sur la colonne ENERGIE du CSV.
- Comparaison avec deux colonnes de référence fournies: "Gravity Center Open Source Raqiq" et
  "BGC Ninjatrader Calcule a la fermeture de la barre" (RMSE et corrélations).
- Visualisation: histogramme de l'énergie (barres vertes/rouges) avec ligne zéro.

Dépendances: pandas, numpy, matplotlib, scipy (optionnel mais utilisé ici si dispo).
Tous les commentaires et docstrings sont en français comme demandé.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd

try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except Exception:  # pragma: no cover
    SCIPY_AVAILABLE = False

import matplotlib.pyplot as plt


# -----------------------------
# Utilitaires de parsing
# -----------------------------

def parse_time_hhHMM(s: str) -> str:
    """Convertit une heure de forme "20H30" en "20:30".
    Ne gère pas les secondes.
    """
    if pd.isna(s):
        return "00:00"
    s = str(s).strip()
    m = re.match(r"^(\d{1,2})H(\d{2})$", s)
    if not m:
        # si déjà au bon format ou autre
        return s
    hh, mm = m.groups()
    return f"{int(hh):02d}:{int(mm):02d}"


def parse_volume_updown(s: str) -> Tuple[float, int]:
    """Extrait (valeur, signe) depuis une chaîne type "2390 U" ou "1470 D".
    Retourne (volume, sign) où sign est +1 pour 'U' (Up) et -1 pour 'D' (Down).
    Si parsing impossible, retourne (nan, 0).
    """
    if pd.isna(s):
        return (np.nan, 0)
    s = str(s).strip()
    m = re.match(r"^\s*([\d\.]+)\s*([UD])\s*$", s, re.IGNORECASE)
    if m:
        vol = float(m.group(1))
        sign = 1 if m.group(2).upper() == 'U' else -1
        return (vol, sign)
    # fallback: juste un nombre
    try:
        vol = float(s)
        return (vol, 0)
    except Exception:
        return (np.nan, 0)


# -----------------------------
# Calcul COG quadratique
# -----------------------------

def cog_quadratic(close: pd.Series, length: int) -> pd.Series:
    """Calcule le Centre de Gravité par régression polynomiale d'ordre 2 sur une fenêtre glissante.
    Le COG retourné est la valeur ajustée au dernier point de la fenêtre (bar close), en cohérence avec
    "BGC Ninjatrader Calcule a la fermeture de la barre".

    Paramètres
    - close: série des prix de clôture
    - length: taille de la fenêtre (ex: 14, 19, 38)

    Retour
    - pd.Series alignée à close
    """
    n = length
    if n < 3:
        raise ValueError("length doit être >= 3 pour une régression quadratique")

    x_base = np.arange(n)
    # Pré-allocation
    res = np.full(len(close), np.nan, dtype=float)
    values = close.values.astype(float)

    for i in range(n - 1, len(values)):
        y = values[i - n + 1: i + 1]
        # Ajustement poly2 sur indices 0..n-1
        coeffs = np.polyfit(x_base, y, 2)  # renvoie [a2, a1, a0]
        # Valeur ajustée au dernier index (n-1)
        y_hat_last = np.polyval(coeffs, n - 1)
        res[i] = y_hat_last

    return pd.Series(res, index=close.index, name=f"COG_{length}")


# -----------------------------
# Calcul de l'énergie
# -----------------------------

def compute_energy(
    df: pd.DataFrame,
    length: int = 19,
    volume_col: str = "VOLUME Up/Down",
    use_reference_bgc: Optional[str] = None,
    normalize_volume: bool = True,
    epsilon: float = 1e-12,
) -> pd.DataFrame:
    """Calcule l'Énergie = (Close - COG) * Volume_signé (éventuellement normalisé).

    - length: fenêtre du COG quadratique. Options usuelles: 14, 19, 38.
    - use_reference_bgc: si fourni, utilise directement cette colonne pour le COG
      (ex: "BGC Ninjatrader Calcule a la fermeture de la barre") sinon calcule cog_quadratic.
    - normalize_volume: si True, normalise le volume signé par son écart-type (z-score) sur la série entière.

    Retourne un DataFrame avec colonnes: Close, COG, volume, sign, vol_signed, vol_signed_norm,
    energy_raw (sans recalibrage), energy_norm (avec volume normalisé).
    """
    out = df.copy()

    # COG source
    if use_reference_bgc and use_reference_bgc in out.columns:
        cog = out[use_reference_bgc].astype(float).rename(f"COG_ref")
    else:
        cog = cog_quadratic(out["CLOSE"].astype(float), length)
        cog = cog.rename("COG")

    # Volume signé
    parsed = out[volume_col].apply(parse_volume_updown)
    out["VOL_VAL"] = parsed.apply(lambda t: t[0])
    out["VOL_SIGN"] = parsed.apply(lambda t: t[1])
    out["VOL_SIGNED"] = out["VOL_VAL"] * out["VOL_SIGN"]

    # normalisation volume (z-score sur la série non-na)
    if normalize_volume:
        v = out["VOL_SIGNED"].astype(float).values
        v_mean = np.nanmean(v)
        v_std = np.nanstd(v)
        v_std = v_std if v_std > 0 else 1.0
        out["VOL_SIGNED_NORM"] = (out["VOL_SIGNED"] - v_mean) / (v_std + epsilon)
    else:
        out["VOL_SIGNED_NORM"] = out["VOL_SIGNED"]

    # Énergie brute
    out["COG_USED"] = cog
    out["DEV"] = out["CLOSE"].astype(float) - out["COG_USED"].astype(float)
    out["ENERGY_RAW"] = out["DEV"] * out["VOL_SIGNED"]
    out["ENERGY_NORM"] = out["DEV"] * out["VOL_SIGNED_NORM"]

    return out


# -----------------------------
# Étalonnage sur ENERGIE (régression linéaire)
# -----------------------------

def calibrate_energy(
    df: pd.DataFrame,
    target_col: str = "ENERGIE",
    source_col: str = "ENERGY_NORM",
) -> Tuple[pd.Series, Dict[str, float]]:
    """Calibre l'énergie via une régression linéaire: target ≈ a + b * source.
    Retourne (energy_calibrated, metrics).
    """
    x = df[source_col].astype(float)
    y = df[target_col].astype(float)

    mask = x.notna() & y.notna()
    if mask.sum() < 10:
        # pas assez de points
        return (x.copy() * np.nan, {"corr": np.nan, "rmse": np.nan, "a": np.nan, "b": np.nan})

    x_ = x[mask]
    y_ = y[mask]

    # Régression simple (moindres carrés) y = a + b x
    A = np.vstack([np.ones_like(x_), x_]).T
    coeffs, _, _, _ = np.linalg.lstsq(A, y_, rcond=None)
    a, b = float(coeffs[0]), float(coeffs[1])

    y_hat = a + b * x

    # Métriques
    def rmse(a1, a2):
        d = a1 - a2
        return float(np.sqrt(np.nanmean(d * d)))

    corr = float(np.corrcoef(y_[~np.isnan(y_hat[mask])], y_hat[mask][~np.isnan(y_hat[mask])])[0, 1]) if mask.sum() > 1 else np.nan
    metrics = {
        "corr": corr,
        "rmse": rmse(y_, y_hat[mask]),
        "a": a,
        "b": b,
    }
    return (y_hat.rename("ENERGY_CALIB"), metrics)


# -----------------------------
# Comparaison COGs
# -----------------------------

def compare_cogs(df: pd.DataFrame, cog_ours: pd.Series,
                 ref_cols: Iterable[str] = ("Gravity Center Open Source Raqiq",
                                            "BGC Ninjatrader Calcule a la fermeture de la barre")) -> Dict[str, Dict[str, float]]:
    """Calcule RMSE et corrélation entre notre COG et les colonnes de référence.
    Retourne {col: {rmse: float, corr: float}}.
    """
    res: Dict[str, Dict[str, float]] = {}
    y = cog_ours.astype(float)
    for col in ref_cols:
        if col in df.columns:
            x = df[col].astype(float)
            mask = x.notna() & y.notna()
            if mask.sum() >= 5:
                diff = x[mask] - y[mask]
                rmse = float(np.sqrt(np.nanmean(diff * diff)))
                corr = float(np.corrcoef(x[mask], y[mask])[0, 1])
                res[col] = {"rmse": rmse, "corr": corr}
    return res


# -----------------------------
# Optimisation simple
# -----------------------------

def grid_search_energy(
    df: pd.DataFrame,
    lengths: Iterable[int] = (14, 19, 38),
    use_reference_bgc: Optional[str] = None,
) -> Tuple[pd.DataFrame, Dict[str, float]]:
    """Teste plusieurs longueurs et choisit celle qui maximise la corrélation avec la colonne ENERGIE.
    Retourne (df_best, report) où df_best contient ENERGY_CALIB pour la meilleure longueur.
    """
    best = {"corr": -np.inf}
    best_df = None
    for L in lengths:
        cand = compute_energy(df, length=L, use_reference_bgc=use_reference_bgc)
        energy_calib, met = calibrate_energy(cand)
        cand["ENERGY_CALIB"] = energy_calib
        if met["corr"] > best.get("corr", -np.inf):
            best = {"length": L, **met}
            best_df = cand
    if best_df is None:
        best_df = compute_energy(df, length=list(lengths)[0], use_reference_bgc=use_reference_bgc)
        energy_calib, met = calibrate_energy(best_df)
        best_df["ENERGY_CALIB"] = energy_calib
        best = {"length": list(lengths)[0], **met}
    return best_df, best


# -----------------------------
# Visualisation
# -----------------------------

def plot_energy_histogram(df: pd.DataFrame, energy_col: str = "ENERGY_CALIB", title: str = "Énergie du marché") -> None:
    """Trace un histogramme centré autour de zéro (barres verticales colorées par signe)."""
    y = df[energy_col].astype(float)
    idx = np.arange(len(y))
    colors = np.where(y >= 0, "#2ecc71", "#e74c3c")

    plt.figure(figsize=(12, 4))
    plt.bar(idx, y.values, color=colors, width=0.8, align="center")
    plt.axhline(0.0, color="black", linewidth=1.0)
    plt.title(title)
    plt.xlabel("Bar")
    plt.ylabel("Énergie")
    plt.tight_layout()


# -----------------------------
# Chargement CSV fourni
# -----------------------------

def load_provided_csv(path: str) -> pd.DataFrame:
    """Charge le CSV fourni avec les colonnes: BARRE, DATE, HEURE UTC+2, OPEN,HIGH,LOW,CLOSE,
    VOLUME Up/Down, ENERGIE, Gravity Center Open Source Raqiq, BGC Ninjatrader Calcule a la fermeture de la barre, ...
    Ajoute un index datetime combinant DATE + HEURE.
    """
    df = pd.read_csv(path)

    # Harmonisation noms clés (au cas où des espaces parasites existent)
    df.columns = [c.strip() for c in df.columns]

    # Construction datetime
    if "DATE" in df.columns and "HEURE UTC+2" in df.columns:
        times = df["HEURE UTC+2"].map(parse_time_hhHMM)
        dt = pd.to_datetime(df["DATE"].astype(str) + " " + times, dayfirst=True, errors="coerce")
        df.index = dt
        df.index.name = "datetime"

    # Types numériques pour OHLC et références COG
    num_cols = [c for c in ["OPEN", "HIGH", "LOW", "CLOSE",
                            "ENERGIE",
                            "Gravity Center Open Source Raqiq",
                            "BGC Ninjatrader Calcule a la fermeture de la barre"] if c in df.columns]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    return df


# -----------------------------
# Rapport de validation
# -----------------------------

def validation_report(df: pd.DataFrame, length: int = 19, use_reference_bgc: Optional[str] = None) -> Dict[str, Dict[str, float]]:
    """Construit un rapport contenant:
    - métriques d'étalonnage (corrélation vs ENERGIE, RMSE)
    - métriques de comparaison COG vs références
    """
    tmp = compute_energy(df, length=length, use_reference_bgc=use_reference_bgc)
    energy_calib, met = calibrate_energy(tmp)
    tmp["ENERGY_CALIB"] = energy_calib

    # COG ours (si on veut comparer)
    cog = tmp["COG_USED"].astype(float)
    comp = compare_cogs(df, cog)

    report = {
        "energy": met,
        "cogs": comp,
    }
    return report


__all__ = [
    "parse_time_hhHMM",
    "parse_volume_updown",
    "cog_quadratic",
    "compute_energy",
    "calibrate_energy",
    "compare_cogs",
    "grid_search_energy",
    "plot_energy_histogram",
    "load_provided_csv",
    "validation_report",
]
