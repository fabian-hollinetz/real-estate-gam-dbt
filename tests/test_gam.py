# tests/test_gam.py
import pytest
from src.models.gam import fit_gam, build_gam
from src.data.load_features import load_gam_features

def test_build_gam_instance():
    """
    Test that build_gam returns a LinearGAM instance.
    """
    gam = build_gam()
    from pygam import LinearGAM
    assert isinstance(gam, LinearGAM), "build_gam() did not return a LinearGAM"

def test_fit_gam_runs():
    """
    Test that fit_gam runs without error on a small sample.
    """
    df = load_gam_features()
    # Use first 3 rows as minimal test data
    df_sample = df.head(3)
    X = df_sample[["living_area", "rooms", "year", "latitude", "longitude"]]
    y = df_sample["price"]
    gam = fit_gam(X, y)
    # Check predictions
    y_pred = gam.predict(X)
    assert len(y_pred) == len(y), "Prediction length mismatch"
