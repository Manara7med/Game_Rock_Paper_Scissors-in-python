#Algorithm
#Start the game.
#Display the game instructions and options to the player (rock, paper, scissors).
#Initialize the player's score and the computer's score to 0.
#Set the number of attempts or rounds desired.
#For each round:
#a. Prompt the player to enter their choice (rock, paper, or scissors).
#b. Generate a random choice for the computer (rock, paper, or scissors).
#c. Compare the player's choice with the computer's choice to determine the winner of the round.
#d. Update the scores based on the outcome of the round.
#e. Display the choices made by the player and the computer, and the result of the round.
#After all rounds have been played:
#a. Display the final scores.
#b. Determine and display the overall winner based on the scores.
#End the game


#Code

import random

def play_game(attempts):
    print("Let's play Rock, Paper, Scissors!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    for _ in range(attempts):
        player_choice = int(input("Your turn: ")) - 1
        player_move = choices[player_choice]

        computer_choice = random.randint(0, 2)
        computer_move = choices[computer_choice]

        print("You chose:", player_move)
        print("Computer chose:", computer_move)

        if player_move == computer_move:
            print("It's a tie!")
        elif (
            (player_move == "rock" and computer_move == "scissors")
            or (player_move == "paper" and computer_move == "rock")
            or (player_move == "scissors" and computer_move == "paper")
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print("")

    print("Game over!")
    print("Your score:", player_score)
    print("Computer score:", computer_score)
    if player_score > computer_score:
        print("Congratulations, you win!")
    elif player_score < computer_score:
        print("Sorry, computer wins!")
    else:
        print("It's a tie!")

play_game(6)