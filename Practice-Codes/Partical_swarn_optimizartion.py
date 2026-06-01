import numpy as np

# Objective function
def objective_function(x):
    return np.sum(x**2)

# PSO Algorithm
def pso(n_particles=10, dim=2, max_iter=50):
    # Initialize particles
    particles = np.random.uniform(-10, 10, (n_particles, dim))
    velocities = np.random.uniform(-1, 1, (n_particles, dim))

    # Personal best
    pbest = particles.copy()
    pbest_val = np.array([objective_function(p) for p in particles])

    # Global best
    gbest = pbest[np.argmin(pbest_val)]

    # Parameters
    w = 0.5      # inertia
    c1 = 1.5     # cognitive
    c2 = 1.5     # social

    for _ in range(max_iter):
        for i in range(n_particles):
            r1, r2 = np.random.rand(), np.random.rand()

            # Update velocity
            velocities[i] = (w * velocities[i] +
                             c1 * r1 * (pbest[i] - particles[i]) +
                             c2 * r2 * (gbest - particles[i]))

            # Update position
            particles[i] += velocities[i]

            # Update personal best
            val = objective_function(particles[i])
            if val < pbest_val[i]:
                pbest[i] = particles[i]
                pbest_val[i] = val

        # Update global best
        gbest = pbest[np.argmin(pbest_val)]

    return gbest, objective_function(gbest)

# Run PSO
best_pos, best_val = pso()
print("Best Position:", best_pos)
print("Best Value:", best_val)
