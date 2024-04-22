# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:38:52 2024

@author: Usuario
"""

#comperhension dictionary 
movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']

# give me a dict('movies': year) for each movies, year in zip(movies, year)
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
print(new_dict)

n1 =[[name + "s favorite movie was " + movie + " from " + str(yr)] for name,movie,yr in zip(names,movies,year) if yr < 1981 ]
print(n1)