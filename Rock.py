def do_you_want_play():
    play = input("Do you want to play?")
    return play.lower() in ["y", "yes"]


while do_you_want_play():

    player1 = input("Player1 please make your pick: ")
    player2 = input("Player2 please make your pick: ")

    # Draw
    if (player1 == "rock" and player2 == "rock") or (player1 == "paper" and player2 == "paper") or \
            (player1 == "scissors" and player2 == "scissors"):
        print("Player1 is ", player1, " and Player2 is ", player2)
        print("************ This is a draw ************")

    # Player1 winner
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or \
            (player1 == "paper" and player2 == "rock"):

        print("Player1 is ", player1, " and Player2 is ", player2)
        print("************ Player1 WON ************")

    # Player2 winner
    elif (player2 == "rock" and player1 == "scissors") or (player2 == "scissors" and player1 == "paper") or \
            (player2 == "paper" and player1 == "rock"):

        print("Player1 is ", player1, " and Player2 is ", player2)
        print("************ Player2 WON ************")
