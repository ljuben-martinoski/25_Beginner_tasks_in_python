"""
     ===Unique Elements===
Write a program to find unique elements in a list using a set!
"""

# here is the program to finding a unique elements in  a set.


numbers = [1,2,3,2,4,5,1,6,3,9,7,8] # creating a list variable with duplicates

unique_numbers = set(numbers) #  converting the list to a set with the set()-method to remove the duplicates

unique_list = list(unique_numbers) # converting back to a list if needed


print("Original list: ", numbers)
print("Unique elements: ", unique_list)