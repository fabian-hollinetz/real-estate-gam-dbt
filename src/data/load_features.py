import pandas as pd
from .config import OUT_DIR

def load_gam_features(snapshot_year: int | None = None) -> pd.DataFrame:
    """
    Loads GAM-ready features from Statistik Austria Parquet snapshots.

    Args:
        snapshot_year (int | None): Year of the snapshot to load. If None, loads combined snapshot 'flats.parquet'.

    Returns:
        pd.DataFrame: Prepared DataFrame ready for GAM modeling.
    """
    # Wähle Datei basierend auf Jahr
    if snapshot_year is None:
        path = OUT_DIR / "flats.parquet"
    else:
        path = OUT_DIR / f"flats_{snapshot_year}.parquet"
    
    # Parquet-Datei laden
    df = pd.read_parquet(path)

    # --- Feature Engineering ---
    # Kategorische Variablen
    df["district_code"] = df["district_code"].astype("category")
    df["age_category"] = df["age_category"].astype("category")
    df["size_band"] = df["size_band"].astype("category")
    
    # Boolean -> int
    df["has_external"] = df["has_external"].astype(int)
    
    # Jahr extrahieren
    df["year"] = pd.to_datetime(df["snapshot_date"]).dt.year
    
    # Zielvariable
    df.rename(columns={"price_per_m2": "price"}, inplace=True)
    
    # Nur relevante Spalten zurückgeben
    feature_cols = ["district_code", "age_category", "size_band", "has_external", "year", "price"]
    return df[feature_cols]
