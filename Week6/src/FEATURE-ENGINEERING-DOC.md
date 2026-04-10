# Feature Engineering and Feature Selection Documentation

## Project: Titanic Survival Prediction

## Week 6 – Day 2

## Author: Vidhi Omer

---

# 1. Introduction

Feature engineering is a critical step in machine learning where raw data is transformed into meaningful features that improve model performance.
The goal is to extract useful patterns from existing variables so that machine learning algorithms can learn better relationships with the target variable.

In this project, feature engineering was applied to the Titanic dataset to create additional informative features, encode categorical variables, scale numerical values, and select the most important features using statistical techniques.

---

# 2. Dataset Overview

The dataset contains passenger information from the Titanic ship, including demographic details, ticket information, and survival status.

### Target Variable

* **Survived**

  * 0 → Passenger did not survive
  * 1 → Passenger survived

### Important Original Features

* PassengerId
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

Some of these variables required transformation to make them useful for machine learning.

---

# 3. Feature Engineering

Feature engineering was performed to create new meaningful variables that may better capture relationships between passenger characteristics and survival outcomes.

### 3.1 Family Size

Family size represents the total number of family members traveling together.

Formula:

FamilySize = SibSp + Parch + 1

Explanation:

* SibSp → Number of siblings or spouses aboard
* Parch → Number of parents or children aboard
* +1 → Includes the passenger themselves

This feature helps the model understand whether passengers traveling with family had different survival probabilities.

---

### 3.2 IsAlone

This feature indicates whether a passenger was traveling alone.

Condition:

If FamilySize == 1 → IsAlone = 1
Else → IsAlone = 0

Passengers traveling alone may have had different survival chances compared to those traveling with families.

---

### 3.3 Fare Per Person

This feature distributes the ticket fare across the family members.

Formula:

FarePerPerson = Fare / FamilySize

This helps normalize the ticket cost and provides better insight into the passenger's economic status.

---

### 3.4 Age–Fare Interaction

An interaction feature was created between age and fare.

Formula:

AgeFare = Age × Fare

This feature captures combined effects of age and economic class on survival probability.

---

### 3.5 Age Squared

This feature introduces non-linearity in age relationships.

Formula:

AgeSquared = Age²

Sometimes survival probability does not change linearly with age, so polynomial transformations help the model capture more complex patterns.

---

### 3.6 Log Transformation of Fare

Ticket fares were highly skewed, meaning most passengers paid small amounts while a few paid very large amounts.

To reduce skewness:

FareLog = log(1 + Fare)

Log transformation compresses large values and makes the distribution more normal.

---

### 3.7 Age Group

Age was converted into categorical groups.

Age groups used:

* 0–12 → Child
* 12–18 → Teen
* 18–40 → Adult
* 40–60 → Middle-aged
* 60+ → Senior

Grouping helps models capture behavioral differences across age categories.

---

### 3.8 Fare Category

Fare values were divided into categories using binning.

Example categories:

* Low fare
* Medium fare
* High fare
* Premium fare

This allows the model to detect class-level travel patterns.

---

### 3.9 Family Interaction Feature

Interaction between siblings/spouses and parents/children:

FamilyInteraction = SibSp × Parch

This captures more complex family structure relationships.

---

### 3.10 Age Per Family

This feature measures how age relates to family size.

Formula:

AgePerFamily = Age / FamilySize

It helps represent family composition more accurately.

---

# 4. Removal of High Cardinality Columns

Certain columns were removed because they contain extremely high numbers of unique values and provide little predictive value.

Removed columns:

* PassengerId
* Name
* Ticket
* Cabin

Reasons:

1. These columns mostly contain unique identifiers.
2. One-hot encoding them creates hundreds of unnecessary features.
3. They increase model complexity and risk overfitting.

---

# 5. Categorical Encoding

Categorical variables must be converted into numerical format before training machine learning models.

One-Hot Encoding was applied using:

pd.get_dummies()

Example:

Sex column:

Male → Sex_male = 1
Female → Sex_male = 0

Embarked column:

Embarked_S
Embarked_Q
Embarked_C

Drop-first encoding was used to avoid multicollinearity.

---

# 6. Feature Scaling

Feature scaling ensures that numerical variables are on similar ranges so that machine learning algorithms can perform better.

Standardization was applied using:

StandardScaler

Formula:

Scaled Value = (X − Mean) / Standard Deviation

Scaling was applied to all numeric features except the target variable.

---

# 7. Train-Test Split

The dataset was divided into training and testing sets to evaluate model performance on unseen data.

Split ratio used:

* Training data → 80%
* Testing data → 20%

Random state used: 42

This ensures reproducibility of results.

---

# 8. Feature Selection

Feature selection helps remove irrelevant or redundant variables and keeps only the most important features.

Mutual Information was used to measure dependency between each feature and the target variable.

Method used:

mutual_info_classif()

Higher mutual information score indicates a stronger relationship between a feature and survival outcome.

The top 15 most informative features were selected and stored in a JSON file.

---

# 9. Selected Features

The following top features were selected:

* Sex_male
* FarePerPerson
* Fare
* FareCategory_1
* Pclass
* FamilySize
* Embarked_S
* Age
* FareLog
* AgeFare
* AgePerFamily
* Embarked_Q
* AgeGroup_4
* SibSp
* AgeGroup_3

These features provide meaningful information related to passenger demographics, ticket class, family structure, and economic status.

---

# 10. Output Artifacts

The feature engineering pipeline generates the following outputs:

1. Engineered dataset with new features
2. Feature importance visualization
3. Selected feature list saved in:

features/feature_list.json

This file will be used in the next stage of the pipeline for model training.

---

# 11. Conclusion

Feature engineering significantly enhances the predictive power of machine learning models by transforming raw data into informative features.

In this project:

* Multiple interaction features were created
* Skewed data was transformed
* Categorical variables were encoded
* Numerical features were scaled
* Mutual information was used to select the most relevant features

These steps ensure that the dataset is properly prepared for building accurate and robust machine learning models in the next stage of the project.
