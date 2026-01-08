from pathlib import Path

from .data.load_features import load_gam_features
from .evaluation.metrics import evaluate_model
from .evaluation.plots import plot_partial_dependence
from .experiments.load_experiment import load_experiment
from .experiments.parse_experiment import build_feature_specs
from .features.build_matrix import build_design_matrix
from .models.gam import fit_gam

# Absolute project root for all paths
PROJECT_ROOT = Path(__file__).parent.parent.resolve()


def main(experiment_path: Path | None = None, return_results: bool = False):
    """
    Run GAM experiment.

    Parameters
    ----------
    experiment_path : Path, optional
        Path to the experiment YAML file. If None, defaults to baseline_gam.yaml.
    return_results : bool
        Whether to return model results as a dictionary.

    Returns
    -------
    dict, optional
        Contains 'gam', 'X', 'y', 'feature_names', 'metrics' if return_results=True
    """
    if experiment_path is None:
        experiment_path = PROJECT_ROOT / "experiments" / "baseline_gam.yaml"
    elif not experiment_path.is_absolute():
        # Convert relative paths to absolute, relative to project root
        experiment_path = PROJECT_ROOT / experiment_path

    # --- load experiment ---
    exp = load_experiment(experiment_path)

    # --- data ---
    df = load_gam_features(snapshot_year=exp["data"]["snapshot_year"])
    target = exp["data"]["target"]

    # --- features ---
    feature_specs = build_feature_specs(exp["features"])
    feature_names = [fs.name for fs in feature_specs]

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

    if return_results:
        return {
            "gam": gam,
            "X": X,
            "y": y,
            "feature_names": feature_names,
            "metrics": metrics,
        }
