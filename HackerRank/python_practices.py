# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:26:59 2024

@author: Usuario
"""

#python practices
A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
B = A.copy()
C = A
D = ['W', 'X', 'Y', 'Z']
A.append(4)
A.insert(7,'J')
#A.clear()
D.extend(A)
print(A,B,C)
print(A.count(4))
print(D)
print(A.index('G') + 1)
A.pop()
A.remove('A')
print(A)
A.reverse()
print(A)
A.sort()
print(A)
T = (1, 2, 3, 4, 5, 6, 7)
print(sum(T) )
S = {1, 2, 3, 4, 5, 6, 7}
U = {1, 2, 3, 8, 9, 10}
S.update((1, 8))
S.discard(1)
S.remove(2)
print(S)
print(S.union(U))
print(S.intersection(U))
print(S.difference(U))
print(U.difference(S))
print(U.symmetric_difference(S))