import pandas as pd
from .config import get_engine

def load_gam_features():
    """
    Loads GAM feature table from Postgres via dbt output.
    Returns a pandas DataFrame.
    """
    query = "SELECT * FROM public_features.gam_features"
    df = pd.read_sql(query, get_engine())
    return df
