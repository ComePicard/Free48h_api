from fastapi import FastAPI

from api.config import ConfigFastapi
from api.dao import get_pool
from api.endpoints import router
from api.endpoints.endpointsticket import router as router_ticket


def make_app() -> FastAPI:
    _app = FastAPI(
        title="MV-FLOW-LP-API",
        root_path=ConfigFastapi().openapi_prefix,
        swagger_ui_parameters={  # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
            "defaultModelsExpandDepth": 0,
            "docExpansion": "none",
            "syntaxHighlight.theme": "tomorrow-night",
            "tryItOutEnabled": True,
            "requestSnippetsEnabled": True,
        },
    )

    @_app.on_event("startup")
    def initialize_bdd_pool():
        get_pool()

    @_app.on_event("shutdown")
    def close_pool():
        cnx = get_pool()
        print("Fermeture de la piscine de connexions ❌")
        cnx.closeall()

    _app.include_router(router_ticket)
    _app.include_router(router)
    return _app
