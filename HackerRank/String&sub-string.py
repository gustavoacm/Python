# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:48:30 2024

@author: Usuario
"""

#practices string and sub-string
string = 'ABCDCDC'
sub_string = 'CDC'
print(sum(1 for i in range(len(string)) if string.startswith(sub_string, i)))