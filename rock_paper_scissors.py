# Rock, Paper, Scissors Game

# Line 1: Import the random module to generate computer's random choice
import random

# Line 4: Define the main game function
def play_game():
    # Line 6-8: Create a list of possible choices for the game
    choices = ['rock', 'paper', 'scissors']

    # Line 10-11: Display welcome message to the player
    print("Welcome to Rock, Paper, Scissors!")
    print("-" * 40)

    # Line 13-14: Initialize score variables to track wins for player and computer
    player_score = 0
    computer_score = 0

    # Line 16-17: Start main game loop that continues until player wants to quit
    while True:
        # Line 18-20: Display current scores
        print(f"\nScore - You: {player_score} | Computer: {computer_score}")
        print("-" * 40)

        # Line 22-23: Get player's choice and convert to lowercase for consistency
        player_choice = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()

        # Line 25-27: Check if player wants to quit the game
        if player_choice == 'quit':
            print(f"\nFinal Score - You: {player_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        # Line 29-32: Validate player's input
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Line 34-35: Generate computer's random choice from the choices list
        computer_choice = random.choice(choices)

        # Line 37-38: Display both choices
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Line 40-42: Check if it's a tie
        if player_choice == computer_choice:
            print("It's a tie!")

        # Line 44-58: Determine the winner based on game rules
        # Rock beats scissors, scissors beats paper, paper beats rock
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            # Line 48-49: Player wins this round
            print("You win this round!")
            player_score += 1

        else:
            # Line 52-53: Computer wins this round
            print("Computer wins this round!")
            computer_score += 1

# Line 56-58: Check if this script is being run directly (not imported)
if __name__ == "__main__":
    # Line 58: Call the main game function to start the game
    play_game()
