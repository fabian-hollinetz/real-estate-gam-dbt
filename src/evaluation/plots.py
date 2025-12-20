import matplotlib.pyplot as plt

def plot_partial_dependence(gam, X):
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
        plt.title(f"Effect of {X.columns[i]}")
        plt.xlabel(X.columns[i])
        plt.ylabel("Price effect")
        plt.show()
