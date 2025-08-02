import pytest
from ..context_loader import load_knowledge, VastecKnowledge
import json

def test_load_knowledge_valido(tmp_path):
    data = {
        "empresa": "Vastec",
        "productos": [{"nombre": "DesignPro"}],
        "faq": [{"pregunta": "¿Garantía?", "respuesta": "2 años"}],
        "institucional": {"historia": "Desde 1990", "mision": "Innovar", "alianzas": ["HP"], "certificaciones": ["ISO 9001"]}
    }
    f = tmp_path / "vastec_knowledge.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    k = load_knowledge(str(f))
    assert isinstance(k, VastecKnowledge)
    assert k.empresa == "Vastec"
    assert k.productos[0].nombre == "DesignPro"
    assert k.faq[0].respuesta == "2 años"
    assert "ISO 9001" in k.institucional.certificaciones

def test_load_knowledge_invalido(tmp_path):
    data = {"empresa": "Vastec"}  # falta campos obligatorios
    f = tmp_path / "vastec_knowledge.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(Exception):
        load_knowledge(str(f))
