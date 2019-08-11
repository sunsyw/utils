from pyspark import SparkContext


# 用户个数
if __name__ == '__main__':
    #创建spark context
    sc = SparkContext('local[2]','uvcount')
    rdd1 = sc.textFile('./access.log')
    rdd2 = rdd1.map(lambda x:x.split())#.map(lambda x:x[0])
    rdd2_ = rdd2.map(lambda x:x[0])
    rdd3 = rdd2_.distinct().map(lambda x:('uv',1))
    rdd4 = rdd3.reduceByKey(lambda a,b:a+b)

    print(rdd1.collect())
    print(rdd2.collect())
    print(rdd2_.collect())
    print(rdd3.collect())
    print(rdd4.collect())