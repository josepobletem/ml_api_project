from unittest.mock import MagicMock, patch

from api.chatbot.feedback import save_feedback


def test_save_feedback():
    with patch("api.chatbot.feedback.sqlite3.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        save_feedback("¿Qué es IA?", "Es la simulación de inteligencia humana.")

        mock_cursor.execute.assert_any_call(
            "CREATE TABLE IF NOT EXISTS feedback (question TEXT, response TEXT)"
        )
        mock_cursor.execute.assert_any_call(
            "INSERT INTO feedback VALUES (?, ?)",
            ("¿Qué es IA?", "Es la simulación de inteligencia humana."),
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()
