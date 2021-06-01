from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from urllib.request import urlopen
from urllib.parse import urlencode
import json
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class CaptchaAPIView(APIView):
    """验证码"""

    def get(self, request):
        """接受客户端提交的验证码相关信息"""
        UserIP = request._request.META.get('REMOTE_ADDR')
        print(f"用户的ip地址为:{UserIP}")
        params = urlencode({
            "aid": settings.TENCENT_CAPTCHA.get("APPID"),
            "AppSecretKey": settings.TENCENT_CAPTCHA.get("App_Secret_Key"),
            "Ticket": request.query_params.get('ticket'),
            "Randstr": request.query_params.get('randstr'),
            "UserIP": request._request.META.get('REMOTE_ADDR')
        })
        url = settings.TENCENT_CAPTCHA.get("GATEWAY")

        f = urlopen("%s?%s" % (url, params))
        content = f.read()
        res = json.loads(content)
        print(res)
        # {'response': '1', 'evil_level': '0', 'err_msg': 'OK'}
        if res:
            error_code = res["response"]
            if error_code == '1':
                return Response({
                    'detail': 1,
                    "msg": res["err_msg"]
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'detail': 0,
                    "msg": res["err_msg"]
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'detail': 0,
            "msg": '请求失败'
        }, status=status.HTTP_400_BAD_REQUEST)
