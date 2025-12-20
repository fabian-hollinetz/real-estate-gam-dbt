from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate_model(gam, X, y):
    """
    Returns R² and RMSE for the GAM predictions.
    Works with any scikit-learn version.
    """
    y_pred = gam.predict(X)
    r2 = gam.statistics_['pseudo_r2'] if hasattr(gam, 'statistics_') else None

    # RMSE: immer via sqrt(MSE), statt squared=False
    rmse = np.sqrt(mean_squared_error(y, y_pred))

    return {"r2": r2, "rmse": rmse}
