from AIML_1_1 import *
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)
print(df)
