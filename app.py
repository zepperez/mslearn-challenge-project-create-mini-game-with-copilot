# write a multiplayer game called rock paper scissors

# The game should have the following features:

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.

# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.

# By the end of each round, the player can choose whether to play again.

# Display the player's score at the end of the game.

# The mini game must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

# The mini game must handle the computer's choice randomly.
import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("The first to 3 points wins!")
    print("Good luck!")
    print("")

    # set up variables
    player_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]

    # game loop
    while player_score < 3 and computer_score < 3:
        print("Your score: " + str(player_score))
        print("Computer score: " + str(computer_score))
        print("")

        # player input
        player_choice = input("Choose rock, paper, or scissors: ")
        player_choice = player_choice.lower()

        # check if player input is valid
        while player_choice not in options:
            print("Invalid option. Please try again.")
            player_choice = input("Choose rock, paper, or scissors: ")
            player_choice = player_choice.lower()

        # computer input
        computer_choice = random.choice(options)

        # print choices
        print("")
        print("You chose " + player_choice + ".")
        print("The computer chose " + computer_choice + ".")
        print("")

        # check who won
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "paper":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1

        print("")
        time.sleep(1)

    # print final scores
    print("Your score: " + str(player_score))
    print("Computer score: " + str(computer_score))
    print("")

    # print winner
    if player_score > computer_score:
        print("You win!")
    else:
        print("You lose!")

    print("")

    # ask if player wants to play again
    play_again = input("Play again? (y/n): ")
    play_again = play_again.lower()