import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

RAW_PATH = "data/raw/dataset.csv"
PROCESSED_PATH = "data/processed/final.csv"


def load_data():
    df = pd.read_csv(RAW_PATH)
    print("Data Loaded")
    return df


def remove_duplicates(df):
    df = df.drop_duplicates()
    print("Duplicates Removed")
    return df


def handle_missing(df):

    # numeric columns interpolation
    for col in df.select_dtypes(include='number').columns:
        #df[col] = df[col].interpolate(method='linear')
        df[col] = df[col].fillna(df[col].median())

    # categorical columns
    for col in df.select_dtypes(include=['object','string']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    print("Missing Values Handled")

    return df


def remove_outliers(df):
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df = df[(df[col] >= lower) & (df[col] <= upper)]

    print("Outliers Removed")
    return df


def scale_data(df):
    scaler = StandardScaler()

    numeric_cols = df.select_dtypes(include=np.number).columns

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    print("Data Scaled")

    return df


def save_data(df):
    df.to_csv(PROCESSED_PATH, index=False)
    print("Processed Data Saved")


def run_pipeline():
    df = load_data()
    df = remove_duplicates(df)
    df = handle_missing(df)
    df = remove_outliers(df)
    df = scale_data(df)
    save_data(df)


if __name__ == "__main__":
    run_pipeline()