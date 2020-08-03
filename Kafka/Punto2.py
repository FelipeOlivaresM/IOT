from pyspark import SparkContext

sc = SparkContext("local", "Mapper2")
rdd1 = sc.textFile("price_paid_records.csv")
rdd2 = rdd1.map(lambda fila: ((((fila.split(",")[2]).split(" ")[0]).split("-")[0]), 1))
rdd3 = rdd2.reduceByKey(lambda x, y: x + y)
rdd3.saveAsTextFile("output2")
