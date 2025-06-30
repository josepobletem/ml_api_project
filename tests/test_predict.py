from unittest.mock import patch

def test_prediction(client, headers):
    payload = {"feature1": 1, "feature2": 2}

    with patch("ml_pipeline.predictor.predict") as mock_predict:
        mock_predict.return_value = {"prediction": [1]}
        response = client.post("/predict/", json=payload, headers=headers)

    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], list)
