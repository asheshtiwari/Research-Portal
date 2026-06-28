from enum import Enum
from pydantic import BaseModel, conlist


class ManagementToneEnum(str, Enum):
    """Strict categorical matrix boundaries for executive sentiment notation."""
    OPTIMISTIC = "Optimistic"
    CAUTIOUS = "Cautious"
    NEUTRAL = "Neutral"
    PESSIMISTIC = "Pessimistic"


class ConfidenceLevelEnum(str, Enum):
    """Explicit confidence ratings for metrics verification routing loops."""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class AnalysisReport(BaseModel):
    """
    Establishes the strict immutable semantic contract for transcript evaluations.
    Enforces absolute consistency limits before outbound networking hooks fire.
    """
    management_tone: ManagementToneEnum
    confidence_level: ConfidenceLevelEnum
    
    # Enforcing business validation layer thresholds directly on list streams
    key_positives: conlist(str, min_length=1, max_length=6)
    key_challenges: conlist(str, min_length=1, max_length=6)
    
    forward_guidance: str
    growth_initiatives: conlist(str, min_length=1, max_length=4)


class UploadSuccessResponse(BaseModel):
    """
    Standard corporate API response wrapper for structural file data streams.
    """
    filename: str
    status: str = "success"
    data: AnalysisReport