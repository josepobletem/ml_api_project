import pandas as pd

from ml_pipeline.data_loader import load_data_from_csv


def test_load_data_from_csv(tmp_path):
    test_file = tmp_path / "sample.csv"
    expected_df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    expected_df.to_csv(test_file, index=False)

    result = load_data_from_csv(str(test_file))
    pd.testing.assert_frame_equal(result, expected_df)
