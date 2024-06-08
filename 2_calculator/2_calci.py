#                                    A BASIC CALCULATOR TO PERFORM BASIC MATHEMATICS OPERATIONS

# Used for formating and making user interface better
def print_separator():
    print("=" * 40)

# Used to get i/p from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Used to get the operation from the user
def get_operation():
    valid_operations = ["+", "-", "*", "/", "%", "**"]
    while True:
        operand = input("Enter the operation (+, -, *, /, %, **): ")
        if operand in valid_operations:
            return operand
        else:
            print("Invalid operation. Please enter a valid operation.")

print_separator()
print("WELCOME TO THE BASIC CALCULATOR")
print_separator()

num1 = get_number("Enter the first number: ")

# making calculator to use again and again
again = "y"
while again.lower() != "n":
    num2 = get_number("Enter the second number: ")
    operand = get_operation()

# making calculations
    if operand == "+":
        answer = num1 + num2
    elif operand == "-":
        answer = num1 - num2
    elif operand == "*":
        answer = num1 * num2
    elif operand == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        answer = num1 / num2
    elif operand == "%":
        if num2 == 0:
            print("Error: Modulo by zero is not allowed.")
            continue
        answer = num1 % num2
    elif operand == "**":
        answer = num1 ** num2

    print(f"The result of {num1} {operand} {num2} is: {answer}")
    num1 = answer

    print_separator()
    again = input("Do you want to perform more operations? (y/n): ").strip().lower()
    if(again == "y"):
        continue
    elif(again == "n"):
        break
    else:
        print("Enter the valid input !!")
    again = input("Do you want to perform more operations? (y/n): ").strip().lower()

print_separator()

print("Thank you for using the basic calculator!")