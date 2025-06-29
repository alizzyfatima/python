def fibonacci_loop(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci_loop(10))
