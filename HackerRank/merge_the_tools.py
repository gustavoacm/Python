# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:25:04 2024

@author: Usuario
"""

def merge_the_tools(string, k):
    rlist = list()
    for i in range(0,len(string),k):
        result = ''
        for letter in string[i:i+k]:
            if letter not in result:
                result += letter
        rlist.append(result)
    print('\n'.join(rlist))
    
        

merge_the_tools('AABCAAADA', 3)