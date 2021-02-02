from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^orders/settlement/$', views.OrderSettlementView.as_view(), name="settlement"),  # 结算订单
    url(r'^orders/commit/$', views.OrderCommitView.as_view(), name="commit"),  # 提交订单
    url(r'^orders/success/$', views.OrderSuccessView.as_view(), name="success"),  # 提交订单成功
    url(r'^orders/info/(?P<page_num>\d+)/$', views.UserOrderInfoView.as_view(), name="info"),  # 我的订单
]