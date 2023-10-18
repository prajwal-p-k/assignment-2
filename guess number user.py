import random

def guess_the_number():
    # Define the range for the number to be guessed
    lower_bound = 1
    upper_bound = 100
    
    # Computer picks a random number between lower_bound and upper_bound
    number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    while True:
        try:
            # Ask the user to guess the number
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            # Check if the guess is correct
            if guess < number:
                print("Your guess is too low.")
            elif guess > number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")
            

if __name__ == "__main__":
    guess_the_number()
