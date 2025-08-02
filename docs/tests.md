# Pruebas y cobertura

- Las pruebas unitarias se encuentran en `tests/` y cubren lógica de intents, carga de contexto y cliente Claude.
- Ejecuta los tests con:
  ```bash
  pytest
  ```
- La cobertura se mide con:
  ```bash
  coverage run -m pytest && coverage report -m
  ```
- El workflow CI exige cobertura ≥ 80 %.
