# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:38:16 2024

@author: Usuario
"""

#comperhension list 

new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))
print(new_list)

new_list = [(letter+'M',num*3) if num % 2 == 0 else num for letter in'GC' for num in range(8)]
print(new_list)