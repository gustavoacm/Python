# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:29:22 2024

@author: Usuario
"""

#pandas and numpy

import pandas as pd
import numpy as np

# dictionary of lists
dict = {'id':[1, 4, np.nan, 9],
        'Age': [30, 45, np.nan, np.nan],
        'Score':[np.nan, 140, 180, 198]}
print(dict)
# creating a DataFrame
df = pd.DataFrame(dict)

#replace null values with -999
df.replace(to_replace = np.nan, value = -999)
print(df)
df.isnull().sum()