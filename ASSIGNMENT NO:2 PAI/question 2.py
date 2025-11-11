import numpy as np

#load data
with open("sensor_data.csv", "r") as f:
    lines = f.readlines()
datalist=[]
for line in lines:
    parts=line.strip().split(",")
    datalist.append(parts)
    
#numpy conversion
data =np.array(datalist,dtype=float)

#Data Cleaning (Vectorized)
data[data==-999]=np.nan
data[(data < 0) | (data > 100)]=np.nan

#Data Analysis (Axis Operation)
mean=np.nanmean(data,axis=0)
median=np.nanmedian(data,axis=1)
counts=np.isnan(data).sum(axis=0)
invalidsensor=np.argmax(counts)

#Normalization 
validmin =np.nanmin(data)
validmax =np.nanmax(data)
normalized_data =(data - validmin) / (validmax - validmin)

#Save output
np.savetxt("sensor_data_normalized.csv", normalized_data, delimiter=",",fmt="%.4f")

print("Data Cleaning & Normalization Complete")
print(f"Mean Moisture per Sensor (columns):{mean[:5]}")
print(f"Median Moisture per Hour (rows): {median[:5]}")
print(f"Sensor with most invalid readings: Column {invalidsensor}")
print(f"Minimum valid reading: {validmin:.2f}")
print(f"Maximum valid reading: {validmax:.2f}")