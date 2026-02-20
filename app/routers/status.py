from fastapi import APIRouter, Depends

from app.dependencies import get_status_service
from app.schemas.status import StatusResponse
from app.services.status import StatusService

router = APIRouter(prefix="/status", tags=["status"])


@router.get("/", response_model=StatusResponse)
def get_status(service: StatusService = Depends(get_status_service)):
    return service.get_current_status()
