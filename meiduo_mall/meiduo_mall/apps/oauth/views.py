from django.views import View
from django import http
from QQLoginTool.QQtool import OAuthQQ
from django.conf import settings

from meiduo_mall.utils.response_code import RETCODE


class QQAuthURLView(View):
    '''提供QQ登录页面网址'''
    def get(self, request):
        # next表示从哪个页面进入到的登录页面，将来登录成功后，就自动回到那个页面
        next = request.GET.get('next')
        # 获取QQ登录页面网址
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET, redirect_uri=settings.QQ_REDIRECT_URI, state=next)
        login_url = oauth.get_qq_url()
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'login_url':login_url})