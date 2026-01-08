from pygam import LinearGAM, f, s

from ..features.schema import FeatureSpec


def build_gam(feature_specs):
    terms = None

    for i, spec in enumerate(feature_specs):
        if spec.gam_term == "factor":
            term = f(i)
        else:
            lam = spec.lam if spec.lam is not None else 0.6
            term = s(i, lam=lam)

        if terms is None:
            terms = term
        else:
            terms += term   # creates / extends a TermList

    return LinearGAM(terms)


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
