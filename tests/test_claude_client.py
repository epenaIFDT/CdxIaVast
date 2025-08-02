import pytest
from ..claude_client import ClaudeClient
import os

class DummyClaudeClient(ClaudeClient):
    def send_message(self, prompt, max_tokens=512, retries=3, backoff=1.0):
        return "Respuesta simulada"

def test_send_message_mock(monkeypatch):
    monkeypatch.setenv("CLAUDE_API_KEY", "sk-test")
    client = DummyClaudeClient()
    resp = client.send_message("Hola")
    assert resp == "Respuesta simulada"

# Test de error por falta de API key

def test_api_key_missing(monkeypatch):
    monkeypatch.delenv("CLAUDE_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        ClaudeClient()
