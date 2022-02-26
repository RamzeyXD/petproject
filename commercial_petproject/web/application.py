from importlib import metadata
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles

from commercial_petproject.web.api.router import api_router
from commercial_petproject.web.lifetime import shutdown, startup

APP_ROOT = Path(__file__).parent.parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="commercial_petproject",
        description="",
        version=metadata.version("commercial_petproject"),
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.on_event("startup")(startup(app))
    app.on_event("shutdown")(shutdown(app))

    app.include_router(router=api_router, prefix="/api")
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static",
    )

    return app
