import random 

choices = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        elif computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        elif computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Goodbye!")
        break
