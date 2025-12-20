from .data.load_features import load_gam_features
from .models.gam import fit_gam
from .evaluation.plots import plot_partial_dependence
from .evaluation.metrics import evaluate_model

# 1 Load data
df = load_gam_features()

# 2 Define X and y
X = df[["living_area", "rooms", "year", "latitude", "longitude"]]
y = df["price"]

# 3 Fit GAM
gam = fit_gam(X, y)

# 4 Print summary
print(gam.summary())

# 5 Evaluate metrics
metrics = evaluate_model(gam, X, y)
print(f"R²: {metrics['r2']}, RMSE: {metrics['rmse']:.2f}")

# 6 Plot partial dependence
plot_partial_dependence(gam, X)
