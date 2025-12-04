import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('laptopprices.csv')
df['ram_gb'] = df['ram_gb'].str.replace(' GB', '').astype(int)

df['ssd'] = df['ssd'].str.replace(' GB', '').astype(int)
df['hdd'] = df['hdd'].str.replace(' GB', '').astype(int)
df['storage_total'] = df['ssd'] + df['hdd']

df['cpu_gen'] = df['processor_gnrtn'].str.extract(r'(\d+)')
df['cpu_gen'] = df['cpu_gen'].fillna(0).astype(int)  

df['weight_encoded'] = df['weight'].astype('category').cat.codes

X = df[['ram_gb', 'weight_encoded', 'cpu_gen', 'storage_total']]
y = df['Price']

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=42)

model1 = LinearRegression()
model1.fit(xtrain, ytrain)

pred1 = model1.predict(xtest)

mse1 = mean_squared_error(ytest, pred1)
rmse1 = np.sqrt(mse1)
r2_1 = r2_score(ytest, pred1)

print("UNSCALED MODEL:")
print("Coefficients:", model1.coef_)
print("R²:", round(r2_1, 4))
print("RMSE:", round(rmse1, 2))
print()

scaler = StandardScaler()
xtrain_scaled = scaler.fit_transform(xtrain)
xtest_scaled = scaler.transform(xtest)

model2 = LinearRegression()
model2.fit(xtrain_scaled, ytrain)

pred2 = model2.predict(xtest_scaled)

mse2 = mean_squared_error(ytest, pred2)
rmse2 = np.sqrt(mse2)
r2_2 = r2_score(ytest, pred2)

print("SCALED MODEL:")
print("Coefficients:", model2.coef_)
print("R²:", round(r2_2, 4))
print("RMSE:", round(rmse2, 2))
print()

coef_series = pd.Series(model2.coef_, index=X.columns)
most_important = coef_series.abs().idxmax()

print("Most significant predictor:", most_important)
