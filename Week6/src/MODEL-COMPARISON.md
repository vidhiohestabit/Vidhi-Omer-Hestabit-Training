# Model Comparison

Four machine learning models were trained and evaluated using 5-fold cross-validation.

## Logistic Regression

Accuracy: 0.85
Precision: 0.79
Recall: 0.67
F1 Score: 0.73
ROC-AUC: 0.81

## Random Forest

Accuracy: 0.76
Precision: 0.60
Recall: 0.61
F1 Score: 0.61
ROC-AUC: 0.75

## XGBoost

Accuracy: 0.79
Precision: 0.65
Recall: 0.61
F1 Score: 0.63
ROC-AUC: 0.75

## Neural Network

Accuracy: 0.81
Precision: 0.72
Recall: 0.61
F1 Score: 0.66
ROC-AUC: 0.79

## Best Model

Logistic Regression achieved the best overall performance based on F1 Score and ROC-AUC.
Therefore it was selected as the final model and saved as `best_model.pkl`.
