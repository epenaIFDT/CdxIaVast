from app.utils import sanitize_input

def test_html_removal():
    assert sanitize_input('<b>hola</b>') == 'hola'

def test_js_removal():
    assert sanitize_input('<script>alert(1)</script>hola') == 'hola'

def test_special_chars():
    assert sanitize_input('¿Qué "certificación" tiene?') == '¿Qué certificación tiene?'

def test_newlines():
    assert sanitize_input('hola\n\r') == 'hola'
