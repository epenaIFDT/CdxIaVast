"""
Cliente para la API Claude Haiku 3.5
"""


import os
import time
import requests
from typing import Optional
from dotenv import load_dotenv

CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

class ClaudeClient:
    def __init__(self, api_key: Optional[str] = None):
        # Usar solo variable de entorno, compatible con GitHub Actions Secrets
        self.api_key = api_key if api_key is not None else os.getenv("CLAUDE_API_KEY")
        if self.api_key is None or self.api_key.strip() == "":
            raise RuntimeError("No se encontró la clave CLAUDE_API_KEY.")

    def send_message(self, prompt: str, max_tokens: int = 512, retries: int = 3, backoff: float = 1.0) -> str:
        headers = {
            "x-api-key": self.api_key,
            "content-type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        payload = {
            "model": "claude-3-haiku-20240307",
            "max_tokens": max_tokens,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        for attempt in range(retries):
            try:
                resp = requests.post(CLAUDE_API_URL, headers=headers, json=payload, timeout=10)
                resp.raise_for_status()
                data = resp.json()
                # Claude API responde con 'content' dentro de 'content' o 'choices', según versión
                if "content" in data:
                    return data["content"]
                elif "choices" in data and data["choices"]:
                    return data["choices"][0]["message"]["content"]
                return "[Sin respuesta: formato desconocido]"
            except Exception as e:
                # Si es error HTTP, mostrar el cuerpo para depuración
                if hasattr(e, 'response') and e.response is not None:
                    try:
                        error_body = e.response.text
                    except Exception:
                        error_body = str(e)
                    msg = f"Error al consultar Claude: {e} | Respuesta: {error_body}"
                else:
                    msg = f"Error al consultar Claude: {e}"
                if attempt < retries - 1:
                    time.sleep(backoff * (2 ** attempt))
                else:
                    raise RuntimeError(msg)
