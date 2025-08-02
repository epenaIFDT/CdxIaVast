# Seguridad y privacidad

- La clave de API Claude nunca se sube al repositorio.
- Se utiliza `.env` local o GitHub Secret (`CLAUDE_API_KEY`).
- Las entradas del usuario se sanitizan antes de enviarse a la API.
- Los logs se almacenan localmente, con rotación diaria y sin datos personales.
- El código sigue buenas prácticas PEP 8 y tipado estricto.
