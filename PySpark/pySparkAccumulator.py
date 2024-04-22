# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:32:09 2024

@author: Usuario
"""

#pyspark
import findspark
findspark.init()

#PySpark Accumulator
from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()

accum=spark.sparkContext.accumulator(0)
rdd=spark.sparkContext.parallelize([1,2,3,4,5])
rdd.foreach(lambda x:accum.add(x))
print(accum.value) #Accessed by driver