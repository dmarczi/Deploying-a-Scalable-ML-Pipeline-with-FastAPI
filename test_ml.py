import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics
from train_model import train, test, X_train, y_train, X_test, y_test
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Testing that train_model is returning a RandomForestClassifieer
    """
    # Your code here
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), 'Model supposed to be a RandomForestClassifier'
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Testing that inference returns a numpy array with correct length
    """
    # Your code here
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    assert isinstance(preds, np.ndarray), 'Inference supposed to return NumPy array'
    assert len(preds) == len(y_test), 'Number of predictions supposed to match test samples'
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Testing that compute_model_metrics returns p, r, fbeta as floats
    """
    # Your code here
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)

    for metric in [precision, recall, fbeta]:
        assert isinstance(metric, float), 'Should be floats'
    pass
