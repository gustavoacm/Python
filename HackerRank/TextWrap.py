# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:49:24 2024

@author: Usuario
"""

#practice text wrap

import textwrap

text = (
    "The single-responsibility principle (SRP) is a computer programming principle "
    "that states that every class in a computer program should have responsibility over "
    "a single part of that program's functionality, which it should encapsulate. "
    "All of the module's, class' or function's services should be narrowly aligned with that responsibility"
)

lines = '\n'.join(textwrap.wrap(text.replace('\n',''), 70))
print(lines)
