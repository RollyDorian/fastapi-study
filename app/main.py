from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routes import router
from core.config import settings
from data.db import models
from schemas.models import MLModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    models[1] = MLModel(name="Logistic Regression", accuracy=0.84)
    models[2] = MLModel(name="Random Forest", accuracy=0.91)
    yield
    models.clear()


app = FastAPI(lifespan=lifespan, title=settings.app_name)
app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
