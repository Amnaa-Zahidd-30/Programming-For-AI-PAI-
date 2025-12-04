import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X1=np.array([150,155,160,165,170,175,180]).reshape(-1,1)
y1=np.array([50,55,60,63,68,72,75])

X2=np.array([150,155,160,165,170,175,180,190]).reshape(-1,1)
y2=np.array([50,55,60,63,68,72,75,60])  

m1=LinearRegression()
m1.fit(X1,y1)
m2=LinearRegression()
m2.fit(X2,y2)

pred1=m1.predict(X1)
pred2=m2.predict(X2)

print("Original slope:",m1.coef_)
print("Original intercept:",m1.intercept_)

print("New slope with outlier:",m2.coef_)
print("New intercept with outlier:",m2.intercept_)

r1=r2_score(y1,pred1)
r2 = r2_score(y2,pred2)

print("Original R²:",r1)
print("R² with outlier:",r2)
