# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:49:58 2024

@author: Usuario
"""

#In Python, functions that extend or modify the functionality 
#of other functions or methods are called decorators.

#Decorators are widely used in Python for tasks such as exception 
#handling, execution time measurement, authentication, and data 
#validation, among others.

def mi_decorador(funcion_original):
    def funcion_modificada(*args, **kwargs):
        print("Antes de llamar a la función original")
        resultado = funcion_original(*args, **kwargs)
        print("Después de llamar a la función original")
        return resultado
    return funcion_modificada


@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")