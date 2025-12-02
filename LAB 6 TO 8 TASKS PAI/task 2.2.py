import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('mobile reviews sentiment.csv')
print(data)

fig,ax=plt.subplots(figsize=(10,5))

ax.hist(data['rating'],edgecolor='black')

ax.set_title('Distribution of Ratings across all reviews')
ax.set_xlabel('Reviews')
ax.set_ylabel('Distribution of Ratings')

plt.show()


