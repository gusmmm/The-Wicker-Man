from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Dict
from datetime import date

class ClinicalCoding(BaseModel):
    system: str = Field(..., description="e.g., SNOMED-CT, LOINC, ICD-11")
    code: str
    display: str

class ScoreComponent(BaseModel):
    name: str
    coding: ClinicalCoding
    data_type: str = Field(..., description="float, int, or boolean")
    unit: Optional[str] = None
    description: Optional[str] = None

class ClinicalScore(BaseModel):
    # Metadata for the Repo
    id: str = Field(..., description="URL-friendly slug (e.g., revised-baux)")
    version: str = "1.0.0"
    created_at: date = Field(..., description="Date this record was first created (YYYY-MM-DD)")
    updated_at: date = Field(..., description="Date this record was last updated (YYYY-MM-DD)")
    
    
    # Clinical Identity (The 'What')
    title: str
    description: str
    links: Optional[Dict[str, HttpUrl]] = None
    aliases: List[str] = []
    
    # Primary Interoperability Mappings
    # LOINC is the 'Question/Test', SNOMED is the 'Finding/Entity'
    loinc_code: Optional[str] = Field(None, description="The LOINC code for the assessment")
    snomed_concept: str = Field(..., description="The SNOMED-CT Observable Entity code")
    omop_domain: str = "Measurement"
    
    # Data Inputs (The 'How')
    components: List[ScoreComponent] = Field(..., description="Variables required for calculation")
    
    # Logic and Evidence
    formula_latex: str
    calculation_logic: str = Field(..., description="Python-style logic for automation")
    reference_doi: List[str]
    
    # Interpretation (The 'So What?')
    interpretation_table: Optional[Dict[str, str]] = Field(
        None, description="Mapping score ranges to clinical outcomes/mortality"
    )

# search engine: 
# Hetop: https://www.hetop.eu/hetop/en/?q=&home
# Athena: https://athena.ohdsi.org/search-terms/start
# Loinc: https://loinc.org/search/
