import random

min_num = int(input("Minimum Number: "))
max_num = int(input("Maximum Number: "))
random_number = random.randint(min_num, max_num)
amount_guesses = 0
run = True

while run:
    guess_number = int(input(f"Guess a number between {min_num} and {max_num}: "))
    amount_guesses += 1
