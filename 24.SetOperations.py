"""Set Operations:
Perform union, intersection, and difference operations on two sets.
This module will explain and show implementation of the set operations.
Here we will see how with clear example how union, intersection, and differences work in praktice.
Definitions of set of operations:
  - union
  - Intersection
  - Difference
"""

# Defining two sets 
A = {1,2,3,4}
B = {3,4,5,6}

union = A.union(B)    #  union

intersection = A.intersection(B)   # intersection

difference_A_B = A.difference(B)   # difference
   
difference_B_A = B.difference(A)   #  difference


print("Union: ", union)
print("Intersection: ", intersection)
print("A-B: ", difference_A_B)
print("B-A: ", difference_B_A)



print("------------------------------------------------------------------------------------------------------------------------------------")


"""There is also another way"""

C, D = {1,2,3,4},{3,4,5,6} # seting variables for C and D

# JSON based strukture
result = {
    "Union": C | D,  # union with the operator | 
    "intersection": C & D, # intersection with the operator &
    "difference C - D": C - D, # difference with the operator -
    "difference D - C": D - C 
}
print(result)