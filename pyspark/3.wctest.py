from pyspark import SparkContext
if __name__ == '__main__':
    #创建spark context
    sc = SparkContext('local[2]','wordcount')
    #通过spark context 获取rdd
    rdd1 = sc.textFile('./access.log')
    rdd2 = rdd1.flatMap(lambda line:line.split())
    rdd3 = rdd2.map(lambda x:(x,1))
    rdd4 = rdd3.reduceByKey(lambda x,y:x+y)
    print(rdd2.collect())
    print(rdd4.collect())