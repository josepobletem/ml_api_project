from unittest.mock import patch

import pytest


@pytest.fixture
def mock_openai_response():
    with patch("api.chatbot.prompts.openai.ChatCompletion.create") as mock_create:
        mock_create.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "La inteligencia artificial es la simulación de procesos de inteligencia humana por máquinas."
                    }
                }
            ]
        }
        yield mock_create


def test_chatbot(client, auth_token, mock_openai_response):
    headers = {"Authorization": f"Bearer {auth_token}"}
    question = "¿Qué es inteligencia artificial?"
    response = client.post("/chatbot/", params={"question": question}, headers=headers)

    assert response.status_code == 200
    assert "response" in response.json()
    assert "inteligencia artificial" in response.json()["response"].lower()
