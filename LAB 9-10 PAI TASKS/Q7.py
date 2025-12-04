import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df=pd.read_csv("mallcustomers.csv") 

print("Customer Data (First 10 Rows):")
print(df.head())

features=df[["Annual Income (k$)", "Spending Score (1-100)"]]

scaler=StandardScaler()
scaled_features=scaler.fit_transform(features)

kmeans=KMeans(n_clusters=5, random_state=42)
df["Cluster"]=kmeans.fit_predict(scaled_features)

print("Cluster Assignments:")
print(df[["CustomerID", "Annual Income (k$)", "Spending Score (1-100)", "Cluster"]].head())

plt.figure(figsize=(10,7))
plt.scatter(df["Annual Income (k$)"],df["Spending Score (1-100)"],c=df["Cluster"],s=100)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("K-Means Clustering of Customers")
plt.show()

print("INTERPRETATION OF CLUSTERS:")
print("Cluster 0: Low income, low spending customers = Budget-conscious group")
print("Cluster 1: High income, high spending customers = VIP / Premium shoppers")
print("Cluster 2: Low income, high spending customers = Impulsive buyers")
print("Cluster 3: High income, low spending customers = Wealthy but conservative buyers")
print("Cluster 4: Average income, average spending = Standard middle-class customers")
