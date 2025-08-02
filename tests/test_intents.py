from ..intents import detect_intent

def test_detect_intent_cliente():
    assert detect_intent("¿Cuál es la garantía?") == "Atención Cliente"

def test_detect_intent_comercial():
    assert detect_intent("Comparación DesignPro vs Station Pro") == "Comercial"

def test_detect_intent_tecnico():
    assert detect_intent("¿Cómo registro un RMA?") == "Técnico"

def test_detect_intent_institucional():
    assert detect_intent("¿Con qué socios tecnológicos trabaja Vastec?") == "Institucional"

def test_detect_intent_otro():
    assert detect_intent("¿Qué opinas del clima?") == "Otro"
