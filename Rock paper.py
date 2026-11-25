import random

playeranswer = "yes"
while playeranswer == "yes":
    print("================================ROCK PAPER SCISSORS===================================")
    print("Hello, welcome to Rock, Paper, Scissors! You will play 5 rounds against the computer. Good luck!")
    computerpoints = 0
    playerpoints = 0
    rounds = 5
    draw = "That's a Draw"
    for t in range(1, 6):
        rounds -= 1
        answer = input("Please type Rock, Paper or Scissors, remember you can type them in lowercase if you want to: ")
        answer = answer.lower()
        if answer == "rock" or answer == "paper" or answer == "scissors":
            print("Good choice!")
        else:
            print("Please type Rock, Paper or Scissors, remember you can type them in lowercase if you want to: ")
            answer = input("Please retry to type Rock, Paper or Scissors: ")
            rounds += 1
        computer = random.choice(["rock", "paper", "scissors"])
        print("Your answer:", answer)
        print("And this is the computer choice:", computer)
        if answer == computer:
            print(draw)
            print("you have", rounds, "rounds left!")
        elif (answer == "rock" and computer == "scissors") or (answer == "paper" and computer == "rock") or (answer == "scissors" and computer == "paper"):
            print("You win")
            print("you have", rounds, "rounds left!")
            playerpoints += 1
        else:
            print("You lose")
            print("you have", rounds, "rounds left!")
            computerpoints += 1
        print("Your points: ", playerpoints)
        print("Computer points: ", computerpoints)
        if rounds == 0:
            print("Game Over!")
            if playerpoints > computerpoints:
                print("You win the game!")
                print("And your final score is: ", playerpoints)
            elif playerpoints < computerpoints:
                print("The computer wins the game!")
                print("And the computer final score is: ", computerpoints)
    print("===============================THANK YOU FOR PLAYING!===================================")
    playeranswer = input("This game will soon restart. Please type Yes if you want to play again or No if you want to exit the game. ").lower()
    print("=======================================GAME OVER========================================")
    print("Made by @vhmshop1234")
   
