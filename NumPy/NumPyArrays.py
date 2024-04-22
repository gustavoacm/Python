# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:03:39 2024

@author: Usuario
"""

#Numpy 
import numpy as np 
a = np.arange(15).reshape(3, 5)
#matrix
print('matrix')
print(a)
#matrix element type 
print('matrix element type')
print(a.dtype.name)
#The size in bytes of each element
print('matrix size in bytes of each element')
print(a.itemsize)
#matrix dimension
print('matrix dimension')
print(a.ndim)
#matrix shape 
print('matrix shape')
print(a.shape)
#matrix number of elements 
print('matrix number of elements')
print(a.size)
#type of data
print('type of data')
print(type(a))
#matrix of zeros
print('matrix of zeros')
print( np.zeros((3, 4)) )
#matrix of ones
print('matrix of ones')
print(np.ones((3, 4), dtype=np.int16) )
#matrix of random
print('matrix of random')
print(np.empty((2, 3)))
#basic operators on arrays apply elementwise
b = np.arange(15).reshape(3, 5)
c = a - b
print(c)
print(b**2)
print(10 * np.sin(a))
print(a > 7)
print(a * b)
a += b
print(a)
print('Sum of each column')
print(b.sum(axis=0))
#
print('Min of each row')
print(b.min(axis=1) )
# cumulative sum along each row
print('cumulative sum along each row')
print(b.cumsum(axis=1))
# cumulative sum along each column
print('cumulative sum along each column')
print(b.cumsum(axis=0))
print(np.exp(b))
print(np.add(a, b))
#indexing, slicing and iterating
print(b[2])
print(b[2][3])
print(a[::-1])  # reversed a
for row in b.flat:
    print(row)