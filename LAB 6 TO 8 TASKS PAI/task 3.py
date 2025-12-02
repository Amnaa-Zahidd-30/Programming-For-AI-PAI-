import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('mobile reviews sentiment.csv')
print(data)

fig,ax=plt.subplots(figsize=(8,8))

counts=data['sentiment'].value_counts()

plt.pie(counts.values,labels=counts.index,autopct='%1.2f%%')
plt.show()

