"""
Largest of three numbers:
Create a funktion to find the largest number among three given numbers.
"""

# first we need to create three inputs:
# float because we dont know if the user will enter a decimal number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
# assumung a is the largest
largest = a

#  compare with b
if b > largest:
    largest = b

# compare with c
if c > largest:
    largest = c
# if the user enter the same number so it is equal and not largest
if a == largest:
    print("The number is equal") 
else:
    print("The largest number is: ", largest)          

 



