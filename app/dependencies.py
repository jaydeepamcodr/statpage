from app.services.status import StatusService


def get_status_service() -> StatusService:
    return StatusService()
