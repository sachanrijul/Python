"""
Python random module notes:
This module implements pseudo-random number generators for various distributions.
Useful for random selections, shuffling, generating random numbers, etc.
"""

import random

# ------------------- Basic Functions -------------------

# 1. random() – Returns a random float number in [0.0, 1.0)
print(random.random())  # e.g., 0.37444887175646646

# 2. uniform(a, b) – Returns a random float in [a, b] or [b, a]
print(random.uniform(1, 10))  # e.g., 5.432

# 3. randint(a, b) – Returns a random integer N such that a <= N <= b
print(random.randint(1, 6))  # Simulates dice roll

# 4. randrange(start, stop[, step]) – Returns a random integer from range(start, stop, step)
print(random.randrange(0, 10, 2))  # Even number from 0 to 8

# ------------------- Sequence Related Functions -------------------

items = ['apple', 'banana', 'cherry', 'date']

# 5. choice(seq) – Returns a random element from non-empty sequence
print(random.choice(items))  # e.g., 'banana'

# 6. choices(population, weights=None, *, cum_weights=None, k=1) – Returns k random elements with replacement
print(random.choices(items, k=3))  # e.g., ['date', 'banana', 'banana']

# 7. choices() with weights
weights = [10, 5, 1, 1]  # apple more likely than cherry or date
print(random.choices(items, weights=weights, k=5))

# 8. shuffle(x) – Shuffles sequence x in place
random.shuffle(items)
print(items)  # items order changed randomly

# 9. sample(population, k, *, counts=None) – Returns k unique elements chosen without replacement
print(random.sample(items, 2))  # e.g., ['cherry', 'apple']

# ------------------- State Management -------------------

# 10. seed(a=None, version=2) – Initialize random number generator for reproducibility
random.seed(123)
print(random.random())  # Always same output for this seed

# 11. getstate() and setstate(state) – Save and restore internal state of RNG
state = random.getstate()
print(random.random())
random.setstate(state)
print(random.random())  # Same as previous print

# ------------------- Random Number Generators for Various Distributions -------------------

# 12. betavariate(alpha, beta) – Beta distribution (0 to 1)
print(random.betavariate(2, 5))

# 13. expovariate(lambd) – Exponential distribution; lambd = 1/mean
print(random.expovariate(1.5))

# 14. gammavariate(alpha, beta) – Gamma distribution
print(random.gammavariate(2, 2))

# 15. gauss(mu, sigma) – Gaussian distribution (mean mu, std dev sigma)
print(random.gauss(0, 1))

# 16. lognormvariate(mu, sigma) – Log normal distribution
print(random.lognormvariate(0, 0.25))

# 17. normalvariate(mu, sigma) – Normal distribution (like gauss)
print(random.normalvariate(0, 1))

# 18. vonmisesvariate(mu, kappa) – Circular data distribution (mu: mean angle, kappa: concentration)
print(random.vonmisesvariate(0, 4))

# 19. paretovariate(alpha) – Pareto distribution
print(random.paretovariate(1.5))

# 20. weibullvariate(alpha, beta) – Weibull distribution
print(random.weibullvariate(1, 1.5))

# ------------------- Random Class for Independent Generators -------------------

# You can create independent RNGs with own internal states using random.Random()

r1 = random.Random()  # New generator instance
print(r1.randint(1, 10))

r2 = random.Random(42)  # Seeded instance for reproducible results
print(r2.random())

# ------------------- Notes on Randomness -------------------

# - random module uses Mersenne Twister RNG algorithm (pseudo-random)
# - Not suitable for cryptographic purposes
# - For cryptography use `secrets` module instead

# ------------------- Summary -------------------

# Common use cases:
# - random.random(): base random float [0,1)
# - random.randint(): random integer in inclusive range
# - random.choice(): select random item from sequence
# - random.shuffle(): randomize sequence order
# - random.sample(): select unique random subset
# - random.seed(): fix randomness for reproducibility

# ------------------- End of random module notes -------------------
