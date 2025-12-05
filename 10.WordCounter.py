""" word Counter:
Count the number of words in a sentence entered by the user.
"""
# creating variable string for the user to enter
user = str(input("Please write a sentence and i will count the words in that sentence: "))
# variable words that will split the words in the user variable
words = user.split()
# count variable that will count the words in the user input
count = len(words)

print("The number of words is: ", count)

print("===================================================================================================")

# here is anotehr way to solve this a littel bit more advanced
# importing the regex module
import re
# defining a funktion with the name word_count,with text as parameter and to return int 
def word_count(text: str) -> int:
    # find all sequences of letters/numbers as words
    words = re.findall(r"\b\w+\b", text)
    # return the number of words
    return len(words)


print(word_count("Hello, world: This is a test."))











