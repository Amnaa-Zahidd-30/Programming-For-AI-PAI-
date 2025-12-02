import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('software houses PK.csv')
print (data)
data['Services']=data['Services'].astype(str).str.lower()

technology=["ai","flutter","seo","it services","machine learning","node","react","web development","graphic designing","php web development","e-commerce","mobile apps","cybersecurity","software development","wordpress","shopify"]

languages=["c++","java","python","c#","javascript","php","r","kotlin","c","typescript"]

ser=(data['Services'].apply(lambda x:[k for k in languages if k in x])).explode().value_counts()

ser2=(data['Services'].apply(lambda y:[j for j in technology if j in y])).explode().value_counts()

fig,ax=plt.subplots(figsize=(10,5))
ser.plot(kind="bar")
plt.title("most commonly used programming languages in pakistan")
plt.xlabel("languages")
plt.ylabel("Frequency Counts")
plt.tight_layout()
plt.show()

ser2.plot(kind="bar")
plt.title("most commonly used technology in pakistan")
plt.xlabel("technology")
plt.ylabel("Frequency Counts")
plt.tight_layout()
plt.show()

