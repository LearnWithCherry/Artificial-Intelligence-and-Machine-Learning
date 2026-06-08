# !pip install scikit-optimize
import numpy as np
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from scipy.optimize import differential_evolution
from skopt import BayesSearchCV

# Synthetic dataset (500 samples, 10 features, 5 informative)
X, y = make_classification(n_samples=500, n_features=10, n_informative=5,
                           n_redundant=2, random_state=42)
X = StandardScaler().fit_transform(X)

# Parameter bounds (log10 space)
bounds = [(-2, 2), (-4, 0)]  # log10(C), log10(gamma)

def objective(params):
    C, gamma = 10**params[0], 10**params[1]
    return -cross_val_score(SVC(C=C, gamma=gamma, random_state=0),
                           X, y, cv=3, scoring='accuracy').mean()

# 1. Grid Search
print("Grid Search...")
grid = GridSearchCV(SVC(random_state=0),
                    {'C': np.logspace(-2,2,5), 'gamma': np.logspace(-4,0,5)}, cv=3)
grid.fit(X, y)
print(f"  Best: {grid.best_score_:.4f} with {grid.best_params_}")

# 2. Random Search
print("\nRandom Search...")
rand = RandomizedSearchCV(SVC(random_state=0),
                          {'C': np.logspace(-2,2), 'gamma': np.logspace(-4,0)},
                          n_iter=25, cv=3, random_state=0)
rand.fit(X, y)
print(f"  Best: {rand.best_score_:.4f} with {rand.best_params_}")

# 3. Evolutionary (Differential Evolution)
print("\nEvolutionary Search...")
res = differential_evolution(objective, bounds, maxiter=10, popsize=10, seed=0)
C_evo, gamma_evo = 10**res.x[0], 10**res.x[1]
print(f"  Best: {-res.fun:.4f} with C={C_evo:.3f}, gamma={gamma_evo:.4f}")

# 4. Bayesian Optimization
print("\nBayesian Optimization...")
bayes = BayesSearchCV(SVC(random_state=0),
                      {'C': (1e-2, 1e2, 'log-uniform'),
                       'gamma': (1e-4, 1, 'log-uniform')},
                      n_iter=25, cv=3, random_state=0)
bayes.fit(X, y)
print(f"  Best: {bayes.best_score_:.4f} with {bayes.best_params_}")
