import pytest
from app.claude_client import ClaudeClient

class DummyClaudeClient(ClaudeClient):
    def send_message(self, prompt, max_tokens=512, retries=3, backoff=1.0):
        # Simula diferentes respuestas y errores
        if prompt == "error":
            raise RuntimeError("Simulación de error")
        if prompt == "choices":
            return "Respuesta de choices"
        return "Respuesta simulada"

def test_send_message_ok(monkeypatch):
    client = DummyClaudeClient(api_key="test")
    assert client.send_message("hola") == "Respuesta simulada"

def test_send_message_error(monkeypatch):
    client = DummyClaudeClient(api_key="test")
    with pytest.raises(RuntimeError):
        client.send_message("error")

def test_api_key_empty():
    with pytest.raises(RuntimeError):
        ClaudeClient(api_key="")

def test_api_key_none(monkeypatch):
    monkeypatch.setattr('os.getenv', lambda k, default=None: None)
    with pytest.raises(RuntimeError):
        ClaudeClient()
