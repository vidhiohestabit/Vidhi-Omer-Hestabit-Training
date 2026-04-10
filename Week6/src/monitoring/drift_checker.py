import pandas as pd

TRAIN_DATA = "./src/data/raw/dataset.csv"
LOG_FILE = "./src/logs/prediction_logs.csv"

train = pd.read_csv(TRAIN_DATA)

try:
    logs = pd.read_csv(LOG_FILE)
except:
    print("No prediction logs yet")
    exit()

print("Training data size:", train.shape)
print("Prediction logs:", logs.shape)

print("\nBasic monitoring report")
print("Total predictions:", len(logs))

print("\nDrift check")
print("Train Age mean:", train["Age"].mean())
print("Logs Age mean:", logs["Age"].mean())