# Gradient Descent for minimizing L(w) = (w - 3)^2

w = 0.0                 # initial value
lr = 0.1                # learning rate

for i in range(20):
    grad = 2 * (w - 3)  # derivative of loss
    w = w - lr * grad  # update rule

print("Gradient Descent solution:", w)

# Random Search for minimizing L(w) = (w - 3)^2

import random

best_w = random.uniform(-10, 10)
best_loss = (best_w - 3) ** 2

for i in range(100):
    w = random.uniform(-10, 10)      # random candidate
    loss = (w - 3) ** 2

    if loss < best_loss:
        best_w = w
        best_loss = loss

print("Random Search solution:", best_w)
