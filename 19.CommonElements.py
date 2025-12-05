"""

Common Elements: find the common elements between two lists
So here we neeed to create a for example two lists and compare the content in the both of them,
and find the common elements in both of them  """


list_1 = ['apple', 'orange', 'mandarine', 'kokos', 'mango']  # creating the firstlist
list_2 = ['tomaten', 'banane', 'strawbery', 'kokos', 'papaya'] # creating the second list 
common_list = [] # creating the third empty list so we can put the common item 


#creating a loop to serch in the both lists for the same item
for item in list_1:
    if item in list_2:
        common_list.append(item) ## appending the common item to the empty list 



print("The common element is: ", common_list)        

# we can alos do it with number in the following way
list1 = [2,5,6,9,123,34,56,64545,678]
list2 = [3,4,7,89,23,43,9,12,345,977,1234,321234,54543]

#using sets, 
#so first converting the both list into sets,like here
set1 = set(list1) # converting the first list into set 
set2 = set(list2) # converitng the sedocnf list into a set 

the_common_elements = set1.intersection(set2) # finding the intersections for the common elements, we doing intersection,
#=> the two lists 
the_common_list = list(the_common_elements)  # converting back to a list if you want 
print("The common element is: ",the_common_list)