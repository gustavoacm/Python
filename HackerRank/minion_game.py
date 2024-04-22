# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:24:35 2024

@author: Usuario
"""

#after having a comperhention of the series with copilot helps 

def minion_game(string):
    vowelsStart = 0
    consonantsStart = 0
    n = len(string)
    
    for i, j in enumerate(string):
        if j.upper() in ('A','E','I','O','U'):
            vowelsStart += n -i
        else: 
            consonantsStart += n -i

    if vowelsStart > consonantsStart:
        print(f'Kevin {vowelsStart}')
    elif vowelsStart == consonantsStart:
        print('Draw')
    else: 
        print(f'Stuart {consonantsStart}')
        
minion_game('BANANA')