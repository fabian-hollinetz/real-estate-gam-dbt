from pathlib import Path

from sqlalchemy import create_engine


# ------------------------
# Postgres DB connection
# ------------------------
def get_engine():
    """
    Returns a SQLAlchemy engine to connect to the Postgres database.
    """
    engine = create_engine("postgresql://dbt_user:dbt123@localhost:5432/realestate")
    return engine


# ------------------------
# Local Statistik Austria Parquet snapshots
# ------------------------
# Path to raw .ods files
RAW_DIR = Path("/mnt/c/data/raw/real_estate_statistik_austria/flats")
# Path to processed Parquet snapshots
OUT_DIR = Path("/mnt/c/data/snapshots/flats")

# --- data schema ---
TARGET_COLUMN = "price"

FEATURE_COLUMNS = [
    "district_code",
    "age_category",
    "size_band",
    "has_external",
    "year",
]

# optional, for later
EXPERIMENT_NAME = "baseline"

# Logical schema mapping (temporary Python version)
RENAME_COLUMNS = {
    "price_per_m2": "price",
}

DERIVED_COLUMNS = {
    "year": {
        "source": "snapshot_date",
        "transform": "year",
    }
}

TYPE_CASTS = {
    "has_external": "int",
}










