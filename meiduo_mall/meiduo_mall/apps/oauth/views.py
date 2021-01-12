from django.views import View
from django import http
from QQLoginTool.QQtool import OAuthQQ
from django.conf import settings
import logging

from meiduo_mall.utils.response_code import RETCODE


# 创建日志输出器
logger = logging.getLogger('django')


class QQAuthURLView(View):
    '''提供QQ登录页面网址'''
    def get(self, request):
        # next表示从哪个页面进入到的登录页面，将来登录成功后，就自动回到那个页面
        next = request.GET.get('next')
        # 获取QQ登录页面网址
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET, redirect_uri=settings.QQ_REDIRECT_URI, state=next)
        login_url = oauth.get_qq_url()
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'login_url':login_url})


class QQAuthUserView(View):
    """用户扫码登录的回调处理"""

    def get(self, request):
        """Oauth2.0认证"""
        # 提取code请求参数
        code = request.GET.get('code')
        if not code:
            return http.HttpResponseForbidden('缺少code')

        # 创建工具对象
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET, redirect_uri=settings.QQ_REDIRECT_URI)

        try:
            # 使用code向QQ服务器请求access_token
            access_token = oauth.get_access_token(code)

            # 使用access_token向QQ服务器请求openid
            openid = oauth.get_open_id(access_token)
        except Exception as e:
            logger.error(e)
            return http.HttpResponseServerError('OAuth2.0认证失败')
        pass