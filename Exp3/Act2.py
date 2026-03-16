# -*- Calculate Simple Intrest-8 -*-
"""
Created on Mon Feb 16 10:29:52 2026

@author: Om Gate
"""
def simple_intrest(principle,rate,time):
 si = (principle*rate*time)/100
 return si
# taking Input From The User 
p = float(input("Enter Principle Amount; "))    
r = float(input("Enter Rate Intrest:"))
t = float(input("Enter Time In Years;"))
#Function Call  
intrest=simple_intrest(p,r,t)
print("Simple Intrest Is:",intrest)
