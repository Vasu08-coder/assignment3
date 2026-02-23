import math

number = float(input("Enter a number: "))

if number < 0:
    print("Square root and log are not defined for negative numbers.")
else:
    print("Square root:", math.sqrt(number))
    print("Logarithm:", math.log(number))

# Sine works for all numbers
print("Sine value:", math.sin(number))