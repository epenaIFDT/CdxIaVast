"""
Reglas y keywords para categorizar preguntas
"""

from typing import Literal

CATEGORIAS = {
    "Atención Cliente": ["garantía", "horario", "comprar", "soporte", "servicio"],
    "Comercial": ["catálogo", "precio", "diferencia", "comparación", "modelo", "producto"],
    "Técnico": ["ticket", "rma", "registro", "reparar", "fallo", "problema", "faq"],
    "Institucional": ["historia", "misión", "alianza", "certificación", "certificaciones", "socio", "empresa"]
}

def detect_intent(text: str) -> Literal["Atención Cliente", "Comercial", "Técnico", "Institucional", "Otro"]:
    t = text.lower()
    for categoria, keywords in CATEGORIAS.items():
        if any(k in t for k in keywords):
            return categoria
    return "Otro"
