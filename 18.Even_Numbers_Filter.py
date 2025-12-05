"""
Event numbers filter
Extreact all numbers from a lists.
the idea of the program is to extract all the even numbers form a  list"""

#So first we need to create a list from a number,
numbers = [1,2,3,4,5,6,22,34,56,456,786,3234,4563466,23423,23126674,3434234,345466,432525,]

# Then create new empty list so we can enter the new even nubers that are choosed from the list
even_numbers = [] 

# then we creat the loop 
for num in numbers:
    if num % 2 == 0: # here we are saying the we what it to list and print all the numbers that are even, and we are using a modulo
        even_numbers.append(num) # Heer we are appending the num to the even_numbers lit(appending the even numbers)

print("The even numbers are: ", even_numbers)        

# We could also do it in this way

zahlen = [2,5,6,8,34,123,56,78,237,34,78,2345,9767,23256,457674,45]

gleich_numbers = [num for num in zahlen if num % 2 == 0 ] # filöters even numbers using list comprehension 

print(gleich_numbers)
