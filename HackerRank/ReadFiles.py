# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:35:15 2024

@author: Usuario
"""

#read files 
my_file = open('greeting.txt','r')
print(my_file.readline())
print(my_file.readline())
my_file.close()
my_file = open('greeting.txt','r')
print(my_file.read(100).splitlines())
my_file.close()

#another syntax where we do not need to close the file 
with open('friends.csv','r') as g:
    #var = g.read(100)
    friends = g.read().splitlines()
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year= int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 - year} years old')

with open('movies.txt','r') as g:
    for line in g.readlines():
        print(line)