from app.schemas.status import StatusResponse


class StatusService:
    def get_current_status(self) -> StatusResponse:
        return StatusResponse(status="operational", message="All systems operational")
