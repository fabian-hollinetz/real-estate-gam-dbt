from dataclasses import dataclass
from enum import Enum
from typing import Any, List


class FeatureType(str, Enum):
    CONTINUOUS = "continuous"
    CATEGORICAL = "categorical"
    BINNED = "binned"

@dataclass
class FeatureSpec:
    name: str                   # feature column name
    type: FeatureType           # categorical / continuous / binned
    bins: list | None = None    # optional, for binned variables
    lam: float | None = None    # optional, for GAM term
    gam_term: str | None = None # "factor" or "spline"
