from pathlib import Path

import joblib

MODEL_PATH = Path("models")
MODEL_PATH.mkdir(exist_ok=True)


def save_model(model, filename: str = "model.joblib"):
    """Guarda un modelo entrenado."""
    joblib.dump(model, MODEL_PATH / filename)


def load_model(filename: str = "model.joblib"):
    """Carga un modelo entrenado."""
    return joblib.load(MODEL_PATH / filename)


def save_preprocessor(preprocessor, filename: str = "preprocessor.joblib"):
    """Guarda el preprocesador."""
    joblib.dump(preprocessor, MODEL_PATH / filename)


def load_preprocessor(filename: str = "preprocessor.joblib"):
    """Carga el preprocesador."""
    return joblib.load(MODEL_PATH / filename)
