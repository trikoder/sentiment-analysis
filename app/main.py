from fastapi import FastAPI

from app.routers.health import health_router
from app.routers.sentiment import sentiment_router

app = FastAPI(
    title="Sentiment Analysis API",
    docs_url="/",
    debug=False,
)
app.include_router(health_router)
app.include_router(sentiment_router)
