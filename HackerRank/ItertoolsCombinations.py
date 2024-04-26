# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:10:06 2024

@author: Usuario
"""

from itertools import combinations
S, k = input().split()
k = int(k)
S = sorted(S)
  
for i in range(1, k+1):
    for combined in combinations(S, i):
        print("".join(combined))