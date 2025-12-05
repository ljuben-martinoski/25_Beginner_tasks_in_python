"""Fibonacci Sequence(short explanation what is Fibonacci sequence:
In mathematics, the Fibonacci sequence is a sequence in which each element is the sum of the two elements that precede it. 
Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn . 
Many writers begin the sequence with 0 and 1, although some authors start it from 1 and 1[1][2] and some 
(as did Fibonacci) from 1 and 2. Starting from 0 and 1, the sequence begins
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 14)), 
The task here is generate teh first n numbers in the Fibonacci sequence."""

# seting a variable n of how many numbers we want in the fibonacci sequence(you can choose any number as you want)
n = 45

fi_sequenze = [0, 1] # starting the sequenze with the first fibonacci numbers

# while list in withch we keep adding numbers until we reach n(the wanted numbers of fibonaci numbers)
while len(fi_sequenze) < n:
    #the next number is the sum of the last two nubers
    next_number = fi_sequenze[-1] + fi_sequenze[-2] # here we are takiong the last element of the list 
    # and we are adding withn the secon to the last element of the list.
    fi_sequenze.append(next_number) # we are appending the next_number to the fi_sequenze

#showing the result
print("The first ", n, "Fibonacci numbers are: ",  fi_sequenze)

#another way to solve this

m = 39  # same as n in the previous example

fib_seq = [0, 1] # starting the sequenz with the first fibonacci numbers

# for loop to add the next numbers,seting the numbers from the range 2 until the desired number that is given by m
for i in range(2, m):
    next_number = fib_seq[i-1] + fib_seq[i-2]#  here we are taking the number just before position i([i-1]), 
# and taking the second number before i([i-2]), and then wi are adding them together.
    fib_seq.append(next_number)   #   here we are appending the numbers to the fi_seq

print("The first", m, "Fibonacci numbers are: ", fib_seq)    