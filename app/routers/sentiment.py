from fastapi import APIRouter, status

from app.schemas.sentiment import Sentiment
from app.services.sentiment import bert_sentiment_analysis

sentiment_router = APIRouter(prefix="")


@sentiment_router.post(
    "/sentiment_analysis",
    status_code=status.HTTP_200_OK,
    description="Predict sentiment of a given text",
    tags=["Sentiment Analysis"],
)
async def sentiment_analysis(request: Sentiment) -> dict[str, str]:
    response = bert_sentiment_analysis.infer(request)
    return {"sentiment_analysis": response}
