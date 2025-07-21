# train_model.py

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Cargar datos
X, y = load_iris(return_X_y=True)

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, "model.joblib")

print("✅ Modelo guardado como model.joblib")