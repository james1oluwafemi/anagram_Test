correct_number = 10
play_game = True
while play_game == True:
    user_guess = float(input("Please guess a number: \n"))
    if user_guess < correct_number:
        print("Sorry! Your guess is incorrect. Guess higher")
    elif user_guess > correct_number:
        print("Sorry! Your guess is incorrect. Guess lower")
    else:
        print("Congratulations! You guessed correctly")
        break