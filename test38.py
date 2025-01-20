import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Admin\Downloads\NIFTY 50-9-12-2024-to-9-01-2025.csv")
df.columns = df.columns.str.strip()  # Removes leading/trailing whitespace

df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y', errors='coerce')
df = df.dropna(subset=['Date','High', 'Close','Low'])

# Step 3: Convert 'Date' to a datetime object (for proper x-axis scaling)
df['Date'] = pd.to_datetime(df['Date'])

# Step 4: Plot the closing price over time
plt.figure(figsize=(20, 10))
plt.plot(df['Date'], df['Close'],'r-')
plt.plot(df['Date'], df['High'],'g-')
plt.plot(df['Date'], df['Low'],'b-')

# Step 5: Customize the plot
plt.title('Index Movement - High & Low per day', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Closing Price', fontsize=20)
# plt.xticks(rotation=15) # Rotate dates for better readability
plt.grid(True)
# plt.legend()

# Step 6: Show the plot
plt.show()