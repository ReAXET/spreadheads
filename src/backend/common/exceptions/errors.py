"""Custom errors for the application."""

from typing import Optional, Any
from fastapi import HTTPException, status
from starlette.background import BackgroundTask
from backend.common.reponses.response_codes import CustomErrorCode, StandardResponseCodes


class BaseExceptionMixin(Exception):
    """Base Exception Mixin for all custom exceptions."""

    code: int
    
    def __init__(self, *, message = None, data: Any = None, background: BackgroundTask | None = None):
        self.message = message
        self.data = data
        self.background = background
    


class HTTPError(HTTPException):
    def __init__(self, *, code: int, message: str, headers: dict[str, Any] | None = None):
        super().__init__(status_code=code, detail=message, headers=headers)



class CustomError(BaseExceptionMixin):
    def __init__(self, *, error: CustomErrorCode, data: Any = None, background: BackgroundTask | None = None):
        self.code = error.code
        super().__init__(message=error.message, data=data, background=background)   


class RequestError(BaseExceptionMixin):
    code = StandardResponseCodes.HTTP_400
    def __init__(self, *, message: str = 'Bad Request', data: Any = None, background: BackgroundTask | None = None):
        super().__init__(message=message, data=data, background=background)

class ForbiddenError(BaseExceptionMixin):
    code = StandardResponseCodes.HTTP_403
    def __init__(self, *, message: str = 'Forbidden', data: Any = None, background: BackgroundTask | None = None):
        super().__init__(message=message, data=data, background=background)


class NotFoundError(BaseExceptionMixin):
    code = StandardResponseCodes.HTTP_404
    def __init__(self, *, message: str = 'Not Found', data: Any = None, background: BackgroundTask | None = None):
        super().__init__(message=message, data=data, background=background)


class ServerError(BaseExceptionMixin):
    code = StandardResponseCodes.HTTP_500
    def __init__(self, *, message: str = 'Internal Server Error', data: Any = None, background: BackgroundTask | None = None):
        super().__init__(message=message, data=data, background=background)


class GatewayError(BaseExceptionMixin):
    code = StandardResponseCodes.HTTP_502
    def __init__(self, *, message: str = 'Bad Gateway', data: Any = None, background: BackgroundTask | None = None):
        super().__init__(message=message, data=data, background=background)


class AuthorizationError(BaseExceptionMixin):
    code = StandardResponseCodes.HTTP_401
    def __init__(self, *, message: str = 'Unauthorized', data: Any = None, background: BackgroundTask | None = None):
        super().__init__(message=message, data=data, background=background)


class TokenExpiredError(BaseExceptionMixin):
    code = StandardResponseCodes.HTTP_401
    def __init__(self, *, message: str = 'Token Expired', data: Any = None, background: BackgroundTask | None = None):
        super().__init__(message=message, data=data, background=background)


