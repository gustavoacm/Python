# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:42:54 2024

@author: Usuario
"""

#python course Math tutor
#import modules
from random import randrange as r 
from time import time as t
# ask how many questions user wants
no_questions = int(input('How many questions do you want?: '))
max_num =int(input('Highest number used in practice?: '))
#set score start at zero
score = 0
answer_list = []
#loop through number of questions

for _ in range(no_questions):
    num1,num2 = r(1,max_num+1),r(1,max_num+1)
    ans = num1 * num2
    start = end = 0
    start = t()
    u_ans =int(input(f'{num1} X {num2} = '))
    end = t()
    # An history of the answers 
    answer_list.append(f'{num1} X {num2} = {ans} you: {u_ans} in {round(end-start,1)} seconds')
    if u_ans == ans:
        score += 1
print(f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions*100)}%) correct!')
for a in answer_list:
    print(a)
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score 