import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import os

# create evaluation folder
os.makedirs("../../evaluation", exist_ok=True)

# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv("../../data/raw/titanic.csv")

# -------------------------
# Drop text columns
# -------------------------
df = df.drop(columns=["Name", "Ticket", "Cabin"], errors="ignore")

# -------------------------
# Encode categorical columns
# -------------------------
if "Sex" in df.columns:
    df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# -------------------------
# Fill missing values
# -------------------------
df = df.fillna(df.mean(numeric_only=True))

# -------------------------
# Features / Target
# -------------------------
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Ensure ALL columns numeric
X = X.select_dtypes(include=["int64", "float64", "bool"])

# -------------------------
# Load trained model
# -------------------------
with open("../../models/best_model.pkl", "rb") as f:
    model = pickle.load(f)

# -------------------------
# SHAP explainability
# -------------------------
explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

# -------------------------
# SHAP summary plot
# -------------------------
shap.summary_plot(shap_values, X, show=False)
plt.savefig("../../evaluation/shap_summary.png")
plt.clf()

# -------------------------
# Feature importance
# -------------------------
shap.summary_plot(shap_values, X, plot_type="bar", show=False)
plt.savefig("../../evaluation/feature_importance.png")
plt.clf()

# -------------------------
# Error heatmap
# -------------------------
predictions = model.predict(X)

cm = confusion_matrix(y, predictions)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Error Analysis Heatmap")

plt.savefig("../../evaluation/error_heatmap.png")
plt.clf()

print("SHAP analysis completed successfully")
print("Results saved in evaluation folder")