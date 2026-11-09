from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.infrastructure.database.session import get_db

router = APIRouter(tags=["Health"])
settings = get_settings()


@router.get("/health", summary="Verificar que la API está activa")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}


@router.get("/health/ready", summary="Verificar la conexión con MySQL")
def readiness_check(db: Session = Depends(get_db)) -> dict[str, str]:
    try:
        db.execute(text("SELECT 1"))
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="No hay conexión con la base de datos.",
        ) from exc
    return {"status": "ready", "database": "connected"}