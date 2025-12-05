"""6. Palindrome Checker: 
Check if a given string is a palindrome.
A palindrom is a word that reads the same forward and backward"""


text = input("Enter a word: ")

text = text.lower()

reversed_text = ""
# create a reversed version manualy
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
    # comparing witht he original
    if text == reversed_text:
        print("Its a palindrome.")
    else:
        print("It is NOT a palindrome.")

print("=================================================================================================")


def is_palindrome(s: str) -> bool:
    s = s.lower()  # normalize
    left = 0
    right = len(s) - 1

    # Compare characters from both ends
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Examples
print(is_palindrome("Radar"))      # True
print(is_palindrome("Warehouse"))  # False


