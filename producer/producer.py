import json
import time

from kafka import KafkaProducer

from config import KAFKA_BROKER, TOPIC_NAME, MESSAGE_INTERVAL
from shipment_generator import generate_shipment


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


print("=" * 60)
print("Shipment Producer Started...")
print(f"Sending events to topic: {TOPIC_NAME}")
print("=" * 60)


try:

    while True:

        shipment = generate_shipment()

        producer.send(
            TOPIC_NAME,
            value=shipment
        )

        producer.flush()

        print(json.dumps(shipment, indent=4))

        print("-" * 60)

        time.sleep(MESSAGE_INTERVAL)

except KeyboardInterrupt:

    print("\nStopping Producer...")

finally:

    producer.close()