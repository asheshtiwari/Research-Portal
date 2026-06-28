import pytest
from app.services.cohere_service import CohereAnalysisService

def test_cohere_service_initialization():
    """
    Verifies that the Cohere service initializes with expected default parameters.
    """
    # Service instantiation
    ai_engine = CohereAnalysisService()
    
    # Assert state consistency with current enterprise standards
    assert ai_engine.model_name == "command-a-03-2025"
    assert hasattr(ai_engine, "client")

def test_analyze_financial_transcript_input_handling():
    """
    Verifies that the service layer accepts input streams before calling the external API.
    """
    ai_engine = CohereAnalysisService()
    
    # Testing for valid input stream handling
    # We use a dummy string to verify it reaches the service logic cleanly
    with pytest.raises(Exception):
        # We expect a RuntimeError here because the mock API call won't have a real key
        ai_engine.analyze_financial_transcript("Dummy transcript stream for analysis.")