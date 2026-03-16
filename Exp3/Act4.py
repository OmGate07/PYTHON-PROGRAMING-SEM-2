# -*-calculate total stairs climbed -*-
"""
Created on Mon Feb 16 10:09:34 2026

@author: Om Gate
"""
# Recursive function to calculate total stairs climbed

def count_stairs(steps):
    if steps == 0:
        return 0
    else:
        return 1 + count_stairs(steps - 1)

# Taking input from user
total_steps = int(input("Enter number of steps climbed: "))

# Function call
result = count_stairs(total_steps)

print("Total stairs climbed:", result)
