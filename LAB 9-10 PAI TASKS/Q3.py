import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X=np.array([150,155,160,165,170,175,180]).reshape(-1,1)
y=np.array([50,55,60,63,68,72,75])

model=LinearRegression()
model.fit(X,y)
predy=model.predict(X)

print("slope:",model.coef_)
print("intercept:",model.intercept_)

newx=np.array([[172]])
pred=model.predict(newx)
print("predicted weight:",pred)

predall=model.predict(X)
residuals=y-predall
print("residuals:",residuals)

plt.scatter(X,y,label="data points")
plt.plot(X,predy,label="best fit line")
plt.scatter(newx,pred,label="predicted point")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.show()
