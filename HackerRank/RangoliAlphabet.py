# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:23:31 2024

@author: Usuario
"""

#alphabet rangoli
import string
size = 10

end = size -1
nAlph = []
alphabets = list(sorted(set(string.ascii_letters.lower())))
for _ in range(end):
    nAlph.append(alphabets[end])
    end -= 1
for i in range(size):
    nAlph.append(alphabets[i])

middleGraph = '-'.join(nAlph) 

length = len(middleGraph)
#remove letter a 
nAlph.pop(nAlph.index('a'))
#create the list of alph rangoli based on middleGraph
axes = []
for i in range(len(nAlph)): 
    nAlph.pop(len(nAlph)//2)
    if len(nAlph) % 2 != 0:
        axes.append(tuple(nAlph))
# print the graph: 
#upper graph        
for i in reversed(range(len(axes))):
    print('-'.join(axes[i]).center(length,'-'))
#center graph
print(middleGraph)
#button graph
for i in range(len(axes)):
    print('-'.join(axes[i]).center(length,'-'))
