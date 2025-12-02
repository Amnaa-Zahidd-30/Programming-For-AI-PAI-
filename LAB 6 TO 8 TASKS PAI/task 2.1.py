import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('mobile reviews sentiment.csv')
print(data)

fig,ax=plt.subplots(figsize=(10,5))

avgprice=data.groupby('brand')['price_usd'].mean()

ax.bar(avgprice.index,avgprice.values)
ax.set_title('Average price (in USD) for each mobile brand')
ax.set_xlabel('Mobile Brand Name')
ax.set_ylabel('Price in USD')

plt.xticks(rotation=45)
plt.show()