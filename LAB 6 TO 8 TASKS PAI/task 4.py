import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('mobile reviews sentiment.csv')
print (data)

fig,ax=plt.subplots(figsize=(10,5))

overallmeanprice=data['price_usd'].mean()
overallmeanrating=data['rating'].mean()

modelprice=data.groupby('model')['price_usd'].mean()
modelrating=data.groupby('model')['rating'].mean()

overpriced=(modelprice>overallmeanprice) & (modelrating<overallmeanrating)

ax.scatter(modelprice,modelrating,color='green')
ax.scatter(modelprice[overpriced],modelrating[overpriced],marker ='*', color='purple')

ax.set_title('Overpriced Models (High Price, Low Rating)')
ax.set_xlabel('Mean Price')
ax.set_ylabel('Mean Rating')

plt.show()



