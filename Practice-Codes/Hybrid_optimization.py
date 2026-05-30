import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

# Load real-world dataset
X, y = load_iris(return_X_y=True)

# Fitness function: maximize cross-validation accuracy
def fitness(params):
    C, gamma = params
    model = SVC(C=C, gamma=gamma)
    score = cross_val_score(model, X, y, cv=3).mean()
    return score

# Hybrid GA-PSO (very short)
def hybrid_optimize():
    # Initial population (positions = [C, gamma])
    n_particles = 5
    pos = np.random.uniform([0.1, 0.01], [10, 1], (n_particles, 2))
    vel = np.random.uniform(-0.5, 0.5, (n_particles, 2))
    pbest = pos.copy()
    pbest_fit = [fitness(p) for p in pbest]
    gbest = pos[np.argmax(pbest_fit)]
    gbest_fit = max(pbest_fit)

    for _ in range(10):  # generations
        # PSO velocity & position update
        w, c1, c2 = 0.7, 1.5, 1.5
        for i in range(n_particles):
            r1, r2 = np.random.rand(2), np.random.rand(2)
            vel[i] = w*vel[i] + c1*r1*(pbest[i]-pos[i]) + c2*r2*(gbest-pos[i])
            pos[i] += vel[i]
            # bounds
            pos[i] = np.clip(pos[i], [0.1,0.01], [10,1])

        # GA step: crossover + mutation on 2 best particles
        fits = [fitness(p) for p in pos]
        idx = np.argsort(fits)[-2:]  # two best indices
        # crossover: average
        child = (pos[idx[0]] + pos[idx[1]]) / 2
        # mutation: small random shift
        child += np.random.uniform(-0.2, 0.2, 2)
        child = np.clip(child, [0.1,0.01], [10,1])
        # replace worst particle with child if better
        worst = np.argmin(fits)
        if fitness(child) > fits[worst]:
            pos[worst] = child

        # update pbest & gbest
        for i in range(n_particles):
            fit_i = fitness(pos[i])
            if fit_i > pbest_fit[i]:
                pbest[i], pbest_fit[i] = pos[i], fit_i
        best_idx = np.argmax(pbest_fit)
        if pbest_fit[best_idx] > gbest_fit:
            gbest, gbest_fit = pbest[best_idx], pbest_fit[best_idx]

    return gbest, gbest_fit

# Run hybrid
best_params, best_acc = hybrid_optimize()
print(f"Best C = {best_params[0]:.3f}, gamma = {best_params[1]:.3f}")
print(f"Cross-validation accuracy = {best_acc:.3f}")
