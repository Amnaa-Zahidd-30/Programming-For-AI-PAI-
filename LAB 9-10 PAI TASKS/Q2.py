import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X=np.array([2,3,4,5,6,7,8]).reshape(-1,1)
y=np.array([30,25,20,15,12,10,8])

model=LinearRegression()
model.fit(X,y)

print("slope:",model.coef_)
print("intercept:",model.intercept_)

pred=model.predict(X)
r2 =r2_score(y, pred)
print("R squared:",r2)

# scatter + line
plt.scatter(X,y,label="data")
plt.plot(X,pred,label="best fit")
plt.xlabel("Screen On Time (hrs)")
plt.ylabel("Battery Life (hrs)")
plt.legend()
plt.show()
