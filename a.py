import matplotlib.pyplot as plt

# Assuming fib_seq is already defined from previous Fibonacci code
# Golden Ratio approximation
def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Number of terms to generate
n_terms = 20
fib_seq = fibonacci_sequence(n_terms)

ratios = [fib_seq[i+1]/fib_seq[i] for i in range(1, len(fib_seq)-1)]

plt.figure(figsize=(8, 5))
plt.plot(range(2, len(fib_seq)), ratios, marker='o', linestyle='--', color='teal')
plt.axhline(y=1.618, color='r', linestyle=':', label='Golden Ratio')
plt.title("Convergence to the Golden Ratio")
plt.xlabel("n")
plt.ylabel("F(n+1) / F(n)")  # ← this was just misplaced before
plt.grid(True)
plt.legend()
plt.show()
