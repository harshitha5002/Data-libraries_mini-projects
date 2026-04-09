import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("03_attendance.csv")
data["attendance_percentage"]=np.round(data["Attended_Classes"]/data["Total_Classes"]*100,2)
print("\npercentage")
print(data)
defaulters=data[data["attendance_percentage"]<75]
print("\ndefaulters list:")
print(defaulters)

#bar plot
plt.figure()
plt.subplot(1, 2, 1)
plt.bar(data["Name"], data["attendance_percentage"])
plt.axhline(75, linestyle='--', label="Minimum Required (75%)")
plt.xlabel("Student Name")
plt.ylabel("Attendance Percentage")
plt.title("Student Attendance Analysis")

#histogram
plt.subplot(1, 2, 2)
plt.hist(data["attendance_percentage"], bins=5)
plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")
plt.title("Attendance Distribution")
plt.tight_layout()
plt.show()

