import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df=pd.read_csv('train8.csv')

x= df[['OverallQual', 'GrLivArea', 'GarageCars', 'YearBuilt']]
y= df['SalePrice']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(xtrain, ytrain)

pred = model.predict(xtest)

mse=mean_squared_error(ytest, pred)
r=r2_score(ytest, pred)
rmse=np.sqrt(mse)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("R squared:", round(r, 3))
print("RMSE:", round(rmse, 2))

coef_OverallQual = 22182
coef_GrLivArea = 54
coef_GarageCars = 17357
coef_YearBuilt = 395

print("OverallQual:", coef_OverallQual)
print("Meaning: For every 1-unit increase in overall house quality rating, the price increases by about $", coef_OverallQual)

print("GrLivArea", coef_GrLivArea)
print("Meaning: Each additional square foot of living area adds about $", coef_GrLivArea, "to the house price.")

print("GarageCars", coef_GarageCars)
print("Meaning: Each additional garage capacity adds roughly $", coef_GarageCars, "to the sale price.")

print("YearBuilt", coef_YearBuilt)
print("Meaning: Newer construction gives about $", coef_YearBuilt, "more value per year.")

largest_coef = max(coef_OverallQual, coef_GrLivArea, coef_GarageCars, coef_YearBuilt)
print("The feature with the largest impact is OverallQual because it has the highest coefficient", largest_coef, "among all predictors.")

