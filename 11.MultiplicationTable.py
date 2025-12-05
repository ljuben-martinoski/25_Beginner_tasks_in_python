"""Multiplication Table: 
Print the multiplication table for a number entered by the user. """



user = int(input("Please entert a number and i will give you the multiplication tabele for that number: "))


for i in range(1,11):
    result = user * i
    print(user, "x", i, "=", result)




print("=============================================================================================================================")
#  advanced way to do this
# defining a funktion multiplication tabele
# with parameters that means n:must be an integer, up_to is also and integer and has a default value of 10, None=> tells python that the funktion returns nothing
def multiplication_table(n: int, up_to: int = 10) -> None:
    for i in range(1, up_to + 1):
        print(f"{n} * {i} = {n * i}") 

multiplication_table(7)        
  








