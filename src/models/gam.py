from pygam import LinearGAM, s

def build_gam():
    """
    Defines a LinearGAM with one spline per feature.
    Assumes X has 5 columns: living_area, rooms, year, latitude, longitude
    """
    gam = LinearGAM(
        s(0) +  # living_area
        s(1) +  # rooms
        s(2) +  # year
        s(3) +  # latitude
        s(4)    # longitude
    )
    return gam

def fit_gam(X, y):
    """
    Fits the GAM to X and y and returns the fitted model.
    """
    gam = build_gam()
    gam.fit(X, y)
    return gam
