# creating a funktion with a name count_characters with parametrers text as string 
# and telling python to return a tuple with parameter integer.
def count_characters1(text: str) -> tuple(int, int):
    # assigning a variable for the vowels
    vowels = set("aeiouAEIOU")
    # starting the count from 0
    vowel_count = 0
    # also here
    constant_count = 0
# starting a for loop, also as char 
    for ch in text:
        # same here insurin that only letters are counted
        if ch.isalpha():
            if ch in vowels1:
                vowels_count += 1
            else: 
                constant_count += 1
    return vowel_count, constant_count
# assigning a variable for the v,c
v, c = count_characters1("LagerverwaltungsApp")
print("Vowels: ", v)
print("Constant: ", c)   