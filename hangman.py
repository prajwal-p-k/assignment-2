import random

def get_word():
    words = ['python', 'java', 'ruby', 'javascript', 'golang', 'kotlin']
    return random.choice(words)

def display(word, guessed_letters):
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'
    return display_word

def hangman():
    word = get_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display(word, guessed_letters))

    while attempts > 0 and set(word) != set(guessed_letters):
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter at a time.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
        else:
            guessed_letters.append(guess)
            print(display(word, guessed_letters))

    if set(word) == set(guessed_letters):
        print(f"Congratulations! The word was '{word}'.")
    else:
        print(f"Sorry, the word was '{word}'. Better luck next time!")

if __name__ == '__main__':
    hangman()
