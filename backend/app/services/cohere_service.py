import json
import logging
import re
import cohere
from app.config.settings import config
from app.models.response_schemas import AnalysisReport

logger = logging.getLogger(__name__)

class CohereAnalysisService:
    """
    Service layer for interacting with Cohere's LLM API.
    Responsible for extracting and validating structured financial data from raw text.
    """
    
    def __init__(self):
        self.client = cohere.Client(api_key=config.cohere_api_key)
        self.model_name = "command-a-03-2025"

    def analyze_financial_transcript(self, transcript_chunk: str) -> AnalysisReport:
        system_instruction = (
            "You are an equity research analyst reviewing corporate financial data. "
            "Extract key metrics and return them EXCLUSIVELY as a valid JSON object. "
            "Do not include markdown formatting, greetings, or conversational text.\n\n"
            "Required JSON Structure:\n"
            "{\n"
            '  "management_tone": "Optimistic" | "Cautious" | "Neutral" | "Pessimistic",\n'
            '  "confidence_level": "High" | "Medium" | "Low",\n'
            '  "key_positives": ["3 to 5 clear structural tailwinds"],\n'
            '  "key_challenges": ["3 to 5 critical macro hurdles"],\n'
            '  "forward_guidance": "Explicit revenue or margin targets",\n'
            '  "growth_initiatives": ["2 to 3 strategic expansion goals"]\n'
            "}\n\n"
            "If a specific metric is completely absent from the text, use 'Information not available'."
        )

        try:
            response = self.client.chat(
                model=self.model_name,
                preamble=system_instruction,
                message=f"Transcript content to parse:\n\n{transcript_chunk}",
                temperature=0.1
            )

            raw_payload = response.text.strip()

            
            json_match = re.search(r'(\{.*\})', raw_payload, re.DOTALL)
            if json_match:
                raw_payload = json_match.group(1)

            parsed_data = json.loads(raw_payload)
            return AnalysisReport.model_validate(parsed_data)

        except json.JSONDecodeError as decode_err:
            logger.error(f"Failed to decode JSON from LLM response. Raw output: {raw_payload}", exc_info=True)
            raise ValueError("Inference engine returned an invalid JSON structure.") from decode_err
        
        except Exception as api_err:
            logger.error("Cohere API communication failure.", exc_info=True)
            raise RuntimeError("Failed to process the transcript through the AI service.") from api_err