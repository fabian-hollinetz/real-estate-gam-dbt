from pathlib import Path

import yaml


def load_experiment(path: Path) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)
