"""Dictionary Sorting: 
Sort a dictionary by its keys or values"""

dictionary = {
    "a": 1,
    "c": 3,
    "b": 2,
    "e": 5,
    "f": 6,
    "d": 4,
    "h": 7,
    "g": 8
}
#------------------
# Sorting by keys a-z
#--------------------
# sorted_by_keys = sorted(dictionary.items()) turns the dictionary into a list of (key,value) pairs
# and sorts them by the key automatically.
sorted_by_keys = sorted(dictionary.items())

# convert the sorted list back into a dictioary
sorted_by_keys = dict(sorted_by_keys)

print("Sorted by keys: ", sorted_by_keys)

#-----------------------
# Sorted by Values(small -> big)
# ----------------------

# key = lambda item:item[1]) means:
# "sort by the second element of each pair" -> which is the value.
sorted_by_values = sorted(dictionary.items(), key = lambda item:item[1])

# convert to dictionary
sorted_by_values = dict(sorted_by_values)

print("Sorted by values: ", sorted_by_values)