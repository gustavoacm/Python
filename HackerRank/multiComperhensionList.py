# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:46:28 2024

@author: Usuario
"""

#hacker practice
x = 1
y = 1
z = 2
n = 3
matrix = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) == n]

print(matrix)
