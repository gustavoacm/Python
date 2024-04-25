# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:38:08 2024

@author: Usuario
"""

n = int(input()) #5
arr = list(map(int, input().split())) #12 9 61 5 14
 
allint = all(isinstance(i, int) for i in arr)
anypalind = any(i == int(str(i)[::-1]) for i in arr) 
print(allint and anypalind)