import findspark
findspark.init() 
from pyspark.sql import SparkSession
print("hello")
spark = SparkSession.builder.appName('Python Spark SQL basic example').config('spark.some.config.option', 'some-value').getOrCreate()

### Create json file using spark
# sparkContext로 객체 생성
sc = spark.sparkContext
print("bye")
# json 파일 읽어들이기
path = "C://spark-2.4.8-bin-hadoop2.7//examples//src//main//resources//people.json"
peopleDF = spark.read.json(path)

# printSchema()로 json파일의 스키마 형태 볼수 있음
peopleDF.printSchema()
print("bye2")