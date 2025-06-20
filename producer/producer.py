import requests
from kafka import KafkaProducer
from json import dumps
from datetime import datetime
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

while True:
    try:
        response = requests.get(url)
        data = response.json()

        if 'bitcoin' not in data or 'ethereum' not in data:
            print("🚫 API limit or malformed data. Sleeping...")
            time.sleep(60)
            continue

        message = {
            'timestamp': datetime.now().isoformat(),
            'prices': data
        }

        producer.send('crypto_prices', value=message)
        print(f"📤 Sent: {message}")

    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(60)

    time.sleep(15)
