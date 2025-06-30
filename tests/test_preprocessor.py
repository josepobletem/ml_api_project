from ml_pipeline.preprocessor import build_preprocessor
import pandas as pd

def test_preprocessor():
    df = pd.DataFrame({
        "num": [1, 2, None],
        "cat": ["a", "b", "a"]
    })

    preprocessor = build_preprocessor(["num"], ["cat"])
    result = preprocessor.fit_transform(df)

    assert result.shape[0] == 3
    assert result.shape[1] >= 2
