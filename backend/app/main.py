from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import config
from app.routes.analysis import router as analysis_router

def create_application() -> FastAPI:
    app = FastAPI(
        title="Equity Research Portal API",
        description="Backend services for financial transcript extraction and analysis.",
        version="1.0.0"
    )

    
    origins = [origin.strip() for origin in config.allowed_origins.split(",") if origin.strip()]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins if origins else ["*"], # Agar env set nahi hai toh "*" fallback lega
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(analysis_router)

    @app.get("/health", tags=["Diagnostics"])
    def health_check():
        return {
            "status": "ok",
            "environment": config.app_env,
            "version": app.version
        }

    return app

app = create_application()