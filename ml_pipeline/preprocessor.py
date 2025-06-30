import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def build_preprocessor(numeric_features, categorical_features):
    """Construye un preprocesador de columnas numéricas y categóricas."""
    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_pipeline, numeric_features),
        ("cat", categorical_pipeline, categorical_features)
    ])

    return preprocessor

def preprocess_fit_transform(df: pd.DataFrame, numeric_cols, categorical_cols):
    """Fit y transform del preprocesador sobre un DataFrame."""
    preprocessor = build_preprocessor(numeric_cols, categorical_cols)
    X = preprocessor.fit_transform(df)
    return X, preprocessor

def preprocess_transform(df: pd.DataFrame, preprocessor):
    """Transforma nuevos datos con el preprocesador ya fit."""
    return preprocessor.transform(df)
