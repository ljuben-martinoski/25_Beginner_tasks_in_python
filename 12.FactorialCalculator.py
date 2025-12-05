"""Factorial Calculator:
Write a funktion to calculate the factorial of a given number """


# creating a variable for user input
number = int(input("Enter a number: "))

# factorial starts at 1
factorial = 1

# Multiply all numbers from 1 to the given number
for i in range(1, number + 1): # loop through all the numbers from 1 up to 'number'
    factorial = factorial * i

print("Factorial of", number,"is", factorial)


print("=========================================================================================================================")

#  Advanced way to solve the same problem,

#defining a function , here factorial with 1 parameter n that we want to be in a integer type.
def calculate_factorial(n: int) -> int:
    # check for a invalid input: factorila does not exist dor negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # directly return 1 if n is a 0 or 1 (both factorials are 1)
    if n in (0,1):
        return 1
    #initialize the result accumulator
    result = 1
    #Multiply all integers from 2 up to n
    # Using range(2, n + 1) avoids unneceassary multiplication by 1
    for i in range(2,n + 1):
        result *= i # same as result = result * i, faste and cleaner
        return result
    

print(calculate_factorial(10))    