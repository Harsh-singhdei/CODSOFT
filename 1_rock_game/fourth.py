import random


list = ["rock","paper","scissors"]
count = 0
win = 0
tie = 0
lose = 0

# FUNCTION FOR DISPLAYING ALL THE RULES
def rules():
    print("THE BASIC RULES OF THIS GAME ARE:-")
    print("1.   USER and computer have to choose out of three choices randomly")
    print("2.   ROCK BEATS SCISSORS")
    print("3.   SCISSORS BEATS PAPER")
    print("4.   PAPER BEATS ROCK")
    print("5.   USER WILL CHOOSE THERE CHOICE FIRST")
    print("6.   RESULTS WILL BE DISPLAY AFTER COMPARING THE CHOICES OF BOTH PLAYERS(USER & COMPUTER)")
    print("7.   ENTER Y FOR REPLAY N FOR END THE GAME L FOR LEADERBOARD")
    print("8.   ENTER N FOR END THE GAME")
    print("9.   ENTER L FOR LEADERBOARD")
    print()

# FUNCTION TO DISPLAY THE LEADERBOARD
def leader_board(count,win,lose,tie):
    print("\t\t----:LEADERBOARD:----")
    print("Total Numbers of Games Played: |",count,"|")
    print("Total rounds won:              |",win,"|")
    print("Total rounds tie:              |",tie,"|")
    print("Total rounds you lost:         |",lose,"|")
    print()

# FUNCTION FOR SCORE TRACKING    
def SCORE_TRACKING(result,com_choice,count,win,lose,tie):
    if result == 1:
        print("Your choice:     |", choice,"|")
        print("Computer choice: |", com_choice,"|")
        tie += 1
        print()
        print("Its a Tie!!")
        print()
    elif result == 2:
        print("Your choice:     |", choice,"|")
        print("Computer choice: |", com_choice,"|")
        lose += 1
        print()
        print("HARD Luck You Lost -_-")
        print()
    else:
        print("Your choice:     |", choice,"|")
        print("Computer choice: |", com_choice,"|")
        win += 1
        print()
        print("BRAVO You won :) !!!")
        print()
    count += 1
    return (count,win,lose,tie)

# FUNCTION TO DECLARE THE RESULTS
def game(choice,list,count,win,lose,tie):
    replay = "yes"
    while replay == "yes" or replay=="y":
        while(choice not in list):
            choice=input("Invalid Choice \nPlease enter a valid input(rock, paper or scissors): ")
        com_choice = random.choice(list)

        result = 0
        # 1->tie
        # 2->com wins
        # 3->user wins 

        if choice == "rock":
            if com_choice == "rock":
                result = 1
            elif com_choice == "paper":
                result = 2
            else:
                result = 3
        elif choice == "paper":
            if com_choice == "paper":
                result = 1
            elif com_choice == "scissors":
                result = 2
            else:
                result = 3
        else:
            if com_choice == "scissors":
                result = 1
            elif com_choice == "rock":
                result = 2
            else:
                result = 3   

        count,win,lose,tie = SCORE_TRACKING(result,com_choice,count,win,lose,tie)
        
        replay = input("DO you want to play again(press : y for yes / n for no / L for leaderbord / r for rules )) : ").lower()
        print()
        while(replay not in ("n","y","l","r")):
            replay=input("ENter the valid choice (i.e y/n/L): ")
        if(replay not in ("y","n","l","r")):
            replay = input("DO you want to play again(y for YES / n for NO").lower()
        if(replay == "r"):
            print()
            rules()
            leader_board(count,win,lose,tie)
            replay = input("Do you want to play again? (y for yes / n for no): ").lower()
            continue
        if(replay=="l"):
            leader_board(count,win,lose,tie)
            replay = input("Do you want to play again? (y for yes / n for no): ").lower()
        if(replay=="n"):
            leader_board(count,win,lose,tie)
            return
        choice = input("Enter your choice(rock, paper or scissors): ").lower()



print("\t__Welocme to the Rock Paper Scissors Game__")
rules()

print("ENTER S for start N for no")
str = input().lower()
if(str == "s"):
    print()
    choice = input("Enter your choice(rock, paper or scissors): ").lower()
    game(choice,list,count,win,lose,tie)
else:
    print("HOPE YOU COME AGAIN TO PLAY THIS EXCITED GAME :) ")
