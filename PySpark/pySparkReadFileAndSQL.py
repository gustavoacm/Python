# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:34:30 2024

@author: Usuario
"""
import time
#pyspark
import findspark
findspark.init()
time.sleep(15)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
#create a session in spark
spark = SparkSession.builder.appName("ReadData").getOrCreate()
#read data from a csv file 
df = spark.read.csv("..\DataFiles\PAZ.csv", header=True, inferSchema=True, sep=";")
#validate data 
df_validated = df.filter(col("Unit") == "People")

#create temp table 
df_validated.createOrReplaceTempView("validatedCSV")

#SQL query to get result 
result = spark.sql("SELECT * FROM validatedCSV")

#show result 
result.show()

#close spark session 
spark.stop()