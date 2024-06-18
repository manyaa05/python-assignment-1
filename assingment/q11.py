# Write a python program that generates the first n numbers in the Fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = []

    a, b = 0, 1

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

def print_fibonacci_sequence(sequence):
    print("Fibonacci Sequence:")
    for num in sequence:
        print(num, end=" ")

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_sequence = generate_fibonacci(n)

print_fibonacci_sequence(fibonacci_sequence)
