# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:35:44 2024

@author: Usuario
"""

#try except
try:
    num=int(input('Enter a number: '))
    num1 = 30/num
except ZeroDivisionError as err:
    print(err,'is an infinity value!')
except ValueError as err: 
    print(err,'is Invalid!')
except:
    print(err,'Invalid Input!')
else: 
    print("30 divided by",num, "is: ", num1)
finally: 
    print("**Thank you for playing!**")