from pathlib import Path
from typing import cast

import pandas as pd

from ..config import (DERIVED_COLUMNS, FEATURE_COLUMNS, OUT_DIR,
                      RENAME_COLUMNS, TARGET_COLUMN, TYPE_CASTS)


def load_gam_features(snapshot_year: int | None = None) -> pd.DataFrame:
    if snapshot_year is None:
        path = OUT_DIR / "flats.parquet"
    else:
        path = OUT_DIR / f"flats_{snapshot_year}.parquet"

    df = pd.read_parquet(path)

    # apply logical schema
    df = df.rename(columns=RENAME_COLUMNS)

    for col, rule in DERIVED_COLUMNS.items():
        if rule["transform"] == "year":
            df[col] = pd.to_datetime(df[rule["source"]]).dt.year

    for col, dtype in TYPE_CASTS.items():
        df[col] = df[col].astype(dtype)

    selected_cols: list[str] = FEATURE_COLUMNS + [TARGET_COLUMN]
    return cast(pd.DataFrame, df[selected_cols])

