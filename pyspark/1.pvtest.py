from pyspark import SparkContext


# 总访问量
if __name__ == '__main__':
    #创建spark context
    sc = SparkContext('local[2]','pvcount')
    rdd1 = sc.textFile('./access.log')
    result = rdd1.map(lambda x:('pv',1)).reduceByKey(lambda a,b:a+b).collect()
    print(result)