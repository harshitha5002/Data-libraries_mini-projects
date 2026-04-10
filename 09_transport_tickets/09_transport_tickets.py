import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("09_transport_tickets.csv")
data["Date"]=pd.to_datetime(data["Date"])
data["Revenue"]=data["Ticket_Price"]*data["Tickets_Sold"]
print("data:")
print(data)
daily_revenue=data.groupby("Date")["Revenue"].sum()
print("\nDaily revenue is:")
print(daily_revenue)
route_revenue=data.groupby("Route")["Revenue"].sum()
print("\nRoute revenue is:")
print(route_revenue)

#barchart-route revenue
plt.figure()
plt.subplot(2,2,1)
plt.bar(route_revenue.index,route_revenue.values,color="green")
plt.xlabel("Route")
plt.ylabel("Revenue")
plt.title("Route revenue")

#line plot-daily revenue
plt.subplot(2,2,2)
plt.plot(daily_revenue.index,daily_revenue.values,marker='o',linestyle="dashed")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Daily revenue trend")
plt.xticks(rotation=45)
plt.tight_layout()

#histogram
plt.subplot(2,2,3)
plt.hist(data["Revenue"],bins=5)
plt.xlabel("Revenue")
plt.ylabel("Frequnecy")
plt.title("Fevenue distribution")
plt.tight_layout()
plt.show()