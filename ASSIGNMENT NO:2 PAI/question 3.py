import pandas as pd
import numpy as np

#Load & inspect
data =pd.read_csv("Titanic-Dataset.csv")

print("Dataset loaded successfully!")
print("Total rows:",len(data))
print("Total columns:",len(data.columns))
print()
print("All columns in the dataset:")
print(list(data.columns))
print()

#inspection report
print("Simple Inspection Report ===")
for column in data.columns:
    print("Column Name:",column)
    print("Data Type:", data[column].dtype)
    print("Missing Values:", data[column].isnull().sum())
    print("Missing Percentage:", round((data[column].isnull().sum() / len(data))*100,2),"%")
    print("-----------------------------")

# Handle mising data
# (a)AGE
data['Age'] =data.groupby(['Pclass','Sex'])['Age'].transform(lambda x:x.fillna(x.median()))

# (b)EMBARKED
data['Embarked'].fillna(data['Embarked'].mode()[0],inplace=True)

# (c)CABIN
if 'Cabin' in data.columns:
    data.drop(columns=['Cabin'],inplace=True)
    print("\nColumn 'Cabin' dropped because it had too many missing values.")

#feature engineering
# (a)
data['FamilySize'] =data['SibSp'] + data['Parch']

# (b)
data['IsAlone'] =np.where(data['FamilySize']==0,1,0)

#type conversion
data['Age'] =data['Age'].astype('int64')

#Save clean data
data.to_csv("titanic_cleaned.csv",index=False)
print("Data cleaning completed successfully! Saved as 'Titanic_Cleaned.csv")
