import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv('mobile reviews sentiment.csv')
print(data)

fig,ax = plt.subplots(figsize=(10,5))

avgrating=data.groupby('brand')['rating'].mean()

   
ax.bar(avgrating.index, avgrating.values , color=['red','yellow','purple','green','pink','blue','orange'])   
ax.set_title(' average overall rating for each mobile brand')
ax.set_xlabel('Mobile Brand Name')
ax.set_ylabel('Mobile Ratings')

plt.xticks(rotation=45)
plt.show()


  