from .config import TARGET_COLUMN
from .data.load_features import load_gam_features
from .evaluation.metrics import evaluate_model
from .evaluation.plots import plot_partial_dependence
from .features.build_matrix import build_design_matrix
from .features.schema import FeatureSpec, FeatureType
from .models.gam import fit_gam

# 1 Load data
df = load_gam_features()

# 2 Define feature specs
feature_specs = [
    FeatureSpec(name="district_code", type=FeatureType.CATEGORICAL),
    FeatureSpec(name="age_category", type=FeatureType.CATEGORICAL),
    FeatureSpec(name="size_band", type=FeatureType.CATEGORICAL),
    FeatureSpec(name="has_external", type=FeatureType.CATEGORICAL),
    FeatureSpec(name="year", type=FeatureType.CATEGORICAL), 
]

# 3 Build design matrix
X, encoders = build_design_matrix(df, feature_specs)
y = df[TARGET_COLUMN].to_numpy()

# 4 Fit GAM
gam = fit_gam(X, y)

# 5 Print summary
print(gam.summary())

# 6 Evaluate metrics
metrics = evaluate_model(gam, X, y)
print(f"R²: {metrics['r2']}, RMSE: {metrics['rmse']:.2f}")

# 7 Plot partial dependence
plot_partial_dependence(gam, X, feature_specs=feature_specs)
