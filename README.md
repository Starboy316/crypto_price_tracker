# 💸 Real-Time Crypto Price Tracker using Kafka, MongoDB & Streamlit

A real-time data pipeline to fetch, stream, store, and visualize cryptocurrency price data using **CoinGecko API**, **Kafka**, **MongoDB**, and **Streamlit**.

---

## 🌟 Objective

> To build a full-stack project that fetches live crypto prices, streams them via Kafka, stores them in MongoDB, and visualizes them using a real-time Streamlit dashboard.

---

## 🔧 Tech Stack

- **Python 3.x**
- **Kafka** (message queue)
- **MongoDB** (document store)
- **Streamlit** (dashboard)
- **Docker Compose** (multi-container orchestration)

---

## 📁 Project Structure

```
crypto_price_tracker/
├── docker-compose.yml
├── producer/
│   └── producer.py
├── consumer/
│   └── consumer.py
├── streamlit/
│   └── dashboard.py
├── check_mongo.py
├── clear_prices.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crypto-price-tracker.git
cd crypto-price-tracker
```

### 2. Install Python Dependencies

```bash
pip install kafka-python pymongo requests pandas streamlit
```

### 3. Docker Setup

Start the containers:

```bash
docker compose up -d
```

Services:

- MongoDB: `localhost:27017`
- Mongo Express: [http://localhost:8081](http://localhost:8081)
- Kafka: `localhost:9092`

---

## 🔄 Data Flow

```
[ CoinGecko API ]
       ⬇
[ Kafka Producer ]  ---➡ [ Kafka Topic ] ➡---  [ Kafka Consumer ]
       ⬇                                ⬇
     [ Kafka ]                          [ MongoDB ]
                                           ⬇
                                    [ Streamlit Dashboard ]
```

---

## 📅 Run the Components

### 1. Producer

```bash
python producer/producer.py
```

This fetches price data and sends it to Kafka.

### 2. Consumer

```bash
python consumer/consumer.py
```

Consumes Kafka data and inserts into MongoDB.

### 3. Streamlit Dashboard

```bash
streamlit run streamlit/dashboard.py
```

View at: [http://localhost:8501](http://localhost:8501)

---

## 🔧 Utility Scripts

### Check MongoDB Data

```bash
python check_mongo.py
```

### Clear MongoDB Collection

```bash
python clear_prices.py
```

---

## ✨ Features

- Real-time price tracking
- Supports multiple cryptocurrencies
- Responsive dashboard with filtering
- Uses Dockerized MongoDB and Kafka
- Avoids duplicate and error entries

---

## ⚠️ Limitations

- CoinGecko API free tier has **rate limits** (e.g. 10-50/min).
- Dashboard only reflects valid price data (skips error entries).

---

## 🌐 Future Enhancements

- Add support for more coins
- Add filtering & historical view
- Deploy dashboard to cloud (Streamlit Cloud)
- Use InfluxDB for better time-series support
- Integrate alerting & notifications

---

## ✌️ Author

Made with ❤️ by **Rohan Suryawanshi**\
Use for portfolio, learning, and real-world data engineering practice.

---


