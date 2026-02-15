import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from AIML_1_3 import *

for col in numerical_cols:
    plt.figure()
    plt.boxplot(df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()


# ================================
# STEP 7: Remove outliers using IQR method
# ================================

df_clean = df.copy()

for col in numerical_cols:
    
    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]


print("\nShape before removing outliers:", df.shape)
print("Shape after removing outliers:", df_clean.shape)


# ================================
# STEP 8: Separate features and target
# ================================

X = df_clean.drop("Survived", axis=1)
y = df_clean["Survived"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())
