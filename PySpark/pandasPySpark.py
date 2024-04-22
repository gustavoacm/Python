# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:29:41 2024

@author: Usuario
"""

#pyspark
import findspark
findspark.init()

import pyspark
import pandas as pd
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.getOrCreate()

# Create a sample DataFrame
df_pd = pd.DataFrame({
    'integers': [1, 2, 3],
    'floats': [-1.0, 0.5, 2.7],
    'integer_arrays': [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
})

# Convert pandas DataFrame to Spark DataFrame
df = spark.createDataFrame(df_pd)

# Show the DataFrame
df.createOrReplaceTempView("PERSON_DATA")
df2 = spark.sql("SELECT * from PERSON_DATA")
#df2.printSchema()
df2.show()
