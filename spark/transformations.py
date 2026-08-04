from pyspark.sql.functions import (
    col,
    to_timestamp,
    current_timestamp,
    when,
    unix_timestamp,
    round
)


def transform(df):
    """
    Apply data cleaning and transformation logic
    for shipment analytics pipeline.
    """

    # --------------------------------------------------
    # 1. Remove duplicate shipment events
    # --------------------------------------------------
    df = df.dropDuplicates(
        ["shipment_id", "event_time"]
    )


    # --------------------------------------------------
    # 2. Remove records with missing mandatory fields
    # --------------------------------------------------
    df = (
        df.filter(col("shipment_id").isNotNull())
          .filter(col("status").isNotNull())
          .filter(col("event_time").isNotNull())
    )


    # --------------------------------------------------
    # 3. Convert timestamp columns
    # --------------------------------------------------
    df = (
        df.withColumn(
            "created_at",
            to_timestamp(
                col("created_at"),
                "yyyy-MM-dd HH:mm:ss"
            )
        )
        .withColumn(
            "estimated_delivery",
            to_timestamp(
                col("estimated_delivery"),
                "yyyy-MM-dd HH:mm:ss"
            )
        )
        .withColumn(
            "event_time",
            to_timestamp(
                col("event_time"),
                "yyyy-MM-dd HH:mm:ss"
            )
        )
    )


    # --------------------------------------------------
    # 4. Calculate shipment age in hours
    # --------------------------------------------------
    df = df.withColumn(
        "shipment_age_hours",
        round(
            (
                unix_timestamp(current_timestamp())
                -
                unix_timestamp(col("created_at"))
            ) / 3600,
            2
        )
    )


    # --------------------------------------------------
    # 5. Create delayed shipment flag
    # --------------------------------------------------
    df = df.withColumn(
        "is_delayed",
        when(
            col("delay_reason").isNotNull(),
            True
        ).otherwise(False)
    )


    # --------------------------------------------------
    # 6. Rename columns for Athena / Power BI layer
    # --------------------------------------------------
    df = (
        df.withColumnRenamed(
            "origin_city",
            "origin"
        )
        .withColumnRenamed(
            "destination_city",
            "destination"
        )
        .withColumnRenamed(
            "weight_kg",
            "weight"
        )
        .withColumnRenamed(
            "created_at",
            "shipment_date"
        )
        .withColumnRenamed(
            "estimated_delivery",
            "delivery_date"
        )
    )


    # --------------------------------------------------
    # 7. Return transformed dataframe
    # --------------------------------------------------
    return df