import numpy as np

# Create array
a = np.array([1, 2, 3, 4, 5])

# 2D array
b = np.array([[1, 2], [3, 4]])
# Basic operations
print(a + 10)
print(a * 2)
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.sum(a))

# Range
x = np.arange(0, 10, 2)
print(x)   # [0 2 4 6 8]

# Zeros and ones
print(np.zeros(5))
print(np.ones(5))

# Random numbers
print(np.random.rand(3))

# Array shape
print(b.shape)

# Reshape
c = np.arange(6).reshape(2, 3)
print(c)
