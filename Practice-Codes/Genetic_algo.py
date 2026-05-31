import numpy as np

def fitness(x):
    return -(x**2 + 5*np.sin(x))   # maximize fitness

pop = np.random.uniform(-5, 5, 20)

for _ in range(50):
    fit = fitness(pop)
    parents = pop[np.argsort(fit)[-10:]]
    children = parents + np.random.normal(0, 0.2, 10)
    pop = np.concatenate((parents, children))

best = pop[np.argmax(fitness(pop))]
print("Best solution:", best)
