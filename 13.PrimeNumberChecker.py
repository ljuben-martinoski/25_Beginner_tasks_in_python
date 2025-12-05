# Prime Number Checker:
# Check if a number is prime or not.

# first we need to know wnat actualy a prime number is:
#Prime number is natural number greater than 1 that is not product of two smaller natural numbers(wikipedia).

# asking the user to input a niumber
number = int(input("Enter a number: "))

# a flag that will tell us if the number is a prime number
is_prime = True

# number less than 2 canot be prime
if number < 2:
    is_prime = False
else:
    # check every number from 2 up to(number - 1)
    for i in range(2, number):
        if number % i == 0: # if divisible not a prime
            is_prime = False
            break # stop checking if we already know

# print the result
if is_prime:
    print(number,"is a prime number.")
else:
     print(number,"is NOT a prime number.")       



print("-----------------------------------------------------------------------------------------------------------------------------")

# another way to do this more advanced just for a example

def is_prime1(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
# Only check odd numbers up to Vn(square root of n)
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True
# Example usage
num = 137
print(is_prime1(num)) # output True