from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
import uuid
import os
import csv
from datetime import datetime

app = FastAPI()

# Load model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


# Input schema
class Passenger(BaseModel):
    Pclass: float
    Age: float
    SibSp: float
    Parch: float
    Fare: float
    Sex_male: float
    Embarked_S: float


@app.get("/")
def home():
    return {"message": "Titanic Model API Running"}



@app.post("/predict")
def predict(passenger: Passenger):

    request_id = str(uuid.uuid4())

    # base dataframe
    df = pd.DataFrame([passenger.dict()])

    # -------- Feature Engineering --------
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    df["FarePerPerson"] = df["Fare"] / df["FamilySize"]
    df["AgeFare"] = df["Age"] * df["Fare"]
    df["AgeSquared"] = df["Age"] ** 2
    df["FareLog"] = np.log1p(df["Fare"])
    df["FamilyInteraction"] = df["SibSp"] * df["Parch"]
    df["AgePerFamily"] = df["Age"] / df["FamilySize"]

    # Embarked_Q (missing from input)
    df["Embarked_Q"] = 0

    # Age Groups
    df["AgeGroup_1"] = (df["Age"] <= 12).astype(int)
    df["AgeGroup_2"] = ((df["Age"] > 12) & (df["Age"] <= 20)).astype(int)
    df["AgeGroup_3"] = ((df["Age"] > 20) & (df["Age"] <= 40)).astype(int)
    df["AgeGroup_4"] = (df["Age"] > 40).astype(int)

    # Fare Categories
    df["FareCategory_1"] = (df["Fare"] <= 10).astype(int)
    df["FareCategory_2"] = ((df["Fare"] > 10) & (df["Fare"] <= 30)).astype(int)
    df["FareCategory_3"] = (df["Fare"] > 30).astype(int)

    feature_order = [
        'Pclass','Age','SibSp','Parch','Fare',
        'FamilySize','IsAlone','FarePerPerson','AgeFare','AgeSquared',
        'FareLog','FamilyInteraction','AgePerFamily',
        'Sex_male','Embarked_Q','Embarked_S',
        'AgeGroup_1','AgeGroup_2','AgeGroup_3','AgeGroup_4',
        'FareCategory_1','FareCategory_2','FareCategory_3'
    ]

    df = df[feature_order]

    prediction = model.predict(df)[0]

    log_file = "./src/logs/prediction_logs.csv"

    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)

        # header create if file empty
        if not file_exists:
            writer.writerow([
                "request_id",
                "timestamp",
                "Pclass",
                "Age",
                "SibSp",
                "Parch",
                "Fare",
                "Sex_male",
                "Embarked_S",
                "prediction"
            ])

        writer.writerow([
            request_id,
            datetime.now(),
            passenger.Pclass,
            passenger.Age,
            passenger.SibSp,
            passenger.Parch,
            passenger.Fare,
            passenger.Sex_male,
            passenger.Embarked_S,
            prediction
        ])

    return {
        "request_id": request_id,
        "prediction": int(prediction)
    }