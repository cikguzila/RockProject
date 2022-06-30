#Rock,Paper, Scissors
from random import randint

#create a list of play options
list = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = list[randint(0,2)]

score=0

#set player to False
player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print(computer,"vs",player)
        print("Tie!")
        score=score+1

            
    elif player == "Rock":
        if computer == "Paper":
            print(computer,"vs",player)
            print("You Lose!", computer, "covers", player)
        else:
            print(computer,"vs",player)
            print("You Win!", player, "smashes", computer)
            score=score+2
                
    elif player == "Paper":
        if computer == "Scissors":
            print(computer,"vs",player)
            print("You Lose!", computer, "cut", player)
        else:
            print(computer,"vs",player)
            print("You Win!", player, "covers", computer)
            score+=2
            
    elif player == "Scissors":
        if computer == "Rock":
            print(computer,"vs",player)
            print("You Lose...", computer, "smashes", player)
        else:
            print(computer,"vs",player)
            print("You Win!", player, "cut", computer)
            score+=2
    else:
        print("That's not a valid play. Check your spelling!")
        
    print("Your total score is", score)
    player= input("\nDo you want to continue the game (Type Yes to proceed)? ")
    if player=="Yes":
        player = False
        computer = list[randint(0,2)]

    else:
        player= True
