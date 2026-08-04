from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Read Parquet") \
    .getOrCreate()

df = spark.read.parquet("/opt/project/data/output")

print("\n===== SCHEMA =====")
df.printSchema()

print("\n===== SAMPLE DATA =====")
df.show(20, truncate=False)

spark.stop()