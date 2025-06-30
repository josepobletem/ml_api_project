from ml_pipeline.metrics import evaluate_model
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def test_evaluate_model():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)
    model = RandomForestClassifier().fit(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)

    assert "accuracy" in metrics
    assert 0.0 <= metrics["accuracy"] <= 1.0
