# 🚚 Real-Time Shipment Tracking Pipeline

> An end-to-end real-time data engineering pipeline that streams shipment events using Apache Kafka, processes them with PySpark Structured Streaming, stores optimized Parquet files in Amazon S3, and enables serverless analytics using Amazon Athena.

---

## 📖 Overview

This project simulates a real-world logistics system where shipment events are continuously generated, streamed, processed, and stored for analytical querying.

The pipeline demonstrates how modern data engineering technologies work together to build scalable streaming applications.

---

# 🏗️ Architecture

![Architecture]
<img width="1536" height="1024" src=["https://chatgpt.com/s/m_6a743a37f5808191b919f22499e24253"] />

---

# 🔄 Pipeline Workflow

```text
                📦 Shipment Generator
                (Python + Faker)
                       │
                       ▼
              🚀 Apache Kafka
                       │
                       ▼
       ⚡ PySpark Structured Streaming
                       │
       Data Cleaning & Transformation
                       │
                       ▼
        🗂️ Amazon S3 (Parquet Files)
                       │
                       ▼
          📚 AWS Glue Data Catalog
                       │
                       ▼
            🔍 Amazon Athena
                       │
                       ▼
            📊 SQL Analytics
```

---

# 🚀 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Streaming Platform | Apache Kafka |
| Processing Engine | Apache Spark Structured Streaming |
| Cloud Storage | Amazon S3 |
| Metadata Catalog | AWS Glue Data Catalog |
| Query Engine | Amazon Athena |
| Storage Format | Apache Parquet |
| Containerization | Docker & Docker Compose |
| Data Generation | Faker |
| Version Control | Git & GitHub |

---

# ✨ Key Features

- 📦 Real-time shipment event generation
- 🚀 Kafka-based message streaming
- ⚡ Stream processing using PySpark Structured Streaming
- 🧹 Data cleaning and validation
- 🔄 Duplicate record removal
- ⏰ Shipment age calculation
- 🚚 Delayed shipment identification
- 💾 Parquet storage optimization
- ☁️ Amazon S3 Data Lake
- 🔍 Interactive SQL analytics with Amazon Athena
- 🐳 Dockerized development environment

---

# 📷 Project Demo

## 🐳 Docker Containers

All required containers running successfully.

![Docker Containers](Screenshots/docker-containers.png)

---

## 🚀 Kafka Topic

Shipment topic successfully created.

![Kafka Topic](Screenshots/kafka-topic.png)

---

## 📦 Shipment Producer

Real-time shipment events continuously published to Kafka.

![Producer](Screenshots/producer.png)

---

## ⚡ Spark Structured Streaming

Real-time data ingestion, transformation, and storage into Amazon S3.

![Spark Streaming](Screenshots/spark-streaming.png)

---

## ☁️ Amazon S3 Output

Processed shipment records stored in Parquet format.

![S3 Output](Screenshots/s3-output.png)

---

## 🔍 Amazon Athena

Querying shipment data directly from Amazon S3.

![Athena](Screenshots/athena-query.png)

---

# ⚙️ Data Processing

The Spark streaming pipeline performs the following transformations before storing data:

### ✅ Data Cleaning

- Removes duplicate shipment events
- Filters invalid records
- Handles missing values
- Converts timestamp fields into Spark Timestamp format

### ✅ Feature Engineering

- Shipment Age (Hours)
- Delay Flag (`is_delayed`)
- Standardized timestamp columns

### ✅ Storage Optimization

Processed data is written in **Apache Parquet** format to improve:

- Query performance
- Compression
- Storage efficiency

---

# 📊 Sample SQL Queries

### Total Shipments

```sql
SELECT COUNT(*)
FROM shipment_processed;
```

### Delayed Shipments

```sql
SELECT *
FROM shipment_processed
WHERE is_delayed = true;
```

### Shipments by Carrier

```sql
SELECT
    carrier,
    COUNT(*) AS total_shipments
FROM shipment_processed
GROUP BY carrier;
```

### Average Shipping Cost

```sql
SELECT AVG(shipping_cost)
FROM shipment_processed;
```

---

# ▶️ Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/DeeptiSahu30/Real-time-shipment-pipeline.git
```

---

## 2️⃣ Start Docker Services

```bash
cd docker

docker compose up -d
```

---

## 3️⃣ Start Shipment Producer

```bash
python producer/producer.py
```

---

## 4️⃣ Start Spark Consumer

```bash
docker exec -it spark bash

cd /opt/project/spark

/opt/spark/bin/spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.6,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 \
consumer.py
```

---

## 5️⃣ Query Using Athena

Execute SQL queries on the **shipment_processed** external table to analyze shipment data.

---

# 🎯 Skills Demonstrated

- Python
- SQL
- Apache Kafka
- Apache Spark Structured Streaming
- ETL Pipeline Development
- Data Validation & Transformation
- Amazon S3
- AWS Glue Data Catalog
- Amazon Athena
- Docker
- Git & GitHub
- Real-Time Data Processing

---

# 📌 Future Enhancements

- Apache Airflow orchestration
- Power BI Dashboard
- Amazon QuickSight Dashboard
- Data Quality Monitoring
- CI/CD using GitHub Actions
- CloudWatch Monitoring

---

# 👩‍💻 Author

**Deepti Sahu**

🐙 GitHub: https://github.com/DeeptiSahu30

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.
