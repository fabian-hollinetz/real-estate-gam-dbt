# tests/test_load_features.py
import pandas as pd
import pytest
from src.data.load_features import load_gam_features

def test_load_gam_features_columns():
    """
    Test that the GAM features loader returns a DataFrame
    with the expected columns.
    """
    df = load_gam_features()
    expected_columns = [
        "district_code",
        "age_category",
        "size_band",
        "has_external",
        "year",
        "price"
    ]
    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"

def test_load_gam_features_not_empty():
    """
    Test that the loaded GAM features DataFrame is not empty.
    """
    df = load_gam_features()
    assert len(df) > 0, "GAM features DataFrame is empty"

def test_load_gam_features_no_nulls():
    """
    Check that critical columns do not have missing values.
    """
    df = load_gam_features()
    critical_cols = [
        "district_code",
        "age_category",
        "size_band",
        "has_external",
        "year",
        "price"
    ]
    for col in critical_cols:
        assert df[col].notna().all(), f"Column {col} contains NaNs"

