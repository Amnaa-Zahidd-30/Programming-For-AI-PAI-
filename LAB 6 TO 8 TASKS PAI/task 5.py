import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('mobile reviews sentiment.csv')
print (data)

fig,ax=plt.subplots(figsize=(10,10))

mapping={'Positive': 1 , "Negative": 2, "Neutral": 3}
data['sentiments']=data['sentiment'].map(mapping)
ratings=data['rating']
columns=[data['sentiments'],ratings]
plt.boxplot(columns)

ax.set_title("[Sentiment vs Rating Comparison (Box Plot)]")
ax.set_xlabel("sentiment data")
ax.set_ylabel("ratings data")
plt.show()