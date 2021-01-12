from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^qq/login/$', views.QQAuthURLView.as_view()),  # QQ登录扫码页面
    url(r'^oauth_callback/$', views.QQAuthUserView.as_view()),  # 接收Authorization Code
]