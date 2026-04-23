import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif


def select_features(X_train, y_train):

    # Calculate mutual information
    mi = mutual_info_classif(X_train, y_train)

    mi_scores = pd.Series(mi, index=X_train.columns)

    # Plot feature importance
    mi_scores.sort_values().plot(kind="barh")

    plt.title("Feature Importance")

    plt.xlabel("Mutual Information Score")

    plt.ylabel("Features")

    plt.show()

    # Select top 15 features
    selected_features = mi_scores.sort_values(ascending=False).head(15).index

    print("Top Features Selected")

    return selected_features


def save_features(features):

    with open("../features/feature_list.json", "w") as f:
        json.dump(list(features), f, indent=4)

    print("Feature List Saved")