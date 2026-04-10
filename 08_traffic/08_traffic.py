import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("08_traffic.csv")
data["Date"] = pd.to_datetime(data["Date"])
print(data)
hourly_avg=data.groupby("Hour")["Vehicle_Count"].mean()
print("\nhourly avg:")
print(hourly_avg)
peak_hour=hourly_avg.idxmax()
print("\npeak hour is:")
print(peak_hour)
day_time_avg=data.groupby("Day")["Vehicle_Count"].mean()
print("\naverage traffic",day_time_avg)

#line plot
plt.figure()
plt.subplot(2,1,1)
plt.plot(hourly_avg.index,hourly_avg.values,marker="o")
plt.xlabel("Hour of day")
plt.ylabel("Avg vehicle count")
plt.title("Avg traffic flow by hour")
plt.grid(True)

#bar plot
plt.subplot(2,1,2)
plt.bar(day_time_avg.index,day_time_avg.values)
plt.xlabel("Day type")
plt.ylabel("Traffic count")
plt.title("weekday vs weekend coversion")
plt.tight_layout()
plt.show()

