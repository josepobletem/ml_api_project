from ml_pipeline.model_registry import save_model, load_model
from sklearn.linear_model import LogisticRegression

def test_model_save_and_load(tmp_path):
    model = LogisticRegression()
    path = tmp_path / "model.joblib"
    save_model(model, path)
    loaded = load_model(path)

    assert hasattr(loaded, "predict")
