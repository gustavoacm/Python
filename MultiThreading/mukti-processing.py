# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:58:10 2024

@author: Usuario
"""

from multiprocessing import Pool

def f(x):
    return x * x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))  # Salida: [1, 4, 9]