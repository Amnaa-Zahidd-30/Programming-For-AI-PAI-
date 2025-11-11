import pandas as pd
import numpy as np

titanic=pd.read_csv("titanic_cleaned.csv")
fares=pd.read_csv("ticket_fares.csv")

print("Datasets loaded successfully!")
print("titanic_cleaned.csv shape:",titanic.shape)
print("ticket_fares.csv shape:",fares.shape)

df=pd.merge(titanic,fares,on='Ticket',how='inner')
print("Datasets merged successfully on 'Ticket'")
print("Merged DataFrame shape:",df.shape)
print()

bins=[0,12,19,59,120]     
labels =['Child','Teen','Adult','Senior']
df['AgeGroup']=pd.cut(df['Age'],bins=bins,labels=labels,right=False)
survival=df.groupby(['Sex','AgeGroup'])['Survived'].mean().reset_index()

print("\Mean Survival Rate:")
print(survival)

print("Hypothesis 1: Women and Children First")
print(survival)
print()

with open("report.txt", "w") as file:
    file.write("Hypothesis 1: Women and Children First\n")
    file.write(str(survival))
    file.write("\nConclusion:\n")
    file.write(
        "The data generally supports the 'Women and Children First' hypothesis. "
        "As seen above, females and younger passengers (children) show a higher mean survival rate "
        "compared to males and adult passengers. This pattern aligns with the historical claim that "
        "women and children were prioritized during the Titanic evacuation.\n"
    )

print("Hypothesis 1 analysis completed and written to report.txt")

survivalbyclass=df.groupby('Pclass')['Survived'].mean().reset_index()
print("Method A: Survival Rate by Passenger Class")
print(survivalbyclass)
print()

df['FareBin']=pd.qcut(df['Fare'],q=4,labels=['Low','Medium','High','Very High'])
survivalbyfare=df.groupby('FareBin')['Survived'].mean().reset_index()
print("Method B: Survival Rate by Fare Bin")
print(survivalbyfare)
print()

with open("report.txt", "a") as file:
    file.write("\nHypothesis 2: Wealthy Had a Higher Survival Rate\n")
    file.write("\nMethod A: By Passenger Class\n")
    file.write(str(survivalbyclass))
    file.write("\n Method B: By Fare Bin\n")
    file.write(str(survivalbyfare))
    file.write("\nConclusion:\n")
    file.write(
        "Both methods indicate that wealthier passengers had higher survival rates. "
        "First-class passengers show a significantly greater mean survival rate compared to lower classes, "
        "and the Fare-based bins confirm that passengers who paid higher fares were more likely to survive. "
        "Therefore, the data supports the 'Wealth Hypothesis' as well.\n"
    )

print("Hypothesis 2 analysis completed and appended to report.txt")
print("All analyses complete! 'report.txt' contains the summary conclusions.")


