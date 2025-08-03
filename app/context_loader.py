"""
Carga y validación del archivo vas...json usando pydantic
"""

from pydantic import ValidationError
import json
from app.models.vastec import VastecKnowledge

def load_knowledge(path: str) -> VastecKnowledge:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    try:
        return VastecKnowledge(**data)
    except ValidationError as e:
        raise RuntimeError(f"Error de validación en vas...json: {e}")
