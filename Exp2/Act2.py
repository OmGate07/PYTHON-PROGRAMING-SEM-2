#  find the factorial of numbers using loops
"""
Created on Tue Feb 10 12:56:58 2026

@author: Om Gate
"""
n =int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact = fact *i
    
print("factorial:",fact)
