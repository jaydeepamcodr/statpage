from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine
from app.routers import status


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="StatPage", version="0.1.0", lifespan=lifespan)
    app.include_router(status.router)
    return app


# Import models so they register with Base.metadata
import app.models.status  # noqa: E402, F401

app = create_app()
