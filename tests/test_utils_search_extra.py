import pytest
from app.utils_search import buscar_info_rapida
from app.models.vastec import VastecKnowledge, Metadata, CompanyProfile, Headquarters, MissionVision, Leadership, ProductsServices, MarketPresence, DistributionChannels, CorporateHistoryItem, FinancialHighlights, ContactInformation, ContactInfoItem, FAQItem

def dummy_knowledge():
    return VastecKnowledge(
        metadata=Metadata(generated_at="2025-08-04", compiler="pytest", scope="test"),
        company_profile=CompanyProfile(legal_name="Vastec S.A.", brand_name="Vastec", ruc="1234567890", industry_classification="TI", date_incorporation="1990-01-01", brand_first_use="1990-01-01", parent_entity="Vastec Group"),
        headquarters=Headquarters(address="Calle Falsa 123", local_phone="0999999999", support_phone="1888888888", email_sales="ventas@vastec.com", email_support="soporte@vastec.com", website="https://vastec.com"),
        mission_vision=MissionVision(mission="Innovar", vision="Liderar"),
        leadership=Leadership(current_general_manager="Juan Pérez", other_key_executives=[{"name": "Ana", "position": "CTO"}], former_general_managers=[{"name": "Luis", "position": "Ex-GM"}]),
        certifications=["ISO 9001"],
        alliances=["HP"],
        products_services=ProductsServices(computo=["PC"], soluciones_ti=["Cloud"], perifericos=["Mouse"], caracteristicas_clave={"garantia": "2 años"}),
        market_presence=MarketPresence(primary_segments=["Empresas"], market_share={"Ecuador": "30%"}, sales_growth_cagr_2015_2020="10%"),
        distribution_channels=DistributionChannels(strategy="Directo", national_distributor="DistribuidorX", retail_partners=["Partner1"], authorized_reseller_network="RedX"),
        corporate_history=[CorporateHistoryItem(date="1990-01-01", event="Fundación")],
        financial_highlights=FinancialHighlights(revenue_growth_estimate="15%", key_metrics={"ventas": "100M"}),
        contact_information=ContactInformation(sales=ContactInfoItem(phone="0999999999", email="ventas@vastec.com", hours="9-18"), technical_support=ContactInfoItem(phone="1888888888", email="soporte@vastec.com", hours="24/7")),
        limitations=["Ninguna"],
        frequently_asked_questions=[FAQItem(id=1, question="¿Garantía?", answer="2 años")]
    )

def test_buscar_info_rapida_producto():
    k = dummy_knowledge()
    r = buscar_info_rapida(k, "¿Qué productos ofrece Vastec?")
    assert "PC" in r

def test_buscar_info_rapida_garantia():
    k = dummy_knowledge()
    r = buscar_info_rapida(k, "¿Cuál es la garantía?")
    assert "2 años" in r

def test_buscar_info_rapida_certificaciones():
    k = dummy_knowledge()
    r = buscar_info_rapida(k, "¿Qué certificaciones tiene la empresa?")
    assert "ISO 9001" in r

def test_buscar_info_rapida_gerente():
    k = dummy_knowledge()
    r = buscar_info_rapida(k, "¿Quién es el gerente general?")
    assert "Juan Pérez" in r

def test_buscar_info_rapida_no_match():
    k = dummy_knowledge()
    r = buscar_info_rapida(k, "¿Qué opinas del clima?")
    assert "No se tiene información" in r
