#key Parameter : mututation rate,population size
#LOW Mutation rate ->  population become similar -> premature stagnation
#HIGH Mutation -> excessive randomness -> slow convergence
#Moderate mutation ->  balanced exploration and exploitation
import numpy as np

def run_ga(mutation_rate):
    pop = np.random.uniform(-5, 5, 20)
    for _ in range(30):
        fit = -pop**2
        parents = pop[np.argsort(fit)[-10:]]
        children = parents + np.random.normal(0, mutation_rate, 10)
        pop = np.concatenate((parents, children))
    return max(-pop**2)

for m in [0.01, 0.1, 0.5]:
    print("Mutation:", m, "Best fitness:", run_ga(m))
