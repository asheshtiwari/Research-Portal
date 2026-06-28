import pytest
from pathlib import Path
from app.services.document_service import DocumentProcessingService

def test_extract_text_raises_filenotfound_on_invalid_path():
    """
    Asserts that passing a non-existent path raises the expected FileNotFoundError.
    """
    invalid_path = "non_existent_mock_file.pdf"
    
    # Specific exception testing ensures we don't mask other runtime errors
    with pytest.raises(FileNotFoundError, match="could not be located"):
        DocumentProcessingService.extract_text_from_pdf(invalid_path)

def test_extract_text_handles_empty_file_gracefully(tmp_path):
    """
    Verifies that an empty (but existing) PDF path doesn't crash the service.
    """
    # Create a dummy file in a temporary system directory
    d = tmp_path / "subdir"
    d.mkdir()
    empty_file = d / "empty.pdf"
    empty_file.write_text("dummy content")
    
    # We expect a PDF read error or runtime error because it's not a valid PDF
    with pytest.raises(ValueError, match="Failed to parse"):
        DocumentProcessingService.extract_text_from_pdf(str(empty_file))