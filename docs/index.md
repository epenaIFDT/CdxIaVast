# Documentación técnica Chatbot Vastec

## Guía rápida de despliegue

1. Clona el repositorio o abre github.dev/Codespaces.
2. Crea el archivo `.env` con tu clave Claude:
   ```bash
   echo "CLAUDE_API_KEY=sk-..." >> .env
   ```
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta el chatbot:
   ```bash
   python chat.py
   ```

## Documentos
- [Arquitectura](arquitectura.md)
- [Guía de uso](uso.md)
- [Seguridad](seguridad.md)
- [Pruebas y cobertura](tests.md)
