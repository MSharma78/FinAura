import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="FinAura", page_icon="📈")

st.title("📈 FinAura - AI Stock Prediction Dashboard")
st.write("Welcome to FinAura! Let's make smarter investment decisions.")

# ---- Stock Symbol Input ----
st.subheader("Phase 2: Fetching Live Stock Data")
st.write("Enter a stock ticker symbol (e.g., AAPL for Apple, TSLA for Tesla):")

# Text input
ticker_symbol = st.text_input("Stock Symbol", "AAPL")

# Fetch data button
if st.button("Fetch Data"):
    try:
        stock_data = yf.download(ticker_symbol, period="1mo", interval="1d")
        st.success(f"Showing data for {ticker_symbol}")
        st.write(stock_data.tail())  # Display last few rows

        # ---- Plot closing price ----
        st.subheader(f"{ticker_symbol} - Closing Price Chart (Last 30 Days)")
        plt.figure(figsize=(10,4))
        plt.plot(stock_data['Close'], label='Close Price')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Error fetching data: {e}")
