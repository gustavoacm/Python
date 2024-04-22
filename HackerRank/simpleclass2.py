# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:29:04 2024

@author: Usuario
"""

# Definimos una clase simple
class Saludo:
    def decir(self):
        return "Hola"

# Instancia de la clase
saludo = Saludo()

# Método original
print(saludo.decir())  # Salida: Hola

# Definimos una nueva función que queremos "inyectar"
def decir_adios(self):
    return "Adiós"

# Aplicamos monkey patching al método 'decir'
Saludo.decir = decir_adios

# El método ha sido modificado
print(saludo.decir())  # Salida: Adiós