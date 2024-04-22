# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:36:23 2024

@author: Usuario
"""

#Classes

class Movie:
    def __init__(self,title,year,score,seen):
        self.title = title
        self.year = year
        self.score = score
        self.seen = seen 

    def printV(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.score)
        print("I have seen it: ", self.seen)
class Cinema(Movie):
    def play(self):
        print(f'Reproduce {self.title}')

movie1 = Cinema('Dead Poets society',1989,10,True)

print(movie1.title)

movie1.play()