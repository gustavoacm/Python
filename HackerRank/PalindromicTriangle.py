# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:30:29 2024

@author: Usuario
"""

#palindromic triangle
for i in range(1,int(input())+1):
    print(*range(1, i + 1), *range(i - 1, 0, -1), sep="")

#for i in range(1,int(input())+1): 
#    print(((10 ** i - 1) // 9) ** 2)5