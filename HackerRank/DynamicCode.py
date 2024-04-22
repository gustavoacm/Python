# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:33:15 2024

@author: Usuario
"""

# asignar elementos (iterables o secuencias) de forma dinamica en python 
from statistics import mean

A, B = map(int, input().split())
List = []
for i in range(B):
    List.append(tuple(map(float, input().split())))
#se hace uso del operador * para desempaquetar  
for scores in zip(*List):
    print(mean(scores))