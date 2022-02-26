from fastapi.routing import APIRouter

from commercial_petproject.web.api import docs, echo, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
