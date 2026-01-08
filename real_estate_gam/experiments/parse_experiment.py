from ..features.schema import FeatureSpec, FeatureType


def build_feature_specs(feature_configs: list[dict]) -> list[FeatureSpec]:
    specs = []
    for f in feature_configs:
        specs.append(
            FeatureSpec(
                name=f["name"],
                type=FeatureType(f["type"]),
                gam_term=f.get("gam_term"),
                lam=f.get("lam"),
                bins=f.get("bins"),
            )
        )
    return specs
