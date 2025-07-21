import joblib
import numpy as np

model = joblib.load("model.joblib")


def predict(data: dict):
    features = np.array([list(data.values())])
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}
