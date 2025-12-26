import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from .schema import FeatureSpec, FeatureType


def build_design_matrix(df: pd.DataFrame, feature_specs: list[FeatureSpec]):
    """
    Returns:
        X: np.ndarray, numeric design matrix
        encoders: dict, LabelEncoders for categorical columns
    """
    X_parts = []
    encoders = {}

    for spec in feature_specs:
        if spec.type == FeatureType.CATEGORICAL:
            le = LabelEncoder()
            col_data = le.fit_transform(df[spec.name]).reshape(-1, 1)
            X_parts.append(col_data)
            encoders[spec.name] = le

        elif spec.type == FeatureType.BINNED:
            if spec.bins is None:
                raise ValueError(f"Bins must be defined for {spec.name}")
            col_data = pd.cut(df[spec.name], bins=spec.bins, labels=False).to_numpy().reshape(-1, 1)
            X_parts.append(col_data)

        else:  # continuous
            col_data = df[spec.name].astype(float).to_numpy().reshape(-1, 1)
            X_parts.append(col_data)

    X = np.hstack(X_parts)
    return X, encoders
