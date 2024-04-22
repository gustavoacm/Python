# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:39:45 2024

@author: Usuario
"""

#timeit and performance 

import timeit

print('Performance and Timeit module')
# Experiment with sieve of Eratosthenes
def test1():
    output = [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(output)

def test2():
    output = [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
    return(output)

def test3():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    #print(primes)
    return(primes)

def test4():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    #print(primes)
    return(primes)

print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))
print(timeit.timeit('test4()', globals=globals(), number=10))
