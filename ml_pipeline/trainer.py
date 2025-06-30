import xgboost as xgb
import joblib
import os

def train_model(X, y, model_path="model.joblib", **xgb_params):
    """
    Entrena un modelo de XGBoost y lo guarda como archivo .joblib

    Args:
        X (array-like): Features de entrenamiento
        y (array-like): Labels de entrenamiento
        model_path (str): Ruta para guardar el modelo entrenado
        **xgb_params: Parámetros adicionales para el modelo XGBoost

    Returns:
        model: El modelo entrenado
    """
    model = xgb.XGBClassifier(**xgb_params)
    model.fit(X, y)
    joblib.dump(model, model_path)
    return model
