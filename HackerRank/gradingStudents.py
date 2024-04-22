# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:42:36 2024

@author: Usuario
"""

#practices



def gradingStudents(grades):
    for i in grades:
        if i > 37:
            nextm5 = (i // 5) * 5 + 5
            if (nextm5 - i) < 3:
                print (nextm5)
                continue
        print (i)
        continue


grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)
