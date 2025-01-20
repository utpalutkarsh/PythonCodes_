# ****Fetch Shares data using yfinance (Yahoo Finance API)*****

import yfinance as yf

print(f"Persistent 's current stock price is: ₹ "f"{round(yf.Ticker("PERSISTENT.NS").history(period="1d")['Close'].iloc[0],2)}")

