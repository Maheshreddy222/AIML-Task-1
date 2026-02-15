import pandas as pd
df=pd.read_csv("C:/Users/bunny/Downloads/Titanic-Dataset.csv")
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin'] = df['Cabin'].fillna('Unknown')
print(df)
