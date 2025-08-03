import pytest
from app.context_loader import load_knowledge
from app.models.vastec import VastecKnowledge
import json

def test_load_knowledge_valido(tmp_path):
    # JSON de prueba con todos los campos requeridos por VastecKnowledge
    data = {
        "metadata": {
            "generated_at": "2025-08-03T12:00:00Z",
            "compiler": "pytest",
            "scope": "test"
        },
        "company_profile": {
            "legal_name": "Vastec S.A.",
            "brand_name": "Vastec",
            "ruc": "1234567890",
            "industry_classification": "Tecnología",
            "date_incorporation": "1990-01-01",
            "brand_first_use": "1990-01-01",
            "parent_entity": "Vastec Group"
        },
        "headquarters": {
            "address": "Calle Falsa 123",
            "local_phone": "0999999999",
            "support_phone": "1888888888",
            "email_sales": "ventas@vastec.com",
            "email_support": "soporte@vastec.com",
            "website": "https://vastec.com"
        },
        "mission_vision": {
            "mission": "Innovar",
            "vision": "Liderar"
        },
        "leadership": {
            "current_general_manager": "Juan Pérez",
            "other_key_executives": [{"nombre": "Ana", "cargo": "CTO"}],
            "former_general_managers": [{"nombre": "Luis", "cargo": "Ex-GM"}]
        },
        "certifications": ["ISO 9001"],
        "alliances": ["HP"],
        "products_services": {
            "computo": ["PC", "Laptop"],
            "soluciones_ti": ["Cloud"],
            "perifericos": ["Mouse"],
            "caracteristicas_clave": {"fiabilidad": "alta"}
        },
        "market_presence": {
            "primary_segments": ["Empresas"],
            "market_share": {"Ecuador": "30%"},
            "sales_growth_cagr_2015_2020": "10%"
        },
        "distribution_channels": {
            "strategy": "Directo",
            "national_distributor": "DistribuidorX",
            "retail_partners": ["Partner1"],
            "authorized_reseller_network": "RedX"
        },
        "corporate_history": [
            {"date": "1990-01-01", "event": "Fundación"}
        ],
        "financial_highlights": {
            "revenue_growth_estimate": "15%",
            "key_metrics": {"ventas": "100M"}
        },
        "contact_information": {
            "sales": {"phone": "0999999999", "email": "ventas@vastec.com", "hours": "9-18"},
            "technical_support": {"phone": "1888888888", "email": "soporte@vastec.com", "hours": "24/7"}
        },
        "limitations": ["Ninguna"],
        "frequently_asked_questions": [
            {"id": 1, "question": "¿Garantía?", "answer": "2 años"}
        ]
    }
    f = tmp_path / "vastec_knowledge.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    k = load_knowledge(str(f))
    assert isinstance(k, VastecKnowledge)
    assert k.certifications[0] == "ISO 9001"
    assert k.metadata.compiler == "pytest"
    assert k.frequently_asked_questions[0].answer == "2 años"

def test_load_knowledge_invalido(tmp_path):
    data = {"empresa": "Vastec"}  # falta campos obligatorios
    f = tmp_path / "vastec_knowledge.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(Exception):
        load_knowledge(str(f))
