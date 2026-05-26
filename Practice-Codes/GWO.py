import numpy as np

# Objective function (Sphere)
def fitness(x):
    return np.sum(x**2)

# Grey Wolf Optimization
def GWO(n_wolves=10, dim=2, max_iter=30):

    # Initialize wolves
    wolves = np.random.uniform(-10, 10, (n_wolves, dim))

    for t in range(max_iter):
        # Evaluate fitness
        fitness_values = np.array([fitness(w) for w in wolves])

        # Sort wolves
        sorted_idx = np.argsort(fitness_values)
        alpha = wolves[sorted_idx[0]]
        beta  = wolves[sorted_idx[1]]
        delta = wolves[sorted_idx[2]]

        # Parameter 'a' decreases linearly
        a = 2 - t * (2 / max_iter)

        for i in range(n_wolves):
            for leader in [alpha, beta, delta]:
                r1, r2 = np.random.rand(), np.random.rand()
                A = 2*a*r1 - a
                C = 2*r2

                D = abs(C*leader - wolves[i])
                X = leader - A*D

                if leader is alpha:
                    X1 = X
                elif leader is beta:
                    X2 = X
                else:
                    X3 = X

            # Update position
            wolves[i] = (X1 + X2 + X3) / 3

        print(f"Iteration {t+1}: Best = {fitness(alpha):.5f}")

    return alpha, fitness(alpha)


# Run
best_pos, best_val = GWO()

print("\nFinal Solution:")
print("Best Position:", best_pos)
print("Minimum Value:", best_val)
