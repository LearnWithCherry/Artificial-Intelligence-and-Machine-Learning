
import numpy as np
y_true = np.array([3, 5, 7, 9, 11])
y_pred = np.array([2.5, 5.5, 6, 9.5, 10])
mse = np.mean((y_true - y_pred) ** 2)
print(f"MSE: {mse:.4f}")  # Output: 0.5500

===================================================

#MSE Gradient Descent with Code
X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 5, 8])
w, b = 0.0, 0.0
lr = 0.01

y_pred = w * X + b
dw = -(2/len(X)) * np.sum(X * (y - y_pred))
db = -(2/len(X)) * np.sum(y - y_pred)
w -= lr * dw
b -= lr * db
print(f"w={w:.4f}, b={b:.4f}")

===================================================

#Sigmoid Function for Logistic Regression
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

print(f"Sigmoid(0) = {sigmoid(0)}")    # 0.5
print(f"Sigmoid(5) = {sigmoid(5):.4f}") # 0.9933

===================================================

#Binary Cross-Entropy
y = np.array([1, 0, 1, 1, 0])
p = np.array([0.9, 0.2, 0.8, 0.3, 0.1])
bce = -np.mean(y * np.log(p) + (1-y) * np.log(1-p))
print(f"Binary Cross-Entropy: {bce:.4f}")  # 0.3720

===================================================

#Sigmoid and Gradient with Code
x = np.array([2, 3])
w = np.array([0.5, -0.2])
b = 0.1
y = 1

z = np.dot(w, x) + b
p = sigmoid(z)
loss = -y * np.log(p)
gradient = (p - y) * x

print(f"p={p:.4f}, loss={loss:.4f}")

===================================================

#Bayesian Linear Regression
from scipy.stats import norm
prior_mean, prior_var = 0, 1
likelihood_var = 1
x, y = 2, 3

post_var = 1/(1/prior_var + x**2/likelihood_var)
post_mean = post_var * (prior_mean/prior_var + x*y/likelihood_var)

print(f"Posterior: N({post_mean:.2f}, {post_var:.2f})")


import numpy as np
X= np.array([1,2])
y= np.array([2,4])
w = 0;b = 0;lr = 0.1
y_pred=w*X+b
dw=-(2/len(X))*np.sum(X*(y-y_pred))
db=-(2/len(X))*np.sum(y-y_pred)

print(dw)
print(db)

import numpy as np
#data true labels and predicted probablities
y_true = np.array([1,0,1])
y_pred = np.array([0.9,0.3,0.8])

# add small epsilon for numerical stability to avoid log(0)
epsilon = 1e-15
y_pred =np.clip(y_pred,epsilon, 1-epsilon)
# compute logistic loss for each sample
losses = -(y_true * np.log(y_pred) + (1-y_true) * np.log(1-y_pred))
# average loss
avg_loss = np.mean(losses)
print("individual losses:",np.round(losses,4))
print("average loss:",np.round(avg_loss,4))


#one sample
import numpy as np
y = 1     #true label
p = 0.8    #predicted Probablity
loss = -(y*np.log(p) + (1-y)*np.log(1-p))
print(loss)

prior_mean = 4
likelihood_mean = 5
#map estimate ( average when variances are equal)
map_estimate = (prior_mean + likelihood_mean)/2
print("map_estimate:",map_estimate)
