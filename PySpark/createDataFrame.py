# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:16:35 2024

@author: Usuario
"""

#pyspark
import findspark
findspark.init()

#pyspark
from pyspark.sql import SparkSession
#create a spark session 
spark = SparkSession.builder.getOrCreate()

#pyspark data frame

data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]

df = spark.createDataFrame(data = data, schema = columns)
df.printSchema()
df.show()