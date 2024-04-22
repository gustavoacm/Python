# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:33:39 2024

@author: Usuario
"""

def ejemplo(*args, **kwargs):
    print("Argumentos posicionales (args):", args)
    print("Argumentos de palabras clave (kwargs):", kwargs)

# Llamada con argumentos posicionales y de palabras clave
ejemplo(1, 2, 3, nombre="Juan", edad=30)
