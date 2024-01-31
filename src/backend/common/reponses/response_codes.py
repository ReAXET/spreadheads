import dataclasses
from enum import Enum
import json



class CustomCodeBase(Enum):

    @property
    def code(self):
        return self.value[0]
    

    @property
    def message(self):
        return self.value[1]
    


class CustomResponseCode(CustomCodeBase):
    HTTP_200 = (200, 'OK')
    HTTP_201 = (201, 'Created')
    HTTP_202 = (202, 'Accepted')
    HTTP_203 = (203, 'Non-Authoritative Information')
    HTTP_204 = (204, 'No Content')
    HTTP_400 = (400, 'Bad Request')
    HTTP_401 = (401, 'Unauthorized')
    HTTP_403 = (403, 'Forbidden')
    HTTP_404 = (404, 'Not Found')
    HTTP_410 = (410, 'Gone')
    HTTP_422 = (422, 'Unprocessable Entity')
    HTTP_425 = (425, 'Too Early')
    HTTP_429 = (429, 'Too Many Requests')
    HTTP_500 = (500, 'Internal Server Error')
    HTTP_501 = (501, 'Not Implemented')
    HTTP_502 = (502, 'Bad Gateway')
    HTTP_503 = (503, 'Service Unavailable')
    HTTP_504 = (504, 'Gateway Timeout')
    HTTP_505 = (505, 'HTTP Version Not Supported')
    HTTP_507 = (507, 'Insufficient Storage')
    HTTP_511 = (511, 'Network Authentication Required')
    HTTP_520 = (520, 'Unknown Error')


class CustomErrorCode(CustomCodeBase):
    CAPTCHA_ERROR = (40001, 'Captcha Error')
    AUTHORIZATION_ERROR = (40002, 'Authorization Error')


@dataclasses.dataclass
class CustomResponse:
    code: int
    message: str
    data: dict = dataclasses.field(default_factory=dict)
    error: dict = dataclasses.field(default_factory=dict)
    

    def __post_init__(self):
        if self.code >= 400:
            self.error = {
                'code': self.code,
                'message': self.message
            }
        else:
            self.data = {
                'code': self.code,
                'message': self.message
            }
        
    

    def __repr__(self):
        return f'<CustomResponse {self.code} {self.message}>'
    
    

    def __str__(self):
        return f'<CustomResponse {self.code} {self.message}>'
    
    

    def to_dict(self):
        return dataclasses.asdict(self)
    
    

    def to_json(self):
        return json.dumps(self.to_dict())
    
    

    def to_tuple(self):
        return (self.code, self.message)
    
    

    def to_tuple_with_data(self):
        return (self.code, self.message, self.data)
    
    

    def to_tuple_with_error(self):
        return (self.code, self.message, self.error)
    


class StandardResponseCodes:
    HTTP_100 = 100
    HTTP_101 = 101
    HTTP_102 = 102
    HTTP_103 = 103
    HTTP_200 = 200
    HTTP_201 = 201
    HTTP_202 = 202
    HTTP_203 = 203
    HTTP_204 = 204
    HTTP_205 = 205
    HTTP_206 = 206
    HTTP_207 = 207
    HTTP_208 = 208
    HTTP_226 = 226
    HTTP_300 = 300
    HTTP_301 = 301
    HTTP_302 = 302
    HTTP_303 = 303
    HTTP_304 = 304
    HTTP_305 = 305
    HTTP_306 = 306
    HTTP_307 = 307
    HTTP_308 = 308
    HTTP_400 = 400
    HTTP_401 = 401
    HTTP_402 = 402
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_405 = 405
    HTTP_406 = 406
    HTTP_407 = 407
    HTTP_408 = 408
    HTTP_409 = 409
    HTTP_410 = 410
    HTTP_411 = 411
    HTTP_412 = 412
    HTTP_413 = 413
    HTTP_414 = 414
    HTTP_415 = 415
    HTTP_416 = 416
    HTTP_417 = 417
    HTTP_418 = 418
    HTTP_421 = 421
    HTTP_422 = 422
    HTTP_423 = 423
    HTTP_424 = 424
    HTTP_425 = 425
    HTTP_426 = 426
    HTTP_428 = 428
    HTTP_429 = 429
    HTTP_431 = 431
    HTTP_451 = 451
    HTTP_500 = 500
    HTTP_501 = 501
    HTTP_502 = 502
    HTTP_503 = 503
    HTTP_504 = 504
    HTTP_505 = 505
    HTTP_506 = 506
    HTTP_507 = 507
    HTTP_508 = 508
    HTTP_510 = 510
    HTTP_511 = 511

    """Websocket status codes"""
    WS_1000 = (1000, 'Normal Closure')
    WS_1001 = (1001, 'Going Away')
    WS_1002 = (1002, 'Protocol Error')
    WS_1003 = (1003, 'Unsupported Data')
    WS_1004 = (1004, 'Reserved')
    WS_1005 = (1005, 'No Status Rcvd')
    WS_1006 = (1006, 'Abnormal Closure')
    WS_1007 = (1007, 'Invalid frame payload data')
    WS_1008 = (1008, 'Policy Violation')
    WS_1009 = (1009, 'Message Too Big')
    WS_1010 = (1010, 'Mandatory Ext.')
    WS_1011 = (1011, 'Internal Server Error')
    WS_1012 = (1012, 'Service Restart')
    WS_1013 = (1013, 'Try Again Later')
    WS_1014 = (1014, 'Bad Gateway')
    WS_1015 = (1015, 'TLS Handshake')
    WS_1016 = (1016, 'TLS Handshake')
    WS_1017 = (1017, 'Bad Gateway')
    WS_1018 = (1018, 'Bad Gateway')
    
    WS_3000 = (3000, 'Bad Gateway')
    WS_3003 = (3003, 'Bad Gateway')


