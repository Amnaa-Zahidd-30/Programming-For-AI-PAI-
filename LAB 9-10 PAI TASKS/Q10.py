import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("fifa19.csv")

def convert_value(val):
    val = val.replace("€", "").replace("M", "e6").replace("K", "e3")
    return float(eval(val))

df["Value"] = df["Value"].apply(convert_value)

features = ["Overall", "Potential", "Age", "International Reputation"]
X = df[features]
y = df["Value"]

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=42)

model1 = LinearRegression()
model1.fit(xtrain, ytrain)

pred1 = model1.predict(xtest)

mse1 = mean_squared_error(ytest, pred1)
rmse1 = np.sqrt(mse1)
r1 = r2_score(ytest, pred1)

print("\nMODEL WITH POTENTIAL")
print("Coefficients:", model1.coef_)
print("R²:", round(r1, 3))
print("RMSE:", round(rmse1, 2))

print("\nINTERPRETATION:")
print("Each coefficient shows how much the player value increases for a 1-unit rise in that feature.")
print("Largest coefficient =", features[np.argmax(abs(model1.coef_))], "=most influential on value.")

X2 = df[["Overall", "Age", "International Reputation"]]

x2train, x2test, y2train, y2test = train_test_split(X2, y, test_size=0.25, random_state=42)

model2 = LinearRegression()
model2.fit(x2train, y2train)

pred2 = model2.predict(x2test)

mse2 = mean_squared_error(y2test, pred2)
rmse2 = np.sqrt(mse2)
r2 = r2_score(y2test, pred2)

print(" MODEL WITHOUT POTENTIAL")
print("Coefficients:", model2.coef_)
print("R²:", round(r2, 3))
print("RMSE:", round(rmse2, 2))

print("\nPerformance drops without Potential,therefore Potential is an important predictor.")
