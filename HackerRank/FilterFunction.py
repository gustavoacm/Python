# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:47:01 2024

@author: Usuario
"""

#hacker practice
arr = [2, 3, 6, 6, 5]
result = list(filter(lambda x: max(arr) - x != 0,arr))
print(max(result))