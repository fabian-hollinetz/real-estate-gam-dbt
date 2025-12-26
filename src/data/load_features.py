# src/data/load_features.py
from pathlib import Path

import pandas as pd

from .config import OUT_DIR


def load_gam_features(snapshot_year: int | None = None) -> pd.DataFrame:
    """
    Loads GAM features from Statistik Austria Parquet snapshots.
    No encoding. No modeling assumptions.
    """
    if snapshot_year is None:
        path = OUT_DIR / "flats.parquet"
    else:
        path = OUT_DIR / f"flats_{snapshot_year}.parquet"

    df = pd.read_parquet(path)

    # minimal, non-controversial cleanup
    df = df.rename(columns={"price_per_m2": "price"})

    df["has_external"] = df["has_external"].astype(int)
    df["year"] = pd.to_datetime(df["snapshot_date"]).dt.year

    feature_cols = [
        "district_code",
        "age_category",
        "size_band",
        "has_external",
        "year",
        "price",
    ]

    return df[feature_cols]
