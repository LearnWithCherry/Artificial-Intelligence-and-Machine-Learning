from sklearn.svm import SVC
from sklearn.datasets import make_circles

X,y=make_circles(n_samples=100,random_state=1,noise=0.05)
linear_svm=SVC(kernel ='linear').fit(X,y)
rbf_svm=SVC(kernel='rbf').fit(X,y)
print("linear accuracy",linear_svm.score(X,y))
print("rbf kernel accuracy",rbf_svm.score(X,y))
