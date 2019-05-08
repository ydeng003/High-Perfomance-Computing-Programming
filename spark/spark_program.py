import sys
from operator import add
from pyspark import SparkContext


sc = SparkContext(appName="SparkProgram")
file1 = sc.textFile(sys.argv[1])
file2 = sc.textFile(sys.argv[2])
#Create RDDs to filter each line for the keyword Spark
spark1 = file1.filter(lambda line: "Spark" in line)
spark2 = file2.filter(lambda line: "Spark" in line)
#Perform a Word Count on each
spark1_counts = spark1.flatMap(lambda line: line.strip().split(' ')).map(lambda word: (word, 1)).reduceByKey(add)
spark2_counts = spark2.flatMap(lambda line: line.strip().split(' ')).map(lambda word: (word, 1)).reduceByKey(add)
#Join the two RDDs
spark_counts = spark1_counts.join(spark2_counts)

spark_counts.saveAsTextFile(sys.argv[3])
sc.stop()
