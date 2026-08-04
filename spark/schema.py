from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    IntegerType,
)

shipment_schema = StructType([
    StructField("shipment_id", StringType(), True),
    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("customer_name", StringType(), True),

    StructField("origin_city", StringType(), True),
    StructField("destination_city", StringType(), True),

    StructField("warehouse", StringType(), True),
    StructField("carrier", StringType(), True),

    StructField("weight_kg", DoubleType(), True),
    StructField("shipping_cost", DoubleType(), True),

    StructField("status_index", IntegerType(), True),
    StructField("status", StringType(), True),

    StructField("delay_reason", StringType(), True),

    StructField("created_at", StringType(), True),
    StructField("estimated_delivery", StringType(), True),
    StructField("event_time", StringType(), True)
])