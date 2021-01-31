from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^carts/$', views.CartsView.as_view(), name='info'),  # 购物车
    url(r'^carts/selection/$', views.CartsSelectAllView.as_view()),  # 全选购物车
    url(r'^carts/simple/$', views.CartsSimpleView.as_view()),  # 简单购物车数据
]