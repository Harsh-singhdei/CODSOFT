#                          A BASIC CALCULATOR TO PERFORM BASIC MATHEMATICS OPERATIONS


num1 = float(input("ENTER THE FIRST NUMBER: "))

again = "y"
while(again != "n"):
    
    
    num2 = float(input("ENTER THE SECOND NUMBER: "))
    operand = input("ENTER THE OPERATION: ")

    if(operand == "+"):
        answer = num1 + num2
        print(answer)
    elif(operand == "-"):
        answer = num1 - num2
        print(answer)
    elif(operand == "*"):
        answer = num1 * num2
        print(answer)
    elif(operand == "/"):
        answer = num1 / num2
        print(answer)
    elif(operand == "%"):
        answer = num1 % num2
        print(answer)
    elif(operand == "**"):
        answer = num1 ** num2
        print(answer)
    else:
        print("ENTER A VALID DATA ")
    num1 = answer
    print("YOU want to perform more operations then enter y -> yes otherwise enter n -> no")
    again = input("")

