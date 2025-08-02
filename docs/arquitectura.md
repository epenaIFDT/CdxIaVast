# Arquitectura lógica

```
┌──────────────────┐
│ vas...json       │
└─────────▲────────┘
          │ pydantic model
┌─────────┴──────────────┐
│ ContextManager         │
└─────────▲──────────────┘
          │ dict
┌─────────┴──────────┐  HTTP POST  ┌─────────────────┐
│ ChatService        │───────────▶│ Claude API 3.5  │
│  • build_prompt    │            └─────────────────┘
│  • parse_response  │
└─────────▲──────────┘
          │ text
┌─────────┴──────────┐
│ CLI (chat.py)      │
│  • Rich Console    │
│  • /reload cmd     │
└────────────────────┘
```

## Componentes
- `chat.py`: CLI principal
- `context_loader.py`: carga y validación de conocimiento
- `claude_client.py`: integración API Claude
- `intents.py`: categorización de preguntas
- `logs/`: registro de interacciones
- `tests/`: pruebas unitarias
- `.github/workflows/ci.yml`: integración continua

## Flujo de operación
1. Carga conocimiento JSON
2. Detecta intención/categoría
3. Construye prompt y consulta a Claude
4. Muestra respuesta y registra log
