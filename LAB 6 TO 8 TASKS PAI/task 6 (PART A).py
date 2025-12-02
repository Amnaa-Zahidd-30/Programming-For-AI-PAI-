import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('software houses PK.csv')
print (data)


# #PART A
c=data['City'].value_counts()
plt.barh(c.index,c.values,height=0.3,edgecolor='b')
plt.title("software houses located in Pakistan")
plt.xlabel("location counts")
plt.ylabel("cities")
plt.tight_layout()

plt.show()



