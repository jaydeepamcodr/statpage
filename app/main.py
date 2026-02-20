from fastapi import FastAPI

from app.routers import status


def create_app() -> FastAPI:
    app = FastAPI(title="StatPage", version="0.1.0")
    app.include_router(status.router)
    return app


app = create_app()
