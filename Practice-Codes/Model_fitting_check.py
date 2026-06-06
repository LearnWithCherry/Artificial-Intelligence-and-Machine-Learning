# Demonstration of:
# 1. Underfitting
# 2. Good Fit
# 3. Overfitting
# 4. L1 Regularization (Lasso)
# 5. L2 Regularization (Ridge)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# --------------------------------------------------
# USER-DEFINED DATASET
# --------------------------------------------------

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

y = np.array([
    3,
    5,
    7,
    6,
    8,
    12,
    18,
    20,
    25,
    30
])

# Smooth values for plotting
X_test = np.linspace(1, 10, 200).reshape(-1, 1)

# --------------------------------------------------
# MODELS
# --------------------------------------------------

# Underfitting Model
underfit_model = make_pipeline(
    PolynomialFeatures(degree=1),
    LinearRegression()
)

# Good Fit Model
goodfit_model = make_pipeline(
    PolynomialFeatures(degree=3),
    LinearRegression()
)

# Overfitting Model
overfit_model = make_pipeline(
    PolynomialFeatures(degree=9),
    LinearRegression()
)

# L1 Regularization (Lasso)
lasso_model = make_pipeline(
    PolynomialFeatures(degree=9),
    Lasso(alpha=0.1, max_iter=10000)
)

# L2 Regularization (Ridge)
ridge_model = make_pipeline(
    PolynomialFeatures(degree=9),
    Ridge(alpha=1.0)
)

models = {
    "Underfitting": underfit_model,
    "Good Fit": goodfit_model,
    "Overfitting": overfit_model,
    "L1 Regularization (Lasso)": lasso_model,
    "L2 Regularization (Ridge)": ridge_model
}

# --------------------------------------------------
# PLOTTING
# --------------------------------------------------

plt.figure(figsize=(15, 10))

for i, (title, model) in enumerate(models.items(), 1):

    # Train
    model.fit(X, y)

    # Predict
    y_pred = model.predict(X_test)

    # Training prediction
    train_pred = model.predict(X)

    # Error
    mse = mean_squared_error(y, train_pred)

    # Plot
    plt.subplot(3, 2, i)

    plt.scatter(X, y, color='blue', label='Data Points')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Model Curve')

    plt.title(f"{title}\nMSE = {mse:.2f}")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.legend()

plt.tight_layout()
plt.show()

