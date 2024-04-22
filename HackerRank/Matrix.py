# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:40:42 2024

@author: Usuario
"""

#matrix 
n = int(input().strip())
arr = []
def diagonalDifference(arr):
    d1 = []
    d2 = []
    for i, Vlist in enumerate(arr):
        for j, Value in enumerate(Vlist): 
            if i == j:
                d1.append(Value)
            if (i + j) == (len(arr) - 1):
                d2.append(Value)
    return abs(sum(d1) - sum(d2))
        
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(diagonalDifference(arr) )