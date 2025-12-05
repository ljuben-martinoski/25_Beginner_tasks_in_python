"""Character Counter:
Couunt the number of vowels and constants in a string.#
"""

# telling the user to enter a string , and with si creating a variable
user = input("Please enter a String, and i will tell you the number of vowels and constatns: ")
# seting that watherver the user entered it is converted to lower case letters
user = user.lower()
# variable that asigns the vowels
vowels ="aeiou"
# assignning a starting count for the vowels
vowel_count = 0
# assigning a starting count for the constants
constant_count = 0

# for loop, using a char(used to represent one character in a string),because here we need the numbe oif vowels and constants
for char in user:
    # this here insures that only letters are counted
    if char.isalpha():
        # loop in a loop, to search the vowels.
        if char in vowels:
            vowel_count += 1 # to increase the count for 1
        else:
            constant_count += 1 #  to increase the count for 1

print("Vowels: ", vowel_count)
print("Constants: ", constant_count)

print("===============================================================================================================")


         
