from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi_limiter import FastAPILimiter
from fastapi_pagination import add_pagination
from starlette.middleware.authentication import AuthenticationMiddleware


from backend.app.api.routers import v1_router
from backend.app.common.exceptions.exception_handler import register_exception
from backend.app.common.redis import redis_client
from backend.app.core.config import settings
from backend.app.utils.db_utils import create_all_tables
from backend.app.database.db_postgres import create_all_tables as create_all_tables_postgres
from backend.app.middleware.jwt_auth import JWTAuthMiddleware
from backend.app.middleware.opera_log import OperaLogMiddleware
from backend.app.utils.demo_site import create_demo_site
from backend.app.utils.health_check import ensure_unique_route_names, http_limit_callback
from backend.app.utils.openapi import simplify_operation_ids
from backend.app.utils.serializers import MsgSpecJSONResponse
