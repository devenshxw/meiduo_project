from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^payment/(?P<order_id>\d+)/$', views.PaymentView.as_view()),  # 订单支付
    url(r'^payment/status/$', views.PaymentStatusView.as_view()),  # 订单支付成功页面
]