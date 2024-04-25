# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:30:15 2024

@author: Usuario
"""

from itertools import product

A = list(map(int, input().split()))# space separated interger
B = list(map(int, input().split()))# space separated interger

print (*product(A, B))