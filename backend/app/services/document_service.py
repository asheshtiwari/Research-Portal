import logging
from pathlib import Path
from pypdf import PdfReader
from pypdf.errors import PdfReadError

# Standard application logger
logger = logging.getLogger(__name__)

class DocumentProcessingService:
    """
    Handles the ingestion and text extraction of PDF documents.
    Optimized for processing corporate transcripts while respecting LLM context limits.
    """
    
    @staticmethod
    def extract_text_from_pdf(file_path: str, max_characters: int = 25000) -> str:
        target_path = Path(file_path)
        
        if not target_path.exists():
            logger.error(f"Target document not found at path: {file_path}")
            raise FileNotFoundError("The requested document could not be located on the server.")
            
        extracted_chunks = []
        
        try:
            reader = PdfReader(str(target_path))
            
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_chunks.append(page_text)
                    
            full_text = "\n".join(extracted_chunks)
            
            # Normalize whitespaces to prevent token waste during LLM processing
            sanitized_text = " ".join(full_text.split())
            
            # Enforce context window limits to prevent LLM API rejection
            if len(sanitized_text) > max_characters:
                logger.warning(f"Document exceeds max character limit ({max_characters}). Truncating text.")
                return sanitized_text[:max_characters]
                
            return sanitized_text
            
        except PdfReadError as pdf_err:
            # Catching specific PDF parsing errors instead of a generic Exception
            logger.error(f"Corrupted or unreadable PDF file: {file_path}", exc_info=True)
            raise ValueError("Failed to parse the PDF document. The file may be corrupted or encrypted.") from pdf_err
            
        except Exception as e:
            logger.error(f"Unexpected error during text extraction: {str(e)}", exc_info=True)
            raise RuntimeError("An internal error occurred while processing the document layout.") from e