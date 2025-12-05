"""List Reversal:
Reverse a list without using built-in funktions...."""

# Example

list = [1,2,3,4,5,6,7,8,9,10]   # creating a list

reversed_list =  []  # creating an empty list

# using a for loop , to loop through each number
for item in list:
    reversed_list.insert(0, item)  # put each item at the beginning of reversed_list


print("Original list: ", list)
print("Revrsed list: ", reversed_list)    


print("-----------------------------------------------------------------------------------------------------------------")
"""Or we can do it also in this way"""

# to keep it even more simple  withiut crating a new list 

numbers = [1,2,3,4,5,6,7,8,9,10] # variable numbers as a list

left = 0  
right = len(numbers) - 1

# while loop as long left is smaller then right 
while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left] # swaping tzhe places of the elements in the list 

    left += 1 # move one step forward for 
    right -= 1 #  move one step backwards 

print(numbers)    

print("-----------------------------------------------------------------------------------------------------------------")

# or also we can do it this way
# reversing using manual pointer walk and list comprehension concepts(no-built-ins)

def reverse_list1(data):  
    reversed_data = []   #  creating a empty list that will store the reversed items

    i = len(data) - 1  # start the i at the last index of the list(lenght - 1)

    while i >= 0:   #  while loop as long as i is a valid index (0 or higher)
        reversed_data.append(data[i])   # append the element at index i to the reversed list
        i -= 1  #  move one step backvards in the list

    return reversed_data   # after the loop finishes, return the fully reversed list

numbers2 = [1,2,3,4,5,6,7,8,9]  # variable numbers as a lsit
result = reverse_list1(numbers2)  # variable result

print("Original: ", numbers2)
print("Reversed: ", result)
