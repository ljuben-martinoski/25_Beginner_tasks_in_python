"""
Simple Interest Calculator: 
Calculate simple interest given principal, rate, and time. 
"""

principal = float(input(" Enter the principal amount: "))
rate = float(input("Enter the interest rate(in %): "))
time = float(input("Enter the time(in years): "))

# simple interesret formula
# SI = (Principal * rate * time) / 100
simple_interest = (principal * rate * time ) / 100

print("Simple Interest =", simple_interest)