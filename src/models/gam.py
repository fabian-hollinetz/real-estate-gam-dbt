from pygam import LinearGAM, f, s

from ..features.schema import FeatureSpec


def build_gam(feature_specs: list[FeatureSpec]):
    """
    Build LinearGAM dynamically from FeatureSpec list.
    Categorical features become f(), smooth features become s().
    """
    terms = []
    for i, spec in enumerate(feature_specs):
        if spec.gam_term == "factor":
            terms.append(f(i))
        else:
            lam = spec.lam if spec.lam is not None else 0.6
            terms.append(s(i, lam=lam))
    
    gam = LinearGAM(sum(terms))
    return gam

def fit_gam(X, y, feature_specs=None):
    """
    Fit GAM to X, y. Optionally pass FeatureSpec to build terms.
    """
    if feature_specs is not None:
        gam = build_gam(feature_specs)
    else:
        gam = LinearGAM()  # fallback
    gam.fit(X, y)
    return gam
