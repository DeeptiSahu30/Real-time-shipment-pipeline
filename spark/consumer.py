from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json

from schema import shipment_schema
from transformations import transform

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("ShipmentTrackingConsumer")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        ",".join([
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.6",
            "org.apache.hadoop:hadoop-aws:3.3.4",
            "com.amazonaws:aws-java-sdk-bundle:1.12.262"
        ])
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# Configure S3
hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()

hadoop_conf.set(
    "fs.s3a.impl",
    "org.apache.hadoop.fs.s3a.S3AFileSystem"
)

hadoop_conf.set(
    "fs.s3a.aws.credentials.provider",
    "com.amazonaws.auth.profile.ProfileCredentialsProvider"
)

hadoop_conf.set(
    "fs.s3a.endpoint",
    "s3.ap-south-1.amazonaws.com"
)

# Read from Kafka
kafka_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:29092")
    .option("subscribe", "shipment-events")
    .option("startingOffsets", "latest")
    .load()
)

# Convert Kafka value to string
json_df = kafka_df.selectExpr("CAST(value AS STRING)")

# Parse JSON
parsed_df = (
    json_df
    .select(
        from_json(
            col("value"),
            shipment_schema
        ).alias("data")
    )
    .select("data.*")
)

# Apply transformations
final_df = transform(parsed_df)

# Write to S3
query = (
    final_df.writeStream
    .format("parquet")
    .outputMode("append")
    .option(
        "path",
        "s3a://shipment-pipeline-deepti-2026/processed_new/"
    )
    .option(
        "checkpointLocation",
        "s3a://shipment-pipeline-deepti-2026/checkpoints/shipment-stream-v2/"
    )
    .start()
)

print("Shipment Streaming Started...")

query.awaitTermination()
