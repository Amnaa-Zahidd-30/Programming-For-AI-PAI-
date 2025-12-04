import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("train.csv")

features=["Pclass", "Sex", "Age", "Fare"]
target="Survived"

le=LabelEncoder()
df["Sex"]=le.fit_transform(df["Sex"])

df["Age"]=df["Age"].fillna(df["Age"].median())

X=df[features]
y=df[target]

Xtrain,Xtest,ytrain,ytest=train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(Xtrain, ytrain)

pred = clf.predict(Xtest)

ac=accuracy_score(ytest, pred)
cr=classification_report(ytest, pred)

print("Accuracy:", ac)
print("Classification Report:\n", cr)

cm = confusion_matrix(ytest,pred)
sns.heatmap(cm, annot=True, cmap="Blues", fmt='d')
plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

plt.figure(figsize=(18, 10))
plot_tree(clf, feature_names=features, class_names=["Died", "Survived"], filled=True)
plt.show()
