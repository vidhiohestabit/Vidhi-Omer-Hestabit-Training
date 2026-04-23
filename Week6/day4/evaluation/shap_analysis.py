import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import seaborn as sns
import os


TRAIN_PATH = "../data/processed/train.csv"
MODEL_PATH = "../models/best_model.pkl"
EVAL_PATH = "../evaluation"

os.makedirs(EVAL_PATH, exist_ok=True)

# -----------------------
# Load processed train dataset
# -----------------------
df = pd.read_csv(TRAIN_PATH)

# Drop target column to get features
X = df.drop(columns=["Survived"], errors="ignore")
y = df["Survived"]

# Ensure all numeric (already processed)
X = X.select_dtypes(include=["int64", "float64", "bool"])

# -----------------------
# Load trained model
# -----------------------
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# -----------------------
# SHAP explainability
# -----------------------
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# -----------------------
# Summary plot
# -----------------------
shap.summary_plot(shap_values, X, show=False)
plt.savefig(f"{EVAL_PATH}/shap_summary.png")
plt.clf()

# Feature importance bar plot
shap.summary_plot(shap_values, X, plot_type="bar", show=False)
plt.savefig(f"{EVAL_PATH}/feature_importance.png")
plt.clf()

# -----------------------
# Error heatmap
# -----------------------
predictions = model.predict(X)
cm = pd.crosstab(y, predictions, rownames=["Actual"], colnames=["Predicted"])

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Error Analysis Heatmap")
plt.savefig(f"{EVAL_PATH}/error_heatmap.png")
plt.clf()

print("SHAP analysis completed successfully. Check the evaluation folder.")