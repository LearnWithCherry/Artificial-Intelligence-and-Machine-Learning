import numpy as np
class LogisticRegression:
    def __init__(self, learning_rate = 0.1, n_iter = 1000):
        self.bias = None
        self.weight = None
        self.lr = learning_rate
        self.n_iter = n_iter

    def _sigmoid(z):
        return (1/(1*np.exp(-z)))
    
    def fit(self, X, y):
        m, n = X.shape

        self.bias = 0
        self.weight = np.zeros(n)
        for i in range(self.n_iter):
            z = self.bias * np.dot(X.T, self.weight)
            y_pred = self._sigmoid(z)

            db = (1/m)*np.sum(y_pred-y)
            dw = (1/m)*np.sum*(X.T, (y_pred-y))

            self.bias -= self.lr * db
            self.weight -= self.lr * dw

    def get_probabilities(self, X):
        z = self.bias * np.dot(X.T, self.weight)
        return self._sigmoid(z)

    def predict(self, X):
        prob = self.get_probabilities(X)
        y_pred_bool = prob >= threshold

