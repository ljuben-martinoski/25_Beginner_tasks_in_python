"""Here we will converting a list into a tuple and vise versa
We just first neeed to understand what is tuple-tuple are actualy a list with valuest  that are not changabel in python"""

#### Here first we will converat a list in to a tupel.
#  variable my_list
my_list = [1,2,4,6,7,8,9]

my_tupel = tuple(my_list)


print("List: ", my_list)
print("Tupel: ", my_tupel)


#### Here we will converta a tuple in list

my_tuple2 = [33,99,22,88,11,44,66,77] # creating a tuple variable

my_list2 = list(my_tuple2)   #  converting a the tuple into a list

print(my_list2)  #    printing the outcome