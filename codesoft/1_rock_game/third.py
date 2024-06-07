import random

replay = "yes"
count = 0

win = 0
tie = 0
lose = 0


def leader_board(count,win,lose,tie):
    print("Total Numbers of Games Played: ",count)
    print("Total rounds won: ",win)
    print("Total rounds tie: ",tie)
    print("Total rounds you lost: ",lose)
    print()






print("__Welocme to the Rock Paper Scissors Game__")
list = ["rock","paper","scissors"]
while replay == "yes" or replay=="y":
    choice = input("Enter your choice(i.e rock , paper or scissors): ").lower()
    while(choice not in list):
        choice=input("Invalid Choice please Enter valid input: ")
    char = random.choice(list)
    result = 0
    # 1->tie
    # 2->com wins
    # 3->user wins 
    if choice == "rock":
        if char == "rock":
            result = 1
        elif char == "paper":
            result = 2
        else:
            result = 3
    elif choice == "paper":
        if char == "paper":
            result = 1
        elif char == "scissors":
            result = 2
        else:
            result = 3
    else:
        if char == "scissors":
            result = 1
        elif char == "rock":
            result = 2
        else:
            result = 3   

    if result == 1:
        print("Your choice: ",choice)
        print("Computer choice: ", char )
        tie += 1
        print()
        print("Its a Tie!!")
        print()
    elif result == 2:
        print("Your choice: ",choice)
        print("Computer choice: ", char )
        lose += 1
        print()
        print("HARD Luck YOu Lost -_-")
        print()
    else:
        print("Your choice: ",choice)
        print("Computer choice: ", char )
        win += 1
        print()
        print("BRAVO You won!!!!")
        print()
    count += 1
    replay = input("DO you want to play again(y for yes / n for no (press L for leaderbord)): ").lower()
    while(replay not in ("n","y","l")):
        replay=input("ENter the valid choice (i.e y/n/L): ")
    if(replay not in ("y","n","l")):
        replay = input("DO you want to play again(y for YES / n for NO").lower()
    if(replay=="l"):
        leader_board(count,win,lose,tie)
    if(replay=="n"):
        leader_board(count,win,lose,tie)
        
    