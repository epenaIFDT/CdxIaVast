# Modelos pydantic y entidades para Vastec

# Modelos pydantic y entidades para Vastec
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class Metadata(BaseModel):
    generated_at: str
    compiler: str
    scope: str

class CompanyProfile(BaseModel):
    legal_name: str
    brand_name: str
    ruc: str
    industry_classification: str
    date_incorporation: str
    brand_first_use: str
    parent_entity: str

class Headquarters(BaseModel):
    address: str
    local_phone: str
    support_phone: str
    email_sales: str
    email_support: str
    website: str

class MissionVision(BaseModel):
    mission: str
    vision: str

class Leadership(BaseModel):
    current_general_manager: str
    other_key_executives: List[Dict[str, str]]
    former_general_managers: List[Dict[str, str]]

class ProductsServices(BaseModel):
    computo: List[str]
    soluciones_ti: List[str]
    perifericos: List[str]
    caracteristicas_clave: Dict[str, Any]

class MarketPresence(BaseModel):
    primary_segments: List[str]
    market_share: Dict[str, str]
    sales_growth_cagr_2015_2020: str

class DistributionChannels(BaseModel):
    strategy: str
    national_distributor: str
    retail_partners: List[str]
    authorized_reseller_network: str

class CorporateHistoryItem(BaseModel):
    date: str
    event: str

class FinancialHighlights(BaseModel):
    revenue_growth_estimate: str
    key_metrics: Dict[str, str]

class ContactInfoItem(BaseModel):
    phone: str
    email: str
    hours: str

class ContactInformation(BaseModel):
    sales: ContactInfoItem
    technical_support: ContactInfoItem

class FAQItem(BaseModel):
    id: int
    question: str
    answer: str

class VastecKnowledge(BaseModel):
    metadata: Metadata
    company_profile: CompanyProfile
    headquarters: Headquarters
    mission_vision: MissionVision
    leadership: Leadership
    certifications: List[str]
    alliances: List[str]
    products_services: ProductsServices
    market_presence: MarketPresence
    distribution_channels: DistributionChannels
    corporate_history: List[CorporateHistoryItem]
    financial_highlights: FinancialHighlights
    contact_information: ContactInformation
    limitations: List[str]
    frequently_asked_questions: List[FAQItem]
