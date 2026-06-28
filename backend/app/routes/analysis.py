import logging
import shutil
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, status

from app.config.settings import config
from app.models.response_schemas import UploadSuccessResponse
from app.services.document_service import DocumentProcessingService
from app.services.cohere_service import CohereAnalysisService

# Initialize standard application logger for server-side diagnostics
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/analysis", tags=["Financial Analysis Engine"])
ai_service = CohereAnalysisService()

@router.post("/upload", response_model=UploadSuccessResponse, status_code=status.HTTP_200_OK)
async def process_transcript_upload(file: UploadFile = File(...)):
    """
    Ingests financial transcript PDFs, extracts raw textual matrix, 
    and drives deterministic JSON summary synthesis via the Cohere LLM.
    """
    # Strict validation: Check both MIME type and extension to prevent spoofing
    if file.content_type != "application/pdf" and not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid asset format. Only standard PDF documents are supported for ingestion."
        )

    # Resolving temporary storage path using modern pathlib
    temp_file_path = Path(config.upload_dir) / f"temp_{file.filename}"

    try:
        # Securely persist the incoming byte stream to the temporary sandbox
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Execute text matrix extraction layer
        raw_text_stream = DocumentProcessingService.extract_text_from_pdf(str(temp_file_path))
        
        if not raw_text_stream.strip():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Document parsing yielded an empty text matrix. Ensure the PDF is not a scanned image."
            )

        # Route structural context directly into the semantic LLM runner
        structured_report = ai_service.analyze_financial_transcript(raw_text_stream)

        return UploadSuccessResponse(
            filename=file.filename,
            data=structured_report
        )

    except HTTPException:
        # Re-raise known API constraints to maintain appropriate HTTP status codes
        raise
    except Exception as e:
        # Secure error handling: Log actual fault internally, mask details from the client
        logger.error(f"Transcript processing pipeline fault: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal processing exception occurred during document evaluation."
        )
    finally:
        # Aggressive resource cleanup to prevent memory/storage leaks on the server node
        file.file.close()
        if temp_file_path.exists():
            temp_file_path.unlink()