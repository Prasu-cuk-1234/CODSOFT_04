import random

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main program
def play_game():
    choices = ["rock", "paper", "scissors"]

    while True:
        # Get the user's choice
        player_choice = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()

        # Allow the user to exit the game
        if player_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break

        # Validate the player's choice
        if player_choice not in choices:
            print("Invalid choice, please try again.")
            continue

        # Computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)

# Run the game
play_game()