# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:18:56 2024

@author: Usuario
"""

from openai import OpenAI

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="256x256",
  quality="standard",
  n=1,
)

image_url = response.data[0].url