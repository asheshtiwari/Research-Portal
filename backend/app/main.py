from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import config
from app.routes.analysis import router as analysis_router

def create_application() -> FastAPI:
    """
    Application factory for initializing the FastAPI server instance.
    """
    app = FastAPI(
        title="Equity Research Portal API",
        description="Backend services for financial transcript extraction and analysis.",
        version="1.0.0"
    )

    # Parse and validate CORS origins from environment configuration
    origins = [origin.strip() for origin in config.allowed_origins.split(",") if origin.strip()]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins if origins else ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Mount application routers
    app.include_router(analysis_router)

    @app.get("/health", tags=["Diagnostics"])
    def health_check():
        """
        Standard liveness probe for deployment orchestration (e.g., Docker/Kubernetes).
        """
        return {
            "status": "ok",
            "environment": config.app_env,
            "version": app.version
        }

    return app

# Application instance for ASGI server (Uvicorn)
app = create_application()