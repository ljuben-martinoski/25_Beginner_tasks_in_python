"""Find the maximum :
Write a function to find the maximum value in a list"""

data = [10, 24,3 ,6, 9, 18]

def find_maximum(numbers):
    
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
            return max_value


print("Maximum value: ", find_maximum(data))


