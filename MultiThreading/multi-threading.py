# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:55:03 2024

@author: Usuario
"""

#multi-threading
import threading

def imprimir_numeros():
    for i in range(1, 6):
        print(f"Número: {i}")

def imprimir_letras():
    for letra in "ABCDE":
        print(f"Letra: {letra}")



# Creamos dos hilos
hilo_numeros = threading.Thread(target=imprimir_numeros)
hilo_letras = threading.Thread(target=imprimir_letras)

# Iniciamos los hilos
hilo_numeros.start()
hilo_letras.start()

# Esperamos a que ambos hilos terminen
hilo_numeros.join()
hilo_letras.join()

print("¡Terminado!")
