"""Substring Finder:
Check if one string is a substring of another."""


# variable main_text fo the user to inpput
main_text = input("Enter the main text: ")
# variable sub_text for the user to input
sub_text = input("Enter the substring: ")
# if loop to go through the text.
if sub_text in main_text:
    print("Yes, the substirng is found.")
else:
    print("No, the substring is NOT found")


print("===========================================================================================================") 



# also a more advanced style

# defining a funktion with a name is_substring, with parameters text and patern as strings, and telling python to return bool.
def is_substring(text: str, pattern: str) -> bool:
    return pattern in text

print(is_substring("FastAPI warehouse app", "warehouse")) # True
print(is_substring("Logistic App", "Driver"))  # False

