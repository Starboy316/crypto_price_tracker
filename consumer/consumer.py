from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["crypto"]
collection = db["prices"]

# Set up Kafka Consumer
consumer = KafkaConsumer(
    'crypto_prices',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("📥 Listening to 'crypto_prices' topic...")

for message in consumer:
    price_data = message.value
    print(f"💾 Storing: {price_data}")
    collection.insert_one(price_data)
