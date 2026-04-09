import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("02_aqi.csv")
data["Date"]=pd.to_datetime(data["Date"])
print("Data is:")
print(data) 

#average of aqi city-wise
avg_aqi=data.groupby("City")["AQI"].mean()
print("\naverage aqi is:\n")
print(avg_aqi)

#maximum aqi city
max_aqi=avg_aqi.idxmax()
print("\nMaximum aqi city is:")
print(max_aqi)

#barchart
plt.subplot(2,2,1)
plt.bar(avg_aqi.index,avg_aqi.values,color="red")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.title("Average AQI by City")
plt.tight_layout()

# Plot 2: Line plot – AQI trend over time (city-wise)
for city in data["City"].unique():
    city_data = data[data["City"] == city]
plt.subplot(2,2,2)
plt.plot(city_data["Date"], city_data["AQI"], marker='o', label=city)

plt.xlabel("Date")
plt.ylabel("AQI")
plt.title("AQI Trend Over Time")
plt.legend()
plt.xticks(rotation=45)


#histogram
plt.subplot(2,2,3)
plt.hist(data["AQI"],bins=6)
plt.xlabel("AQI value")
plt.ylabel("Frequency")
plt.title("AQI Distribution")
plt.tight_layout()
plt.show()