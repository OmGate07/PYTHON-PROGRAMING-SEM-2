# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 04:53:07 2026

@author: Om Gate
"""

# Shop inventory dictionary
inventory = {
    "Rice": 50,
    "Sugar": 30,
    "Oil": 20
}

# Display current inventory
print("Current Inventory:")
for item, quantity in inventory.items():
    print(item, ":", quantity)

# Add new stock
item_name = input("\nEnter item name to add: ")
item_quantity = int(input("Enter quantity to add: "))

# Update inventory
if item_name in inventory:
    inventory[item_name] += item_quantity
else:
    inventory[item_name] = item_quantity

# Display updated inventory
print("\nUpdated Inventory:")
for item, quantity in inventory.items():
    print(item, ":", quantity)
