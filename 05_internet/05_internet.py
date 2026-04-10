import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("05_internet.csv")
data["Date"]=pd.to_datetime(data["Date"])
print("Internet usage:")
print(data)
day_type_avg=data.groupby("Day")["Usage_GB"].mean()
print("\nDay avg is:")
print(day_type_avg)

#line plot
plt.subplot(2,2,1)
plt.plot(data["Date"],data["Usage_GB"],marker='o')
plt.xlabel("Date")
plt.ylabel("Usage (gb)")
plt.title("Internet usage trend")
plt.xticks(rotation=45)
plt.tight_layout()

#bar plot
plt.subplot(2,2,2)
plt.bar(day_type_avg.index,day_type_avg.values,color="green")
plt.xlabel("Day type")
plt.ylabel("Average value")
plt.title("weekday vs weekend")
plt.tight_layout()

#box plot
plt.subplot(2,2,3)
plt.boxplot(data["Usage_GB"])
plt.ylabel("Usage (gb)")
plt.title ("Internet usage distribution")
plt.tight_layout()
plt.show()