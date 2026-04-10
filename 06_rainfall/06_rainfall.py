import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("06_rainfall.csv")
data["Date"]=pd.to_datetime(data["Date"])
print("Rainfall data:")
print(data)
total_rainfall=np.sum(data["Rainfall_mm"])
print("\ntotal rainfall is:")
print(total_rainfall,"mm")
avg_rainfall=np.mean(data["Rainfall_mm"])
print("\naverage rainfall is:")
print(avg_rainfall,"mm")
count_rainydays=(data["Rainfall_mm"]>0).sum()
print("\nNumber of rainydays:")
print(count_rainydays)

#linechart-rainfall over time
plt.subplot(2,2,1)
plt.plot(data["Date"],data["Rainfall_mm"],marker="o")
plt.xlabel("Date",fontsize=10,fontweight="bold")
plt.ylabel("Rainfall",fontsize=10,fontweight="bold")
plt.title("Rainfall trend",fontsize=15,fontweight="bold")
plt.tight_layout()
plt.xticks(rotation=45)

#barchart-rainfall per day
plt.subplot(2,2,2)
plt.bar(data["Date"], data["Rainfall_mm"])
plt.xlabel("Date",fontsize=10,fontweight="bold")
plt.ylabel("Rainfall (mm)",fontsize=10,fontweight="bold")
plt.title("Daily Rainfall Comparison",fontsize=14,fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()

#histogram-rainfall distribution
plt.subplot(2,2,3)
plt.hist(data["Rainfall_mm"],bins=6)
plt.xlabel("Rainfall",fontsize=10,fontweight="bold")
plt.ylabel("Frequency",fontsize=10,fontweight="bold")
plt.title("Rainfall distribution",fontsize=15,fontweight="bold")
plt.tight_layout()
plt.show()

