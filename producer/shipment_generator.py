from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker for Indian locale
fake = Faker("en_IN")

# Cities
CITIES = [
    "Mumbai",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad"
]

# Warehouses mapped to origin city
WAREHOUSE_MAP = {
    "Mumbai": "Mumbai Warehouse",
    "Delhi": "Delhi Warehouse",
    "Bengaluru": "Bengaluru Warehouse",
    "Hyderabad": "Hyderabad Warehouse",
    "Chennai": "Chennai Warehouse",
    "Pune": "Pune Warehouse",
    "Kolkata": "Kolkata Warehouse",
    "Ahmedabad": "Ahmedabad Warehouse"
}

# Carriers with realistic distribution
CARRIERS = [
    "Blue Dart",
    "Delhivery",
    "DTDC",
    "XpressBees",
    "Ecom Express"
]

CARRIER_WEIGHTS = [30, 30, 15, 15, 10]

# Shipment lifecycle
STATUSES = [
    "Order Created",
    "Packed",
    "Shipped",
    "In Transit",
    "Out for Delivery",
    "Delivered"
]

# Delay reasons
DELAY_REASONS = [
    "Bad Weather",
    "Heavy Traffic",
    "Vehicle Breakdown",
    "Route Diversion",
    "Customer Unavailable",
    "Address Verification Pending"
]


def generate_shipment():
    """
    Generate one realistic shipment event.
    Returns:
        dict
    """

    # Origin and destination
    origin_city = random.choice(CITIES)

    destination_city = random.choice(
        [city for city in CITIES if city != origin_city]
    )

    warehouse = WAREHOUSE_MAP[origin_city]

    carrier = random.choices(
        CARRIERS,
        weights=CARRIER_WEIGHTS,
        k=1
    )[0]

    # Shipment timestamps
    created_at = datetime.now() - timedelta(
        days=random.randint(0, 5),
        hours=random.randint(0, 12)
    )

    status_index = random.randint(0, len(STATUSES) - 1)

    status = STATUSES[status_index]

    event_time = created_at + timedelta(
        hours=random.randint(1, 72)
    )

    estimated_delivery = created_at + timedelta(
        days=random.randint(2, 7)
    )

    # Weight
    weight = round(
        random.uniform(0.5, 40),
        2
    )

    # Shipping cost based on weight
    shipping_cost = round(
        80 + (weight * random.uniform(18, 30)),
        2
    )

    # Delay logic
    delay_reason = None

    if status in [
        "Shipped",
        "In Transit",
        "Out for Delivery"
    ]:
        if random.random() < 0.20:
            delay_reason = random.choice(DELAY_REASONS)

    shipment = {

        "shipment_id": f"SHP{random.randint(100000,999999)}",

        "order_id": f"ORD{random.randint(100000,999999)}",

        "customer_id": f"CUST{random.randint(10000,99999)}",

        "customer_name": fake.name(),

        "origin_city": origin_city,

        "destination_city": destination_city,

        "warehouse": warehouse,

        "carrier": carrier,

        "weight_kg": weight,

        "shipping_cost": shipping_cost,

        "status_index": status_index,

        "status": status,

        "delay_reason": delay_reason,

        "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),

        "estimated_delivery": estimated_delivery.strftime("%Y-%m-%d %H:%M:%S"),

        "event_time": event_time.strftime("%Y-%m-%d %H:%M:%S")
    }

    return shipment


if __name__ == "__main__":
    from pprint import pprint

    pprint(generate_shipment())