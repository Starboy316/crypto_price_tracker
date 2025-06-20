import streamlit as st
from pymongo import MongoClient
import pandas as pd
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["crypto"]
collection = db["prices"]

# Streamlit config
st.set_page_config(page_title="Crypto Price Tracker", layout="wide")
st.title("💹 Real-Time Crypto Price Tracker")

# Fetch data from MongoDB
data = list(collection.find({}, {"_id": 0}))

if not data:
    st.warning("⚠️ No data found. Make sure producer and consumer are running.")
else:
    # Convert to DataFrame
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Filter out records missing bitcoin/ethereum
    df = df[df['prices'].apply(lambda x: 'bitcoin' in x and 'ethereum' in x)]

    # Extract prices safely
    df['bitcoin'] = df['prices'].apply(lambda x: x.get('bitcoin', {}).get('usd', None))
    df['ethereum'] = df['prices'].apply(lambda x: x.get('ethereum', {}).get('usd', None))

    # Remove rows with suspicious/junk values
    df = df[(df['bitcoin'] < 100000) & (df['bitcoin'] > 1000)]
    df = df[(df['ethereum'] < 10000) & (df['ethereum'] > 100)]

    # Show latest data table
    st.subheader("📋 Latest Prices")
    st.dataframe(df[['timestamp', 'bitcoin', 'ethereum']].tail(10), use_container_width=True)

    # Plot line chart
    st.subheader("📈 Price Trends")
    st.line_chart(df.set_index('timestamp')[['bitcoin', 'ethereum']])
