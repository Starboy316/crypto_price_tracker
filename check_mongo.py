from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["crypto"]
collection = db["prices"]

data = list(collection.find().limit(5))
if data:
    print("✅ Sample records:")
    for doc in data:
        pprint(doc)
else:
    print("⚠️ No data found in MongoDB.")

