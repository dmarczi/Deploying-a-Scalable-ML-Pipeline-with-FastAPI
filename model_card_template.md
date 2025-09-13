# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Uses Random Forest from scikit-learn with estimators set to 100 and random state to 42.

## Intended Use
Seems to be intended for predicting if an individuals salary is more more than 50k a year based on census data.

## Training Data
The odel was trained on the census.csv dataset. 

## Evaluation Data
20% of census.csv data was used as the test set.

## Metrics
Metrics include precision at 0.7391, recall at 0.6384, and F1 at 0.6851.

## Ethical Considerations
Model can possibly reflect biases present in the training data.

## Caveats and Recommendations
Use this model for practice and demonstration only.
