import random

min_num = int(input("Minimum Number: "))
max_num = int(input("Maximum Number: "))
random_number = random.randint(min_num, max_num)
amount_guesses = 0
run = True

while run:
    guess_number = int(input(f"Guess a number between {min_num} and {max_num}: "))
    amount_guesses += 1
    
    if guess_number > max_num or guess_number < min_num:
        print("I AM GOING TO LEAK YOUR CVV TO THE IRS, ENTER A GOOD NUMBER!")
    elif guess_number != random_number:
        print(f"Try again! Total guesses: {amount_guesses}")
    elif guess_number == random_number:
        print(f"WOW! YOu Got IT in {amount_guesses} guesses!")
        run = False
