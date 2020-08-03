from pyspark import SparkContext

sc = SparkContext("local", "Mapper1")
rdd1 = sc.textFile("100west.txt")
rdd2 = rdd1.flatMap(lambda fila: fila.split())
rdd3 = rdd2.map(lambda palabra: (palabra, 1))
rdd4 = rdd3.reduceByKey(lambda x, y: x + y)
rdd4.saveAsTextFile("output1")
