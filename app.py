import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

st.title("Disease Symptom Prediction System")
st.write("Educational use only. Not for medical diagnosis.")

df=pd.read_csv("training.csv")
df.fillna(0,inplace=True)

encoder=LabelEncoder()
df["prognosis"]=encoder.fit_transform(df["prognosis"])
X=df.drop("prognosis",axis=1)
y=df["prognosis"]

Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=42)

models={
"Logistic Regression":LogisticRegression(max_iter=1000),
"Random Forest":RandomForestClassifier(n_estimators=200,random_state=42),
"SVM":SVC(),
"KNN":KNeighborsClassifier(),
"SGD":SGDClassifier(max_iter=1000,tol=1e-3)
}

best_model=None
best_acc=0
for name,model in models.items():
    model.fit(Xtrain,ytrain)
    acc=accuracy_score(ytest,model.predict(Xtest))
    if acc>best_acc:
        best_acc=acc
        best_model=model
        best_name=name

symptoms=X.columns.tolist()

user_symptoms=st.multiselect("Select your symptoms",symptoms)

if st.button("Predict Disease"):
    inputdata=np.zeros(len(symptoms))
    for s in user_symptoms:
        inputdata[symptoms.index(s)]=1
    pred=best_model.predict([inputdata])[0]
    disease=encoder.inverse_transform([pred])[0]
    st.success(f"Predicted Disease: {disease}")
    st.info(f"Model Used: {best_name}")
