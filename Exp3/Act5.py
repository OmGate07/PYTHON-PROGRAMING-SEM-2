# -*- A ticket booking system -*-
"""
Created on Mon Mar 16 05:02:55 2026

@author: Om Gate
"""
# Program to display seat pattern in a ticket booking system

rows = 5
seats_per_row = 5

for row in range(1, rows + 1):
    print("Row", row, ":", end=" ")
    for seat in range(1, seats_per_row + 1):
        print("S" + str(seat), end=" ")
    print()
