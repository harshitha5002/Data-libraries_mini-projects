import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("07_sales_data.csv")
data["Date"]=pd.to_datetime(data["Date"])
print("data:")
print(data)
total_sales = data["Sales"].sum()
avg_sales = data["Sales"].mean()
print("\nTotal Sales:", total_sales)
print("Average Sales:", avg_sales)
data["Moving_Avg"] = data["Sales"].rolling(window=3).mean()
print("\nSales with Moving Average:\n", data)

# Plot 1: Sales over time (line plot)
plt.subplot(2,1,1)
plt.plot(data["Date"], data["Sales"], marker="o", label="Actual Sales")
plt.plot(data["Date"], data["Moving_Avg"], marker="x", label="3-Day Moving Avg", linestyle="--")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Daily Sales with Moving Average")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Plot 2: Bar chart for sales
plt.subplot(2,1,2)
plt.bar(data["Date"], data["Sales"], color="skyblue")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Daily Sales Comparison")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()