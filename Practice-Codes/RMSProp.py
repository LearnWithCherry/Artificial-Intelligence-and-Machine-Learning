import numpy as np

# Given values (you can change these)
w = 0.5          # initial weight
grad = 0.1       # gradient
lr = 0.01        # learning rate

# Momentum parameters
beta = 0.9
v = 0            # initial velocity

# RMSProp parameters
beta_rms = 0.9
s = 0            # initial squared gradient
epsilon = 1e-8

print("Initial Values:")
print("Weight:", w)
print("Gradient:", grad)
print("-" * 40)

# ---------------------------
# Momentum Update
# ---------------------------
v = beta * v + (1 - beta) * grad
w_momentum = w - lr * v

print("Momentum Update:")
print("Velocity (v):", v)
print("Updated Weight:", w_momentum)
print("-" * 40)

# ---------------------------
# RMSProp Update
# ---------------------------
s = beta_rms * s + (1 - beta_rms) * (grad ** 2)
w_rmsprop = w - (lr / (np.sqrt(s) + epsilon)) * grad

print("RMSProp Update:")
print("Squared Gradient (s):", s)
print("Adjusted Learning Rate:", lr / (np.sqrt(s) + epsilon))
print("Updated Weight:", w_rmsprop)
