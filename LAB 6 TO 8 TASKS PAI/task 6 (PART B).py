import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('software houses PK.csv')

data["Services"] = data["Services"].astype(str).str.lower()

industrykeywords = ["web","mobile","app","software","design","marketing","ai","ecommerce","cloud","seo","graphic","branding"]
industrycounts = (data["Services"].apply(lambda x: [k for k in industrykeywords if k in x]).explode().value_counts())

fig,ax=plt.subplots(figsize=(10,5))
industrycounts.plot(kind="bar")
plt.title("Industries Served by Software Houses in Pakistan")
plt.xlabel("Industry Keyword")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()