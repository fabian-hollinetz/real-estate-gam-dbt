from pathlib import Path

from .data.load_features import load_gam_features
from .evaluation.metrics import evaluate_model
from .evaluation.plots import plot_partial_dependence
from .experiments.load_experiment import load_experiment
from .experiments.parse_experiment import build_feature_specs
from .features.build_matrix import build_design_matrix
from .models.gam import fit_gam

# --- load experiment ---
experiment_path = Path("experiments/baseline_gam.yaml")
exp = load_experiment(experiment_path)

# --- data ---
df = load_gam_features(snapshot_year=exp["data"]["snapshot_year"])
target = exp["data"]["target"]

# --- features ---
feature_specs = build_feature_specs(exp["features"])
X, encoders = build_design_matrix(df, feature_specs)
y = df[target].to_numpy()

# --- model ---
gam = fit_gam(X, y, feature_specs=feature_specs)
print(gam.summary())

# --- evaluation ---
metrics = evaluate_model(gam, X, y)
print(metrics)

if exp["evaluation"].get("plot_partial_dependence", False):
    plot_partial_dependence(gam, X, feature_specs)
