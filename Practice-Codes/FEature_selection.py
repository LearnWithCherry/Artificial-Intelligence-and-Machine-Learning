#Each chromosome represents a feature subset using binary encoding(1=selected,0=not selected)
#GA searches for features combinations that maximises the classification accuracy
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
pop = np.random.randint(0, 2, (10, X.shape[1]))

def fitness(chrom):
    if chrom.sum() == 0: return 0
    model = LogisticRegression(max_iter=200)
    model.fit(X[:, chrom==1], y)
    return model.score(X[:, chrom==1], y)

for _ in range(20):
    scores = np.array([fitness(c) for c in pop])
    parents = pop[np.argsort(scores)[-5:]]
    children = parents ^ np.random.randint(0,2,parents.shape)
    pop = np.vstack((parents, children))

best = pop[np.argmax([fitness(c) for c in pop])]
print("Selected features:", best)
