import random

def computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    if player == "rock":
        return "You win!" if computer == "scissors" else "Computer wins!"
    if player == "paper":
        return "You win!" if computer == "rock" else "Computer wins!"
    if player == "scissors":
        return "You win!" if computer == "paper" else "Computer wins!"

def main():
    print("Rock, Paper, Scissors - The Game!")
    while True:
        player = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        
        if player not in ["rock", "paper", "scissors", "exit"]:
            print("Invalid choice, please choose again.")
            continue
        
        if player == "exit":
            print("Thanks for playing!")
            break

        comp = computer_choice()
        print(f"Computer chose {comp}.")
        
        result = determine_winner(player, comp)
        print(result)

if __name__ == "__main__":
    main()
