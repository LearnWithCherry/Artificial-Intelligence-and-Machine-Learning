import numpy as np


def sphere(x):
    return np.sum(x**2)

def rastrigin(x):
    n = len(x)
    return 10*n + np.sum(x**2 - 10*np.cos(2*np.pi*x))

# Random solution vector (2D)
x = np.array([1.5, -2.0])

# Evaluate functions
print("Input vector:", x)
print("Sphere function value:", sphere(x))
print("Rastrigin function value:", rastrigin(x))
