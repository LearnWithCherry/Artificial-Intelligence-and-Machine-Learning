# Import libraries
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate synthetic dataset
X, y = make_classification(n_samples=100, n_features=4, random_state=42)

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train LinearSVC (solves primal problem)
model = LinearSVC()
model.fit(X_train, y_train)

# Print model parameters
print("Weight vector (w):", model.coef_)
print("Bias (b):", model.intercept_)

# Accuracy check
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)
