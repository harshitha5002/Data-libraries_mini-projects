import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("10_website.csv")
data["Date"]=pd.to_datetime(data["Date"])
print("Data:")
print(data)
daily_visitors=np.mean(data["Visitors"])
print("Daily visitors is:")
print(daily_visitors)
max_visitors=data["Visitors"].max()
print("Maximum visitors is :")
print(max_visitors)

#plot-visitors trend
plt.subplot(2,2,1)
plt.plot(data["Date"],data["Visitors"],marker='^',color="green")
plt.xlabel("Date", fontweight="bold")
plt.ylabel("Number of visitors", fontweight="bold")
plt.title("Visitors trend",fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

#plot-page_views trend
plt.subplot(2,2,2)
plt.plot(data["Visitors"],data["Page_Views"],marker='^',color="green")
plt.xlabel("Visitors", fontweight="bold")
plt.ylabel("Number of page views", fontweight="bold")
plt.title("Page_views trend",fontsize=14, fontweight="bold")
plt.grid(True)
plt.tight_layout()

#scatter graph-visitors vs page views
plt.subplot(2,2,3)
plt.scatter(data["Visitors"],data["Page_Views"],color="red")
plt.xlabel("No.of visitors", fontweight="bold")
plt.ylabel("No.of page views", fontweight="bold")
plt.title("Visitors vs page views", fontweight="bold",fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()