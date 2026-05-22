x = 2
y = 8
w = 3

# Forward pass: prediction calculation
y_pred = w * x

# Loss calculation (Squared Error)
loss = (y - y_pred) ** 2
print("Loss:", loss)  # Outputs: 4
