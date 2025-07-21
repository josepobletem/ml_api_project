from sklearn.linear_model import LogisticRegression

from ml_pipeline.model_registry import load_model, save_model


def test_model_save_and_load(tmp_path):
    model = LogisticRegression()
    path = tmp_path / "model.joblib"
    save_model(model, path)
    loaded = load_model(path)

    assert hasattr(loaded, "predict")
