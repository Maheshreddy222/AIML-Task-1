from AIML_1_2 import *
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
scaler = StandardScaler()

numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch', 'Pclass', 'PassengerId']

df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print("\nData after standardization:")
print(df.head())