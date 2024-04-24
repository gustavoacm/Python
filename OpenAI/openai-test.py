# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:44:26 2024

@author: Usuario
"""

from openai import OpenAI

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente poético, hábil en explicar conceptos de programación complejos con un toque creativo."},
        {"role": "user", "content": "Compon un poema que explique el concepto de recursión en programación."},
    ]
)

print(completion.choices[0].message)
