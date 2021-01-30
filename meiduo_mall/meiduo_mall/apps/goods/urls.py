from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/(?P<category_id>\d+)/(?P<page_num>\d+)/$', views.ListView.as_view(), name='list'),  # 商品列表页
    url(r'^hot/(?P<category_id>\d+)/$', views.HotGoodsView.as_view()),  # 热销商品排行
    url(r'^detail/(?P<sku_id>\d+)/$', views.DetailView.as_view(), name='detail'),  # 商品详情
]