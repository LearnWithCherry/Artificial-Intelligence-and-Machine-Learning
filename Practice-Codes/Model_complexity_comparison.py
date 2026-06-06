import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# -----------------------------
# Nonlinear Dataset
# -----------------------------
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])

y = np.array([1, 4, 9, 16, 25, 36, 49, 64])   # y = x^2

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# Simple Linear Model
# -----------------------------
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

train_linear = linear_model.score(X_train, y_train)
test_linear = linear_model.score(X_test, y_test)

# -----------------------------
# Polynomial Model
# -----------------------------
poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

train_poly = poly_model.score(X_train_poly, y_train)
test_poly = poly_model.score(X_test_poly, y_test)

# -----------------------------
# Results
# -----------------------------
print("----- Linear Model -----")
print("Train Score :", train_linear)
print("Test Score  :", test_linear)

print("\n----- Polynomial Model -----")
print("Train Score :", train_poly)
print("Test Score  :", test_poly)

# -----------------------------
# Plot
# -----------------------------
plt.scatter(X, y, color='black')

# Linear fit
plt.plot(X,
         linear_model.predict(X),
         label='Linear Model')

# Polynomial fit
X_range = np.linspace(1,8,100).reshape(-1,1)
X_range_poly = poly.transform(X_range)

plt.plot(X_range,
         poly_model.predict(X_range_poly),
         label='Polynomial Model')

plt.legend()
plt.title("Model Complexity Comparison")
plt.show()
