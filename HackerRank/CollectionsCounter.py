# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:20:32 2024

@author: Usuario
"""
from collections import Counter

X = int(input())
ShoesSizes = list(map(int, input().split()))
ShoesSizes = Counter(ShoesSizes)
N = int(input())
SizePrice = []
TotalPrice = 0
for _ in range(N):
    SizePrice = input().split()
    size = int(SizePrice[0])
    price = int(SizePrice[1])
    inventory = int(ShoesSizes.get(size, 0))
    if size in ShoesSizes.keys() and inventory != 0:
        inventory -= 1
        ShoesSizes[size] = inventory
        TotalPrice += price
print(TotalPrice)