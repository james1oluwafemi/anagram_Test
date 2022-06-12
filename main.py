import random

while True:
    user_input = input("Enter a choice (r for rock, p for paper, s for scissors): \n").lower()

    try:
        if user_input == "r":
            user_action = "rock"
            
        elif user_input == "p":
            user_action = "paper"
            
        elif user_input == "s":
            user_action = "scissors"

    except:
        print("Invalid input, please try again")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nPlayer {user_action}: CPU {computer_action}\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break