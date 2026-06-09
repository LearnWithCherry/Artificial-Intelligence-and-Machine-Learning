# Import libraries
import numpy as np
from sklearn import svm

# Create slightly overlapping dataset
X = np.array([[1,2], [2,3], [3,3], [2,1], [3,2]])
y = np.array([1, 1, -1, -1, -1])

# Train Soft Margin SVM (smaller C allows misclassification)
model = svm.SVC(kernel='linear', C=0.5)
model.fit(X, y)

# Print support vectors
print("Support Vectors:\n", model.support_vectors_)

# Predict a new point
prediction = model.predict([[2.5, 2]])
print("Prediction for [2.5, 2]:", prediction)
