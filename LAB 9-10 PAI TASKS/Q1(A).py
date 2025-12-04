#USING SCIKIT LEARN LIBRARY
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X=np.array([1.1,1.3,1.5,2.0,2.2,2.9,3.0,3.2,3.2,3.7]).reshape(-1,1)
y=np.array([39,46,47,52,56,64,65,67,68,70])

model=LinearRegression()
model.fit(X,y)

print("slope:",model.coef_)
print("intercept:",model.intercept_)

newx=np.array([[4.5]])
pred=model.predict(newx)
print("Predicted salary at 4.5 yrs:",pred)

pred=model.predict(X)
r2=r2_score(y,pred)
print("R squared:",round(r2,2))
