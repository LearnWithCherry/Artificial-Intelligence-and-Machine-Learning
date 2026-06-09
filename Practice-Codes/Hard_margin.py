import numpy as np   #used for numerical array and matrix operations
import matplotlib.pyplot as plt #used for ploting graph
from sklearn import svm #import svm model

X = np.array([[1,4], [2,5], [4,1], [5,2]])   #input features (2d points)
y = np.array([1, 1, -1, -1]) #class labels(+1,-1)

model = svm.SVC(kernel='linear', C=1e6)
#linear - straight decision boundary
model.fit(X, y)
#trains the model
#finds optimal hyperplane + Support vectors

plt.scatter(X[:,0], X[:,1], c=y)

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)

xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = model.decision_function(xy).reshape(XX.shape)

ax.contour(XX, YY, Z, levels=[0])
plt.show()
