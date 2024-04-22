# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:39:21 2024

@author: Usuario
"""

#randomness

import random, string
for i in range(5):
    print(random.random())

for i in range(5):
    print(random.uniform(7,8))

for i in range(5):
    print(random.randint(7,14))

for i in range(5):
    print(random.randrange(1,7,2))

friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.sample(friends_list,5))
random.shuffle(friends_list)
print(friends_list)

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
print(letters_numbers)