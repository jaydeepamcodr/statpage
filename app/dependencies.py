from app.db.session import get_db
from app.services.status import StatusService

# Re-export get_db for use in routers
__all__ = ["get_db", "get_status_service"]


def get_status_service() -> StatusService:
    return StatusService()
