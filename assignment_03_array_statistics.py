# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1

#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# the for loop to take input from the user

numbers = []
n = int(input("How many numbers? "))
if n <= 0:
    print("Error: Please enter a positive integer.")
else:
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

#sum function
def cal_sum(n):
    final=0
    for i in n:
        final+=i
    return final

#average function
def cal_average(n):
    total=cal_sum(n)
    average=total/len(n)
    return average

#maximum function
def cal_max(n):
    max_value=n[0]
    for i in n:
        if i>max_value:
            max_value=i
    return max_value


#minimum function
def cal_min(n):
    min_value=n[0]
    for i in n:
        if i<min_value:
            min_value=i
    return min_value
print(f"Results:")
print(f"Sum: {cal_sum(numbers)}")
print(f"Average: {cal_average(numbers)}")
print(f"Maximum: {cal_max(numbers)}")
print(f"Minimum: {cal_min(numbers)}")
