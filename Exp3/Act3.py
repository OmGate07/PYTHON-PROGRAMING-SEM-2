# -*-Rows Pattern -*-
"""
Created on Mon Feb 16 10:09:34 2026

@author: Om Gate
"""
# Program to display multiplication tables from 1 to 10

for num in range(1, 11):
    print("Multiplication Table of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    print()   # Blank line for separation
