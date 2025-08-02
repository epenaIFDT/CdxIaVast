import re

def sanitize_input(text: str) -> str:
    # Elimina bloques <script>...</script> completamente
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL|re.IGNORECASE)
    # Elimina cualquier otra etiqueta HTML
    text = re.sub(r'<.*?>', '', text)
    # Elimina comillas y caracteres especiales
    text = re.sub(r'["\'`]', '', text)
    # Elimina saltos de línea y retorno de carro
    text = re.sub(r'[\r\n]', ' ', text)
    return text.strip()
