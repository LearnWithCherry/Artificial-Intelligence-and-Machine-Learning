#import the libraries
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
#create a tiny 2D dataset( 6 points, 2 features)
X=np.array([[1,2],[2,3],[3,3],[6,5],[7,7],[8,6]])
#class 0 :[1,2],[2,3],[3,3]
#class 1 :[6,5],[7,7],[8,6]
y=np.array([0,0,0,1,1,1])
#train a linear SVM with large C (hard margin concept)
svm=SVC(kernel='linear',C=1000)
svm.fit(X,y)
#Extract the value of weight and bias
w = svm.coef_[0]
b = svm.intercept_[0]
print("weight",w)
print("bias",b)
#calculate margin
#margin
margin = 1/np.sqrt(np.sum(w**2))
print("margin",margin)
