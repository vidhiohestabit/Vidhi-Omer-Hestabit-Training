import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from feature_selector import select_features, save_features


def load_data():
    df = pd.read_csv("../data/processed/final.csv")
    return df


def create_features(df):

    # 1 Family size
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    # 2 Is alone
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    # 3 Fare per person
    df["FarePerPerson"] = df["Fare"] / df["FamilySize"]

    # 4 Age * Fare interaction
    df["AgeFare"] = df["Age"] * df["Fare"]

    # 5 Age square
    df["AgeSquared"] = df["Age"] ** 2

    # 6 Fare log
    df["FareLog"] = np.log1p(df["Fare"].clip(lower=0))

    # 7 Age group
    df["AgeGroup"] = pd.cut(df["Age"], bins=[0,12,18,40,60,100], labels=[0,1,2,3,4])

    # 8 Fare category
    df["FareCategory"] = pd.cut(df["Fare"], bins=4, labels=[0,1,2,3])

    # 9 Family interaction
    df["FamilyInteraction"] = df["SibSp"] * df["Parch"]

    # 10 Age per family
    df["AgePerFamily"] = df["Age"] / df["FamilySize"]

    df = df.drop(["Name", "Ticket", "Cabin", "PassengerId"], axis=1)

    print("New Features Created")

    return df


def encode_features(df):

    df = pd.get_dummies(df, drop_first=True)

    print("Categorical Encoding Done")

    return df


def scale_features(df):

    scaler = StandardScaler()

    numeric_cols = df.select_dtypes(include=np.number).columns

    # target column remove karo
    numeric_cols = numeric_cols.drop("Survived")

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    print("Features Scaled")

    return df


def split_data(df):

    X = df.drop("Survived", axis=1)
    y = df["Survived"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Train Test Split Done")

    return X_train, X_test, y_train, y_test

def save_datasets(X_train, X_test, y_train, y_test):

    train = X_train.copy()
    train["Survived"] = y_train

    test = X_test.copy()
    test["Survived"] = y_test

    train.to_csv("../data/processed/train.csv", index=False)
    test.to_csv("../data/processed/test.csv", index=False)

    print("Train and Test datasets saved")


if __name__ == "__main__":

    df = load_data()

    df = create_features(df)

    df = encode_features(df)

    df = scale_features(df)

    X_train, X_test, y_train, y_test = split_data(df)

    # FEATURE SELECTION
    features = select_features(X_train, y_train)

    # SAVE SELECTED FEATURES
    save_features(features)

    # SAVE TRAIN TEST DATA
    save_datasets(X_train, X_test, y_train, y_test)