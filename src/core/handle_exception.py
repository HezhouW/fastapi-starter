from fastapi.exception_handlers import request_validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError,HTTPException
from starlette.responses import JSONResponse

from src.common.exception import AuthenticationError, AuthorizationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import Request
from loguru import logger

def register_exception_handler(app):

    @app.exception_handler(AuthenticationError)
    async def authentication_exception_handler(request: Request, e: AuthenticationError):
        """
        认证异常处理
        """
        return JSONResponse(status_code=401, content={"message": e.message})

    @app.exception_handler(AuthorizationError)
    async def authorization_exception_handler(request: Request, e: AuthorizationError):
        """
        权限异常处理
        """
        return JSONResponse(status_code=403, content={"message": e.message})

    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request: Request, exc):
        return await http_exception_handler(request, exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc):
        return await request_validation_exception_handler(request, exc)
    @app.exception_handler(HTTPException)
    async def validation_exception_handler(request: Request, exc):
        logger.error("OPS!!")
        return await http_exception_handler(request, exc)