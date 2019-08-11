from pyspark import SparkContext
def func(x,y):
    result = x-y
    return result
if __name__ == '__main__':
    #创建spark context
    sc = SparkContext('local[2]','topncount')
    rdd1 = sc.textFile('./access.log')
    # 按照空格切分 取出列表长度大于10的
    rdd0 = rdd1.map(lambda x: x.split()).filter(lambda x: len(x) > 10)
    rdd2 = rdd0.map(lambda x:(x[10],1))
    rdd3 = rdd2.reduceByKey(lambda a,b:a+b)  # (x:2)
    rdd4 = rdd3.sortBy(lambda x:x[1],ascending=False).filter(lambda x:len(x[0])>6)
    result = rdd4.take(1)
    print(rdd0.collect())
    print(rdd2.collect())
    print(rdd3.collect())
    print(rdd4.collect())
    print(result)
    # rdd1 = sc.parallelize([1,2,3,4,5,6])
    # result = rdd1.reduce(func)
    # print(result)