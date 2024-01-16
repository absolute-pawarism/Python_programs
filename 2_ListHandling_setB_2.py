import random

def generate_birthday():
    return random.randint(1, 365)

def has_duplicate(birthdays):
    return len(birthdays) != len(set(birthdays))

def simulate_birthday_experiment(num_experiments): 
    count_duplicates = 0
    for i in range(num_experiments):
        birthdays = [generate_birthday() for j in range(23)]
        if has_duplicate(birthdays):
            count_duplicates += 1
    probability = count_duplicates / num_experiments
    return probability
num_experiments = 100
estimated_probability = simulate_birthday_experiment(num_experiments)
print(f"probability of at least two students having the same birthday: {estimated_probability:.4f}")
