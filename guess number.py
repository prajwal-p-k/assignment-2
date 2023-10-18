import random

def guess_the_number():
    # Define the range for the random number
    lower_limit = 1
    upper_limit = 100
    
    # Generate a random number between the limits
    number = random.randint(lower_limit, upper_limit)
    
    print(f"Guess the number between {lower_limit} and {upper_limit}!")
    
    # Counter for the number of guesses
    guess_count = 0
    
    while True:
        # Get the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("That's not a valid number. Try again!")
            continue
        
        # Increment the guess count
        guess_count += 1
        
        # Check if the guess is correct, too high, or too low
        if user_guess == number:
            print(f"Congratulations! You've guessed it in {guess_count} tries!")
            break
        elif user_guess < number:
            print("Too low!")
        else:
            print("Too high!")

guess_the_number()
