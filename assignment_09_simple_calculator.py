# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# Start of the calculator program

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return round(a / b, 2)

def modulus_numbers(a, b):
    return a % b

def exponentiate_numbers(a, b):
    return a ** b

# Menu display and user interaction
while True:
    print("\n ============================")
    print("        SIMPLE CALCULATOR")
    print(" ============================")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")
    print(" 5. Modulus")
    print(" 6. Exponentiation")
    print(" 7. Quit")

    choice = input("Select an operation (1-7): ")

    if choice == '7':
        print("Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Error: Invalid choice. Please select a number between 1 and 7.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    if choice == '1':
        result = add_numbers(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract_numbers(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply_numbers(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide_numbers(num1, num2)
        operation = '/'
        if result is None:
            continue
    elif choice == '5':
        result = modulus_numbers(num1, num2)
        operation = '%'
    elif choice == '6':
        result = exponentiate_numbers(num1, num2)
        operation = '**'

    print(f"Result: {num1} {operation} {num2} = {result}")