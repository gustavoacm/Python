# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

print('hola mundo')

#camelcase whenever there isn't a number 
def solve(s):
    for i in s.split():
        if not any(c.isdigit() for c in i):
            s = s.replace(i, i.title())
    return s

if __name__ == '__main__':

    s = 'hello   world  lol'#input()

    result = solve(s)

    print(result)