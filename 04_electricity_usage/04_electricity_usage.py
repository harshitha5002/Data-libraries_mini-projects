import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("04_electricity_usage.csv")
data["Date"]=pd.to_datetime(data["Date"])
print("Data:")
print(data)
daily_usage=data.groupby("Date")["Units_Consumed"].mean()
print("\ndaily_usage trend:")
print(daily_usage)
avg_consumption = np.mean(data["Units_Consumed"])
print("\nAverage Daily Consumption:", avg_consumption)
high_consumption=data[data["Units_Consumed"]>avg_consumption]
print("\nhigh consumpton is:")
print(high_consumption)

#line plot-daily consumption trend
plt.figure(figsize=(8,6))
plt.subplot(3,1,1)
plt.plot(data["Date"],data["Units_Consumed"],marker='o',color="red")
plt.xlabel("Date")
plt.ylabel("daily electricity usage")
plt.title("daily electricity usage trend")
plt.xticks(rotation=45)
plt.tight_layout()

#bar graph
plt.subplot(3,1,2)
plt.bar(data["Date"],data["Units_Consumed"],color="pink")
plt.xlabel("Date")
plt.ylabel("Electricity consumption")
plt.title("Electricity consumption per day")
plt.xticks(rotation=45)
plt.tight_layout()


#histogram
plt.subplot(3,1,3)
plt.hist(data["Units_Consumed"],bins=5)
plt.xlabel("Electricity Usage")
plt.ylabel("Frequency")
plt.title("Electricity Distribution")
plt.tight_layout()
plt.show()