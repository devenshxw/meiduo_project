from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^orders/settlement/$', views.OrderSettlementView.as_view(), name="settlement"),  # 结算订单
]