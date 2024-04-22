# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:41:44 2024

@author: Usuario
"""

#pratices
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)