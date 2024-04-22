# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:37:13 2024

@author: Usuario
"""

#zip / unzip

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
# with dict function 
a_dict = dict(zip(keys,values))
print(a_dict)
#with comperhensions dictionary 
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)

a,b = list(new_dict.keys()),list(new_dict.values())
print(a)
print(b)

c,d = zip(*new_dict.items())
print(list(c))
print(list(d))