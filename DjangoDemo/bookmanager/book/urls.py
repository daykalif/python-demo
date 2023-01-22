from django.conf.urls import url
from book.views import index

urlpatterns = [
    # index/
    # url的第一个参数是：正则
    # url的第二个参数是：视图函数名
    url(r'^index/$', index),
]
