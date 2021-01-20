from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^areas/$', views.AreasView.as_view()),  # 省市区三级联动
]