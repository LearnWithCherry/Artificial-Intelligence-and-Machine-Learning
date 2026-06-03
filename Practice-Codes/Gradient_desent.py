import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([3, 5, 7, 9, 11])

# Initialize parameters
w, b = 0.0, 0.0
lr = 0.01
epochs = 100

n = len(X)
losses = []

# Gradient Descent
for _ in range(epochs):
    y_pred = w * X + b

    # Loss (MSE)
    loss = np.mean((Y - y_pred) ** 2)
    losses.append(loss)

    # Gradients
    dw = (-2/n) * np.sum(X * (Y - y_pred))
    db = (-2/n) * np.sum(Y - y_pred)

    # Update
    w -= lr * dw
    b -= lr * db

# Final prediction line
y_final = w * X + b

# Plot 1: Data + Regression Line
plt.figure()
plt.scatter(X, Y)
plt.plot(X, y_final)
plt.title("Linear Regression using Gradient Descent")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Plot 2: Loss Curve
plt.figure()
plt.plot(losses)
plt.title("Loss vs Epochs")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()
