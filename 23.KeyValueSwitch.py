"""Key-Value Switch: Swap the Keys and Values in a dictionary."""

# first we need to create a dictionary
original = {"a:":1,"b:":2,"c:":3,}

swaped = {} # creating a new epmty dictionary 

#for loop to swap the keys and values

for key, value in original.items():
    swaped[value] = key   #  for each pair , you assign value as the new key as the value in the swapped dictionary.

print(swaped) 

# here is another wey to do it

original1 = {"a:":11,"b:":12,"c:":13,} # creating the dictionary

swaped1 = {v: k for k, v in original.items()} # - This is a loop inside the dictionary comprehension.
# It iterates through each (key, value) pair, assigning k to the key and v to the value.



print(swaped)

"""Impoortant notince:
If the original dictionary has a duplicate values, the swap will overwrite keys because dictionary keys must be unique.
Ecample:
original = {"a": 1, "b": 1}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'b'} → 'a' is lost"""