# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:37:44 2024

@author: Usuario
"""

# lambda sort function
monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
def sort_names(name):
    return name.split(' ')[1]
#print(sort_names('John Marwood Cleese')[-1] )

monty_python.sort(key= sort_names)
print(monty_python)

monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python)

def func(n):
    return lambda a: a*n
# Functions of functions 
doubler = func(2)
print(doubler)
print(doubler(3))

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)
print(walkin_cost(2))
print(premium_cost(2))
#include outer and inner parameters
print(price_calc(1,25)(2))
#create lambda function and pass parameters 
print((lambda a,b,c: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))

#use args to include any parameter
print((lambda *args: sum(args))(2,3,4,50))