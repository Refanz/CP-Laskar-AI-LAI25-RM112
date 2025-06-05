from fastapi import FastAPI
from app.api.endpoint import router
from app.core.config import settings

app = FastAPI(
    title="Palm Oil Disease Detection App",
    version=settings.PROJECT_VERSION,
    description="A simple FASTAPI project for model classification"
)

app.include_router(
    router=router,
    prefix="/api/v1",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Classify Palm Oil Disease Model API"
    }
