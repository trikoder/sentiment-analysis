from fastapi import APIRouter, status

health_router = APIRouter(prefix="")


@health_router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    description="Liveness Sentiment Analysis API health check",
    tags=["Sentiment Analysis"],
)
def health_check() -> dict[str, str]:
    return {"health": "UP"}
