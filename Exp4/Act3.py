# -*-  shopping app stores product prices: utf-8 -*-
"""
Created on Mon Mar 16 05:46:57 2026

@author: Om Gate
"""

# A shopping app stores product prices in a list. Find total bill-
"""
Created on Mon Mar 16 11:00:58 2026

@author: User
"""
# Taking list input from the user
n = int(input("Enter number of products: "))
prices = []

for i in range(n):
    num = int(input(f"Enter price of product {i+1}: "))
    prices.append(num)

# Calculating total bill
total = sum(prices)

print("Product Prices:", prices)
print("Total Bill:", total)
