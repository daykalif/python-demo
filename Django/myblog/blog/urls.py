from django.urls import path
from django.conf.urls import url

from . import views

# 设置路由的两种方式：
# 访问：http://127.0.0.1:8000/blog/article/1


app_name = '[blog]'

urlpatterns = [
    path('index/', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    # 第三步：添加页面的url   # 第八步：添加(?P<article_id>[0-9]+),用于接收article_id
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action')  # 第五步：添加响应请求的url
]
