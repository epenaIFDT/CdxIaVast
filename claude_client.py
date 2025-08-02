"""
Cliente para la API Claude Haiku 3.5
"""

import os
import time
import requests
from typing import Optional

CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

class ClaudeClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("CLAUDE_API_KEY")
        if not self.api_key:
            raise RuntimeError("No se encontró la clave CLAUDE_API_KEY.")

    def send_message(self, prompt: str, max_tokens: int = 512, retries: int = 3, backoff: float = 1.0) -> str:
        headers = {
            "x-api-key": self.api_key,
            "content-type": "application/json"
        }
        payload = {
            "model": "claude-3-haiku-20240229",
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
                return data.get("content", "[Sin respuesta]")
            except Exception as e:
                if attempt < retries - 1:
                    time.sleep(backoff * (2 ** attempt))
                else:
                    raise RuntimeError(f"Error al consultar Claude: {e}")
