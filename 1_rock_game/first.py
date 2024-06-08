import random

replay = "yes"
count = 0

win = 0
tie = 0
lose = 0


while replay == "yes":
    choice = input("Enter your choice: ")

    list = ["rock","paper","scissors"]
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
        print("Result is : TIE")
    elif result == 2:
        print("Your choice: ",choice)
        print("Computer choice: ", char )
        lose += 1
        print("Result is : LOSE")
    else:
        print("Your choice: ",choice)
        print("Computer choice: ", char )
        win += 1
        print("Result is : WIN")
    replay = input("you want to play again: ")
    count += 1

print("total no. of rounds played: ",count)
print("Total rounds win: ",win)
print("Total rounds tie: ",tie)
print("Total rounds lose: ",lose)

