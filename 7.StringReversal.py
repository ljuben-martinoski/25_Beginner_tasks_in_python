""" String Reversal:
 Write a program to reverse a string without using built-in functions. """

# ask the user for a string 
text = input("enter a string: ")
# Create an empty string for the reversed result
reversed_text = ""

# looping backward throught the string using indexes
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print("Reversed String: ", reversed_text)


print("================================================================================================")

# advanced style 
# creating a funktion with parameter s as string and telling python to return a string
def reverse_string(s: str) -> str:
    chars = []
    # build a list manualy in reverse order, len(lenght) of the parameter s to go backvards - 1
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i]) # appending char value(to return a single value) 
    return "".join(chars) 

print(reverse_string("Lagerverwaltungs"))    




