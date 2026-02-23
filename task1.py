"""Calculate factorial using recursion"""

number = int(input("Enter a number : "))

def factorial(number):
    if number < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    # Base case
    if number == 0 or number == 1:
        return 1

    # Recursive case
    return number * factorial(number - 1)

factorial_result = factorial(number)

print(f"The factorial of {number} is {factorial_result}")
