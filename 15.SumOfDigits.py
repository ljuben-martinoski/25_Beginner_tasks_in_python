"""SUm of dogits: Here we will calculöate the sum of the digits of a number."""


# we are assigning a variable n 
n = 12345677

number_str = str(n)  # turnign the number into the string so we can look at each digit

digit_sum = 0  # create a variable to hold the sum 

#  for loop to go through the numbes and to add therm ont to the other
for i in number_str:
    digit = int(i) #  assignnig variable that i shoul be printer as a digit
    digit_sum += digit  # this is actuali digit_sum(which is puliung a number from the diogit sum which start from position 0)
    #  plus digit using the operator +=
 

print("The sum of the digits is: ", digit_sum)    