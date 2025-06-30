from ml_pipeline.trainer import train_model
import numpy as np

def test_train_model():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    model = train_model(X, y)
    assert hasattr(model, "predict")
