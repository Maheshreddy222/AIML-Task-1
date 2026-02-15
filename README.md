# AIML-Task-1

##  Project Overview

This project demonstrates the complete data preprocessing pipeline for the Titanic dataset. The goal is to clean, transform, and prepare the data so it can be used for machine learning model training.

The preprocessing steps include:

* Importing and exploring the dataset
* Handling missing values
* Encoding categorical features
* Standardizing numerical features
* Visualizing outliers
* Removing outliers
* Preparing data for model training

---

##  Dataset Information

Dataset Name: Titanic Dataset
Number of rows: 891
Number of columns: 12

Columns include:

* PassengerId
* Survived (Target)
* Pclass
* Name
* Sex
* Age
* SibSp
* Parch
* Ticket
* Fare
* Cabin
* Embarked

---

##  Requirements

Install the following libraries before running the project:

```bash
pip install numpy pandas matplotlib scikit-learn scipy
```

---

##  Step 1: Import Libraries and Dataset

Purpose:
Load dataset and explore basic structure.

Tasks performed:

* Import pandas, numpy, matplotlib, sklearn
* Load dataset using pandas
* Display first few rows
* Check data types
* Check missing values

---

##  Step 2: Handle Missing Values

Missing values found in:

* Age
* Cabin
* Embarked

Handling methods used:

* Age → filled with Median
* Embarked → filled with Mode
* Cabin → filled with "Unknown"

Reason:
Median is better for numerical data with outliers.
Mode is best for categorical data.

---

##  Step 3: Encode Categorical Features

Categorical columns:

* Sex
* Embarked

Encoding methods:

* Sex → Label Encoding
  male = 0
  female = 1

* Embarked → One-Hot Encoding
  Created new columns:

  * Embarked_Q
  * Embarked_S

Dropped unnecessary columns:

* Name
* Ticket
* Cabin

Reason:
These columns are not useful for prediction.

---

##  Step 4: Standardize Numerical Features

Standardization formula:

Z = (X − Mean) / Standard Deviation

Standardized columns:

* Age
* Fare
* SibSp
* Parch
* Pclass
* PassengerId

Purpose:

* Bring all values to same scale
* Improve machine learning performance

Tool used:

StandardScaler from sklearn.preprocessing

---

##  Step 5: Visualize Outliers

Outliers were visualized using Boxplots.

Columns checked:

* Age
* Fare
* SibSp
* Parch
* Pclass

Tool used:

matplotlib.pyplot

Purpose:

* Identify extreme values
* Improve data quality

---

##  Step 6: Remove Outliers

Method used: IQR (Interquartile Range)

Formula:

IQR = Q3 − Q1

Lower limit = Q1 − 1.5 × IQR
Upper limit = Q3 + 1.5 × IQR

Values outside this range were removed.

Result:

Before removing outliers: 891 rows
After removing outliers: 577 rows

---

##  Step 7: Prepare Data for Machine Learning

Split data into:

Features (X):

* PassengerId
* Pclass
* Sex
* Age
* SibSp
* Parch
* Fare
* Embarked_Q
* Embarked_S

Target (y):

* Survived

Data is now ready for training machine learning models.

---

##  Tools and Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* SciPy

---

##  Project Outcome

Successfully completed:

✔ Data cleaning
✔ Missing value handling
✔ Encoding
✔ Standardization
✔ Outlier detection and removal
✔ Data preparation for machine learning

---

##  Learning Outcome

This project helps understand:

* Data preprocessing
* Feature engineering
* Data cleaning techniques
* Machine learning preparation steps

---

