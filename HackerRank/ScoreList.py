# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:45:07 2024

@author: Usuario
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

scoreList = [sc for nam, sc in students]
result = list(filter(lambda x: x - min(scoreList) != 0,scoreList))
secondScore = [nam for nam, sc in students if sc == min(result)]
secondScore.sort()
print('\n'.join(secondScore))
[print(i) for i in secondScore]
print(''.join(secondScore))
[print(i, end=' ') for i in secondScore]