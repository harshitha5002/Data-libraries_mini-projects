import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("01_battery_usage.csv")
print("Mobile Battery Usage Data:\n")
print(data)
total_usage = np.sum(data["Battery_Usage_Percent"])
print("\nTotal Battery Usage:", total_usage)
max_app = data.loc[data["Battery_Usage_Percent"].idxmax()]
print("\nHighest Battery Consuming App:\n", max_app)

# Plot 1: Bar chart – App-wise battery usage
plt.subplot(2,2,1)
plt.bar(data["App"], data["Battery_Usage_Percent"])
plt.xlabel("Mobile App")
plt.ylabel("Battery Usage (%)")
plt.title("App-wise Battery Consumption")
plt.xticks(rotation=45)
plt.tight_layout()

# Plot 2: Pie chart – Battery usage distribution
plt.subplot(2,2,2)
plt.pie(
    data["Battery_Usage_Percent"],
    labels=data["App"],
    autopct="%1.1f%%",
    startangle=90)
plt.title("Battery Usage Distribution by App")
plt.tight_layout()


# Plot 3: Histogram – Battery usage spread
plt.subplot(2,2,3)
plt.hist(data["Battery_Usage_Percent"], bins=5)
plt.xlabel("Battery Usage (%)")
plt.ylabel("Frequency")
plt.title("Battery Usage Distribution")
plt.tight_layout()
plt.show()