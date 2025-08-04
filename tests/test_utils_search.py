from types import SimpleNamespace
from app.utils_search import buscar_info_rapida


def test_buscar_info_rapida_case_insensitive():
    knowledge = SimpleNamespace(
        leadership=SimpleNamespace(
            current_general_manager="Juan Pérez",
            other_key_executives=[SimpleNamespace(name="Ana", position="CTO")],
        )
    )
    # Pregunta en mayúsculas para asegurarnos de que la función no sea case sensitive
    resultado = buscar_info_rapida(knowledge, "QUIÉN ES EL GERENTE GENERAL?")
    assert "Gerente general: Juan Pérez" in resultado
