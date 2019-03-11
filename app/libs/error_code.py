# -*- coding:utf-8 -*-
from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'success'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = '未知的异常'
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = "the resource are not found..."
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'