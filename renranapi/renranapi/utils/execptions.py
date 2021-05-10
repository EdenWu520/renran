from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.Logger('loggers')


def custom_exception_handler(exc, context):
    """
    自定义异常处理函数
    :param exc: 异常类
    :param context: 抛出异常的上下文
    :return: Response响应
    """
    response = exception_handler(exc, context)
    if response is None:
        view = context['view']
        """当response的值为None, 则可能出现两种情况：①没有发生异常 ②本次异常没有被drf进行处理"""
        if isinstance(exc, DatabaseError):
            # 数据库异常
            logger.error(f'数据库发生异常, {view} {exc}')
            response = Response({
                'message': '服务器内部错误'
            }, status=status.HTTP_507_INSUFFICIENT_STORAGE)

        if isinstance(exc, Exception):
            # 未知错误
            logger.error(f'发生未知异常， {view} {exc}')
            response = Response({
                'message': '服务器内部错误'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
