# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:09:31 2024

@author: Usuario
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S, k = input().split()  
k = int(k)
S = sorted(permutations(S, k)) 
print( '\n'.join([''.join(i) for i in S]))