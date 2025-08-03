# CdxIaVast

## Estructura del proyecto

- `app/` : Backend FastAPI y lógica principal
- `app/models/vastec.py` : Modelos pydantic
- `data/` : Base de conocimiento y plantillas
- `frontend/` : Interfaz web
- `logs/` : Archivos de logs
- `tests/` : Pruebas unitarias

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.api:app --reload
```

## Uso

- Accede a `/frontend.html` para la interfaz web
- Usa `/consulta` para consultas vía API

## Notas
- Agrega tu clave Claude API en `.env`
