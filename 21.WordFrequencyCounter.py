"""
Task: word Frequency Counter=> Count the frequency of each word in a given sentence using a dictionary.
"""


# first we need to create a variable containing a sentence

sentence = "Word frequency counter counts the frequency of each word in a sentence" # creating a variable 

words = sentence.lower().split() # convert to lowercase and into word
freq = {} # creating a empty dictionary

# creating a for loop to search the repating word
for word in words:
    if word in freq:
        freq[word] += 1 # increment count if the word exists

    else:
        freq[word] = 1  #  initialize count if word is new


print(freq)      


"""Python has built in tools that make this much shorter and more elegant"""

from collections import Counter

line = "Word frequency counter counts the frequency of each word in a sentence" # creating a variable 
wort = line.lower().split() #  variable , that is converting the "line" variable to lower cases and splits the string into a list of words(whitspace diveided)
freq = Counter(words)
print(freq)
