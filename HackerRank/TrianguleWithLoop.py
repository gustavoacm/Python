# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:41:30 2024

@author: Usuario
"""

#practices
def staircase(n):
    for i in range(n):
        i += 1
        n -= 1
        print(n*' '+i*'#')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)