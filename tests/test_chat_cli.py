import pytest
from ..intents import detect_intent

def test_categoria_chat():
    assert detect_intent("¿Qué certificaciones tiene Vastec?") == "Institucional"
