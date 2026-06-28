import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolve project base directory paths cleanly using standard object orientation
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class ServerSettings(BaseSettings):
    """
    Manages operational parameters for the system application framework.
    Enforces required security token validation cycles prior to boot.
    """
    # Core API Keys
    cohere_api_key: str

    # Environment Configurations
    app_env: str = "development"
    upload_dir: str = "uploads"
    allowed_origins: str = "*"

    # Automatic environment field mapping and casing rules
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_nested_delimiter="__",
        case_sensitive=False  # Allows matching COHERE_API_KEY to cohere_api_key automatically
    )


# Instantiate settings context container
config = ServerSettings()

# Ensure target staging directory space exists before mounting routers
os.makedirs(config.upload_dir, exist_ok=True)