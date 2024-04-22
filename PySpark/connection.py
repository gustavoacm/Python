# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:13:43 2024

@author: Gustavo Cabrera
"""

import findspark
findspark.init()

from pyspark.sql import SparkSession
#create a spark session 
spark = SparkSession.builder.getOrCreate()
#using parallelize to create a rdd from a list
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
rdd = spark.sparkContext.parallelize(dataList)
print(rdd)
print("From local[5] : "+str(rdd.getNumPartitions()))
#using textFile to create a rdd from a text file
rdd2 = spark.sparkContext.textFile('greeting.txt')
print(rdd2)
rdd3 = spark.sparkContext.wholeTextFiles('*')
print(rdd3)
#RDD operations Transformations and Actions, transformations are lazy because require an action to execute, while a transformation 
#creates another RDD an Action triggers computation. 

# some transformations are: flatMap(), map(), reduceByKey(), filter(), sortByKey()
# some Actions are: count(), collect(), first(), max(), reduce()