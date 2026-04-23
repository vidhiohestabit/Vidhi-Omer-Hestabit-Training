import pandas as pd
import json
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv("../data/processed/train.csv")
test = pd.read_csv("../data/processed/test.csv")

X_train = train.drop("Survived", axis=1)
y_train = train["Survived"]

X_test = test.drop("Survived", axis=1)
y_test = test["Survived"]

models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(),
    "XGBoost": XGBClassifier(eval_metric="logloss"),
    "NeuralNetwork": MLPClassifier(hidden_layer_sizes=(64,32), max_iter=500)
}

results = {}

best_model = None
best_score = 0

for name, model in models.items():

    cv_scores = cross_val_score(model, X_train, y_train, cv=5)

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:,1]

    metrics = {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds),
        "recall": recall_score(y_test, preds),
        "f1_score": f1_score(y_test, preds),
        "roc_auc": roc_auc_score(y_test, probs)
    }

    results[name] = metrics

    if metrics["f1_score"] > best_score:
        best_score = metrics["f1_score"]
        best_model = model
        best_preds = preds

cm = confusion_matrix(y_test, best_preds)

sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.show()

joblib.dump(best_model, "../models/best_model.pkl")

with open("../evaluation/metrics.json", "w") as f:
    json.dump(results, f, indent=4)

print("Best model saved")