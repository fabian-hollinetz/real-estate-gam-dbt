import matplotlib.pyplot as plt


def plot_partial_dependence(gam, X, feature_specs=None):
    """
    Plots the partial dependence of each feature in the GAM.
    """
    for i, term in enumerate(gam.terms):
        if term.isintercept:
            continue

        XX = gam.generate_X_grid(term=i)
        plt.figure()
        plt.plot(XX[:, i], gam.partial_dependence(term=i, X=XX))
        plt.fill_between(
            XX[:, i],
            gam.partial_dependence(term=i, X=XX, width=0.95)[1][:, 0],
            gam.partial_dependence(term=i, X=XX, width=0.95)[1][:, 1],
            alpha=0.2
        )
        if feature_specs is not None:
            feat_name = feature_specs[i].name
        else:
            feat_name = f"feature_{i}"

        plt.title(f"Effect of {feat_name}")
        plt.xlabel(feat_name)
        plt.ylabel("Price effect")
        plt.show()
