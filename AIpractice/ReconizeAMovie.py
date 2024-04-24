# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:22:04 2024

@author: Usuario
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Simulamos un conjunto de datos de películas y sus descripciones
datos_peliculas = {
    'titulo': ['El Padrino', 'Forrest Gump', 'La Lista de Schindler', 'El Señor de los Anillos'],
    'descripcion': [
        'El envejecido patriarca de una dinastía del crimen organizado decide transferir su puesto a su hijo.',
        'La historia de un hombre con un coeficiente intelectual bajo y una vida extraordinaria.',
        'En Polonia durante la Segunda Guerra Mundial, Oskar Schindler gradualmente se preocupa por su fuerza laboral judía.',
        'Un Hobbit y sus amigos emprenden una aventura para destruir el poderoso Anillo Único.'
    ]
}

df = pd.DataFrame(datos_peliculas)



# Convertimos las descripciones de texto a una matriz de características TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['descripcion'])


# Calculamos la similitud coseno entre las películas
similitudes = linear_kernel(tfidf_matrix, tfidf_matrix)

# Función para obtener recomendaciones basadas en la similitud de contenido
def recomendar_pelicula(titulo):
    indice = df.index[df['titulo'] == titulo].tolist()[0]
    puntuaciones_similitud = list(enumerate(similitudes[indice]))
    puntuaciones_similitud = sorted(puntuaciones_similitud, key=lambda x: x[1], reverse=True)
    puntuaciones_similitud = puntuaciones_similitud[1:3]  # Obtenemos las 2 películas más similares
    indices_peliculas = [i[0] for i in puntuaciones_similitud]
    return df['titulo'].iloc[indices_peliculas]

# Probamos la función de recomendación
print(recomendar_pelicula('El Padrino'))
