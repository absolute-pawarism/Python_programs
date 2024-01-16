def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fib_seq(generator, num_sequences):
    sequence = []
    for _ in range(num_sequences):
        sequence.append(next(generator))
    return sequence
fibonacci_gen = fibonacci_generator()

while True:
    user_input = input("Do you want the next sequence in the Fibonacci series? (next/exit): ").lower()

    if user_input == 'next':
        next_sequence = fib_seq(fibonacci_gen, 1)
        print("Next sequence: ", next_sequence[0])
    elif user_input == 'exit':
        print("Exit")
        break
    else:
        print("Invalid")
