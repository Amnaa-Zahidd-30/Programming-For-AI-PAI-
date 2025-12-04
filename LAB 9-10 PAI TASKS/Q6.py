import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

df=pd.read_csv("train.csv")
features=["Pclass", "Sex", "Age", "Fare", "Embarked"]
target="Survived"

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

lesex=LabelEncoder()
df["Sex"] = lesex.fit_transform(df["Sex"])

le_emb=LabelEncoder()
df["Embarked"]= le_emb.fit_transform(df["Embarked"])

X = df[features]
y = df[target]

Xtrain,Xtest,ytrain,ytest=train_test_split(X, y, test_size=0.2, random_state=42)
clf= DecisionTreeClassifier(random_state=42)
clf.fit(Xtrain, ytrain)

pred=clf.predict(Xtest)

acc=accuracy_score(ytest, pred)
report=classification_report(ytest, pred)

print("Accuracy:", acc)
print("Classification Report:\n", report)

plt.figure(figsize=(20, 10))
plot_tree(clf, feature_names=features, class_names=["Died", "Survived"], filled=True)
plt.show()

print("\nDISCUSSION:")
print("Filling Age removes missing data issues and improves accuracy slightly.")
print("Encoding categorical variables lets the model use them correctly.")
print("Without preprocessing, the model would fail due to NaN or text data.")
