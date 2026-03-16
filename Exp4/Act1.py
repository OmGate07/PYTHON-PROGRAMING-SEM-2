# to find the sum and average of elements in a list Flowchart:
"""
Created on Mon Mar 16 10:43:58 2026
@author: Om Gate
"""

# Taking list input from the user
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Calculating sum and average
total = sum(numbers)
average = total / n if n > 0 else 0

print("List:", numbers)
print("Sum of elements:", total)
print("Average of elements:", average)
