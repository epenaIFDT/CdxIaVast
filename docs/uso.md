# Guía de uso

## Flujo básico

1. Instala dependencias y configura la clave Claude en `.env`.
2. Ejecuta `python chat.py`.
3. Realiza preguntas sobre Vastec, productos, soporte, institucional, etc.
4. Usa los comandos:
   - `/reload`: recarga el archivo de conocimiento JSON.
   - `/exit`: termina la sesión.
   - `/help`: muestra ayuda de comandos.

## Ejemplo de sesión
```
Tú > ¿Qué certificaciones tiene Vastec?
Categoría detectada: Institucional
Respuesta: ISO 9001:2015, ENERGY STAR Partner, Programa RAEE
```

## Recomendaciones
- No compartas tu clave Claude.
- El archivo de conocimiento puede actualizarse y recargarse en tiempo real.
- Los logs se almacenan localmente y no contienen datos personales.
